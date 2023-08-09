import psycopg2.extras
import redflagbpm
from redflagbpm.PgUtils import get_connection
import os
import datetime
import logging
import pprint
import uuid
from urllib.parse import urljoin
from utils.bbgConnect import connect
from bwslib.bws_auth import download, handle_response
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
# drop table IF EXISTS bbg.des;
# CREATE TABLE IF NOT EXISTS bbg.des
# (
#     id character varying COLLATE pg_catalog."default" NOT NULL,
#     id_hg bigint,
#     id_isin character varying(12) COLLATE pg_catalog."default",
#     id_cusip character varying(9) COLLATE pg_catalog."default",
#     name character varying COLLATE pg_catalog."default",
#     data jsonb,
#     cash_flow jsonb,
#     factor_schedule jsonb,
#     last_update timestamp without time zone,
#     CONSTRAINT des_pkey PRIMARY KEY (id)
# );

DATA_FIELD_LIST = (
    'NAME',
    'LONG_COMP_NAME',
    'INSTRUMENT_FULL_NAME',
    'EXCH_NAMES',
    'PRIMARY_EXCHANGE_NAME',
    'SECURITY_TYP',
    'COUNTRY',
    'CRNCY',
    'ID_ISIN',
    'TICKER',
    'MATURITY',
    'MIN_PIECE',
    'CPN',
    'INT_ACC',
    'SINKING_FUND_FACTOR',
    'RTG_SP',
    'RTG_FITCH',
    'RTG_MOODY',
    'BB_COMPOSITE',
    'ID_BB_UNIQUE',
    'ISSUE_DT',
    'ID_CUSIP',
    'ID_BB_GLOBAL',
    'ID_BB_COMPANY',
    'CPN_FREQ',
    'PAR_AMT',
    'AMT_OUTSTANDING',
    'CNTRY_ISSUE_ISO',
    'FIRST_CPN_DT',
    'CALC_TYP',
    'AMT_ISSUED',
    'DAY_CNT_DES',
    'INT_ACC_DT',
    'MIN_INCREMENT',
    'ISSUE_PX',
    'FIRST_SETTLE_DT',
    'MARKET_ISSUE',
    'CNTRY_OF_RISK',
    'PAYMENT_RANK',
    'LEAD_MGR',
    'IS_TRACE_ELIGIBLE',
    'DES_NOTES',
    'USE_OF_PROCEEDS',
    'BC_USE_OF_PROCEEDS',
    'STEP_UP_DOWN_PROVISION',
    'CHNG_OF_CONTROL_COVENANT',
    'HYBRID_CUMULATIVE_INDICATOR',
    'CLASSIFICATION_SCHEME',
    'ID_LOCAL'
)


def __get_detail(credentials: str, isin_list: list, fields: list = DATA_FIELD_LIST, target_date: str = None):
    try:
        if fields is None:
            fields = DATA_FIELD_LIST

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
            if target_date is not None:
                instruments.append({
                    '@type': 'Identifier',
                    'identifierType': 'ISIN',
                    'identifierValue': isin,
                    "fieldOverrides": [
                        {
                            "@type": "FieldOverride",
                            "mnemonic": "SETTLE_DT",
                            "override": target_date
                        }
                    ]
                })
            else:
                instruments.append({
                    '@type': 'Identifier',
                    'identifierType': 'ISIN',
                    'identifierValue': isin,
                })

        request_payload = {
            '@type': 'DataRequest',
            'identifier': request_id,
            'name': 'DataRequest' + request_id,
            'description': 'Requesting data for: ' + ', '.join(isin_list),
            'universe': {
                '@type': 'Universe',
                'contains': instruments
            },
            'fieldList': {
                '@type': 'DataFieldList',
                'contains': [{'mnemonic': i} for i in fields],
            },
            'trigger': {
                "@type": "SubmitTrigger",
            },
            'formatting': {
                '@type': 'MediaType',
                'outputMediaType': 'application/json',
            }
        }

        LOG.info('Request component payload:\n%s', pprint.pformat(request_payload))

        catalog_url = urljoin(HOST, '/eap/catalogs/{c}/'.format(c=catalog_id))
        requests_url = urljoin(catalog_url, 'requests/')
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


