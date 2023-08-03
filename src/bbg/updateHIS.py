import psycopg2.extras
import redflagbpm
from redflagbpm.PgUtils import get_pool, get_connection
import json
import os
import datetime
import logging
import pprint
import uuid
from urllib.parse import urljoin
from utils.bbgConnect import connect
from bwslib.bws_auth import download, handle_response
from psycopg2.pool import SimpleConnectionPool
from psycopg2.extensions import register_adapter, QuotedString
import json

LOG = logging.getLogger(__name__)
HOST = 'https://api.bloomberg.com'


def adapt_dict(dict_var):
    return QuotedString(json.dumps(dict_var))


register_adapter(dict, adapt_dict)
register_adapter(list, adapt_dict)

# Database
# ===================================================================
# create schema bbg;
# drop table IF EXISTS bbg.his;
# CREATE TABLE IF NOT EXISTS bbg.his
# (
#     id character varying COLLATE pg_catalog."default",
#     target_date date,
#     data jsonb,
#     last_update timestamp without time zone,
#     CONSTRAINT his_pkey PRIMARY KEY (id,target_date)
# );

HISTORY_FIELD_LIST = [
    {'mnemonic': 'PX_LAST'},
    {'mnemonic': 'PX_BID'},
    {'mnemonic': 'PX_ASK'},
    {'mnemonic': 'YLD_YTM_BID'},
    {'mnemonic': 'YLD_YTM_ASK'},
]


def __get_history(credentials: str, isin_list: list, start_date: str, end_date: str, periodicity='daily'):
    try:
        SESSION, SSE_CLIENT = connect(credentials=credentials)

        ############################################################################
        # - Discover catalog identifier for scheduling requests
        catalogs_url = urljoin(HOST, '/eap/catalogs/')
        response = SESSION.get(catalogs_url)

        # Extract a/the account number from the response.
        handle_response(response)

        # We got back a good response. Let's extract our account number
        catalogs = response.json()['contains']
        for catalog in catalogs:
            if catalog['subscriptionType'] == 'scheduled':
                # Take the catalog having "scheduled" subscription type,
                # which corresponds to the Data License account number.
                catalog_id = catalog['identifier']
                break
        else:
            # We exhausted the catalogs, but didn't find a non-'bbg' catalog.
            LOG.error('Scheduled catalog not in %r', response.json()['contains'])
            raise RuntimeError('Scheduled catalog not found')

        ############################################################################
        # # Request

        ############################################################################
        # - Create the request component.
        # Generate a timestamp and random ID so we can create unique component identifiers
        # NOTE The request_id must be 21 characters or less
        request_id = 'r' + datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S') + str(uuid.uuid1())[:6]

        instruments = []
        for isin in isin_list:
            instruments.append({
                '@type': 'Identifier',
                'identifierType': 'ISIN',
                'identifierValue': isin,
            })

        request_payload = {
            '@type': 'HistoryRequest',
            'identifier': request_id,
            'name': 'HistoryRequest' + request_id,
            'description': 'Requesting history for: ' + ', '.join(isin_list),
            'universe': {
                '@type': 'Universe',
                'contains': instruments
            },
            'fieldList': {
                '@type': 'HistoryFieldList',
                'contains': HISTORY_FIELD_LIST,
            },
            'trigger': {
                "@type": "SubmitTrigger",
            },
            'runtimeOptions': {
                '@type': 'HistoryRuntimeOptions',
                'dateRange': {
                    '@type': 'IntervalDateRange',
                    'startDate': start_date,
                    'endDate': end_date
                },
                "period": periodicity
            },
            'formatting': {
                '@type': 'MediaType',
                'outputMediaType': 'application/json',
            }
        }
        LOG.info('Request component payload:\n%s', pprint.pformat(request_payload))

        account_url = urljoin(HOST, '/eap/catalogs/{c}/'.format(c=catalog_id))
        requests_url = urljoin(account_url, 'requests/')
        response = SESSION.post(requests_url, json=request_payload)

        # Check it went well and extract the URL of the created request.
        handle_response(response)

        request_location = response.headers['Location']
        request_url = urljoin(HOST, request_location)

        LOG.info('%s resource has been successfully created at %s',
                 request_id,
                 request_url)

        ############################################################################
        # - Inspect the newly-created request component.
        SESSION.get(request_url)
        reply_timeout = datetime.timedelta(minutes=45)
        expiration_timestamp = datetime.datetime.utcnow() + reply_timeout
        while datetime.datetime.utcnow() < expiration_timestamp:
            # Read the next available event
            event = SSE_CLIENT.read_event()

            if event.is_heartbeat():
                LOG.info('Received heartbeat event, keep waiting for events')
                continue

            LOG.info('Received reply delivery notification event: %s', event)
            event_data = json.loads(event.data)

            try:
                distribution = event_data['generated']
                reply_url = distribution['@id']
                distribution_id = distribution['identifier']

                dataset = distribution['snapshot']['dataset']
                dataset_id = dataset['identifier']

                catalog = dataset['catalog']
                reply_catalog_id = catalog['identifier']
            except KeyError:
                LOG.info("Received other event type, continue waiting")
            else:
                is_required_reply = request_id == dataset_id
                is_same_catalog = reply_catalog_id == catalog_id

                if not is_required_reply or not is_same_catalog:
                    LOG.info("Some other delivery occurred - continue waiting")
                    continue

                output_file_path = os.path.join('/tmp', distribution_id)

                # Add 'Accept-Encoding: gzip' header to reduce download time.
                # Note that the vast majority of dataset files exceed 100MB in size,
                # so compression will speed up downloading significantly.
                headers = {'Accept-Encoding': 'gzip'}
                download(SESSION,
                         reply_url,
                         output_file_path,
                         headers=headers)
                LOG.info('Reply was downloaded')
                return output_file_path
        else:
            LOG.info('Reply NOT delivered, try to increase waiter loop timeout')
    finally:
        try:
            SESSION.close()
        except:
            pass
        try:
            SSE_CLIENT.close()
        except:
            pass


def __update_data(connection, data: dict):
    try:
        with connection.cursor() as cursor:
            # Sentencia SQL para insertar el registro
            sql_insert = """
                INSERT INTO bbg.his as his (id, target_date, data, last_update)
                VALUES (%(id)s, %(target_date)s::date, %(data)s::jsonb, current_timestamp)
                ON CONFLICT (id, target_date) DO UPDATE 
                SET data = his.data||excluded.data, 
                    last_update = excluded.last_update 
            """
            for instrument in data:
                if instrument['DATE'] is None:
                    continue
                # Ejemplo de datos que deseas insertar en la tabla
                LOG.info('Inserting/updating ' + instrument['DATE'] + " - " + instrument['IDENTIFIER'] + '...')
                datos_a_insertar = {
                    "id": instrument['IDENTIFIER'],
                    "target_date": instrument['DATE'],
                    "data": instrument
                }

                # Ejecuta la consulta de inserción con los datos proporcionados
                cursor.execute(sql_insert, datos_a_insertar)
    except Exception as e:
        print("Error:", e)


def update_history(bpm: redflagbpm.BPMService, isin_list: list, start_date: str, end_date: str, periodicity: str):
    credentials = bpm.service.text("BBG_CREDENTIALS")
    file = __get_history(credentials, isin_list, start_date, end_date, periodicity)
    # parse json file
    with open(file) as f:
        data = json.load(f)
    # insert into database
    with get_connection(bpm, 'FLW') as connection:
        __update_data(connection, data)