def __get_cashflow(credentials: str, isin_dict: dict):
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
        for isin, dt in isin_dict.items():
            if dt is not None:
                instruments.append({
                    '@type': 'Identifier',
                    'identifierType': 'ISIN',
                    'identifierValue': isin,
                    "fieldOverrides": [
                        {
                            "@type": "FieldOverride",
                            "mnemonic": "SETTLE_DT",
                            "override": dt.replace('-', '')
                        }
                    ]
                })

        request_payload = {
            '@type': 'DataRequest',
            'identifier': request_id,
            'name': 'DataRequest' + request_id,
            'description': 'Requesting data for: ' + ', '.join(isin_dict.keys()),
            'universe': {
                '@type': 'Universe',
                'contains': instruments
            },
            'fieldList': {
                '@type': 'DataFieldList',
                'contains': [
                    {'mnemonic': 'DES_CASH_FLOW'},
                    {'mnemonic': 'FACTOR_SCHEDULE'}
                ],
            },
            'trigger': {
                "@type": "SubmitTrigger",
            },
            'formatting': {
                '@type': 'MediaType',
                'outputMediaType': 'application/json',
            }
        }
        LOG.info('Request component payload:\n%s', pprint.pformat(request_payload))

        catalog_url = urljoin(HOST, '/eap/catalogs/{c}/'.format(c=catalog_id))
        requests_url = urljoin(catalog_url, 'requests/')
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
                INSERT INTO bbg.des (id_hg, id_isin, id_cusip, id, name, data, last_update)
                VALUES (%(id_hg)s, %(id_isin)s, %(id_cusip)s, %(id)s, %(name)s, %(data)s, current_timestamp)
                ON CONFLICT (id) DO UPDATE 
                SET data = %(data)s, 
                    last_update = current_timestamp, 
                    id_isin = %(id_isin)s, 
                    id_cusip = %(id_cusip)s, 
                    name = %(name)s
            """
            for instrument in data:
                # Ejemplo de datos que deseas insertar en la tabla
                LOG.info('Inserting/updating history: ' + instrument['IDENTIFIER'] + ' ' + instrument[
                    'INSTRUMENT_FULL_NAME'] + '...')
                datos_a_insertar = {
                    "id": instrument['IDENTIFIER'],
                    "id_hg": None,
                    "id_isin": instrument['IDENTIFIER'],
                    "id_cusip": instrument['ID_CUSIP'],
                    "name": instrument['INSTRUMENT_FULL_NAME'],
                    "data": instrument
                }

                # Ejecuta la consulta de inserción con los datos proporcionados
                cursor.execute(sql_insert, datos_a_insertar)
    except Exception as e:
        print("Error:", e)


def __update_flows(connection, data: dict):
    try:
        with connection.cursor() as cursor:
            # Sentencia SQL para actualizar el registro
            sql_insert = """
                update bbg.des 
                SET cash_flow= %(cash_flow)s, 
                    factor_schedule= %(factor_schedule)s,
                    last_update = current_timestamp 
                where id_isin = %(id_isin)s  or id = %(id)s
            """
            for instrument in data:
                LOG.info('Inserting/updating cashflow ' + instrument['IDENTIFIER'] + '...')
                datos_a_actualizar = {
                    "id": instrument['IDENTIFIER'],
                    "id_isin": instrument['IDENTIFIER'],
                    "cash_flow": instrument['DES_CASH_FLOW'],
                    "factor_schedule": instrument['FACTOR_SCHEDULE']
                }

                # Ejecuta la consulta de inserción con los datos proporcionados
                cursor.execute(sql_insert, datos_a_actualizar)
    except Exception as e:
        print("Error:", e)


def update_instruments(bpm: redflagbpm.BPMService, isin_list: list, fields: list):
    credentials = bpm.service.text("BBG_CREDENTIALS")
    file = __get_detail(credentials, isin_list, fields)
    # parse json file
    with open(file) as f:
        data = json.load(f)
    # insert into database
    with get_connection(bpm, 'FLW') as connection:
        __update_data(connection, data)


def update_instruments_and_cashflows(bpm: redflagbpm.BPMService, isin_list: list, fields: list):
    update_instruments(bpm, isin_list, fields)
    update_cashflows(bpm)


def update_cashflows(bpm: redflagbpm.BPMService):
    credentials = bpm.service.text("BBG_CREDENTIALS")

    with get_connection(bpm, 'FLW') as connection:
        with connection.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("""
                select id_isin, data#>>'{ISSUE_DT}' as issue_dt 
                from bbg.des 
                where cash_flow is null and data#>>'{ISSUE_DT}' is not null
            """)
            instrument_list = cursor.fetchall()
            isin_dict = {x['id_isin']: x['issue_dt'] for x in instrument_list}
            if len(isin_dict) != 0:
                file = __get_cashflow(credentials, isin_dict)
                # parse json file
                with open(file) as f:
                    data = json.load(f)
                # insert into database
                __update_flows(connection, data)


def __update_date(connection, data: dict, target_date: str):
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
                LOG.info('Inserting/updating ' + target_date + " - " + instrument['IDENTIFIER'] + '...')
                datos_a_insertar = {
                    "id": instrument['IDENTIFIER'],
                    "target_date": target_date,
                    "data": instrument
                }

                # Ejecuta la consulta de inserción con los datos proporcionados
                cursor.execute(sql_insert, datos_a_insertar)
    except Exception as e:
        print("Error:", e)


def update_date(bpm: redflagbpm.BPMService, isin_list: list, fields: list, target_date: str):
    credentials = bpm.service.text("BBG_CREDENTIALS")
    file = __get_detail(credentials, isin_list, fields, target_date)
    # parse json file
    with open(file) as f:
        data = json.load(f)
    # insert into database
    with get_connection(bpm, 'FLW') as connection:
        __update_date(connection, data, target_date)
