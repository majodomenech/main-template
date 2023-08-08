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
# drop table IF EXISTS bbg.des;
# CREATE TABLE bbg.fields
# (
#     id character varying,
#     mnemonic character varying,
#     title character varying,
#     description character varying,
#     data jsonb,
#     PRIMARY KEY (id)
# )
# WITH (
#     OIDS = FALSE
# );

def __get_field(credentials: str, field_id: str):
    SESSION, SSE_CLIENT = connect(credentials=credentials)
    try:
        request_url = urljoin(HOST, f'/eap/catalogs/bbg/fields/{field_id}')
        response = SESSION.get(request_url)
        # Check it went well and extract the URL of the created request.
        handle_response(response)
        return response.json()
    finally:
        try:
            SESSION.close()
        except:
            pass
        try:
            SSE_CLIENT.close()
        except:
            pass


def __get_fields(credentials: str, page: int = 1, queryParams: str = None):
    SESSION, SSE_CLIENT = connect(credentials=credentials)
    try:
        request_url = urljoin(HOST, f'/eap/catalogs/bbg/fields/?page={page}')
        if queryParams is not None:
            request_url += "&" + queryParams
        response = SESSION.get(request_url)
        # Check it went well and extract the URL of the created request.
        handle_response(response)
        return response.json()
    finally:
        try:
            SESSION.close()
        except:
            pass
        try:
            SSE_CLIENT.close()
        except:
            pass


def __update_field(connection, data: dict):
    try:
        with connection.cursor() as cursor:
            # Sentencia SQL para insertar el registro
            sql_insert = """
                INSERT INTO bbg.fields(id, mnemonic, title, description, data)
	            VALUES (%(id)s, %(mnemonic)s, %(title)s, %(description)s, %(data)s)
                ON CONFLICT (id) DO UPDATE 
                SET data = %(data)s,
                    mnemonic = %(mnemonic)s,
                    title = %(title)s,
                    description = %(description)s
            """
            datos_a_insertar = {
                "id": data['identifier'],
                "mnemonic": data['Mnemonic'],
                "title": data['title'],
                "description": data['description'],
                "data": data
            }

            # Ejecuta la consulta de inserción con los datos proporcionados
            cursor.execute(sql_insert, datos_a_insertar)
    except Exception as e:
        print("Error:", e)


def update_fields(bpm: redflagbpm.BPMService, queryParams: str = None):
    credentials = bpm.service.text("BBG_CREDENTIALS")

    page = 1
    last = 2
    while page <= last:
        data = __get_fields(credentials, page, queryParams)
        last = data['pageCount']
        if len(data['contains']) == 0:
            break
        with get_connection(bpm, 'FLW') as connection:
            for field in data['contains']:
                field_data = __get_field(credentials, field['identifier'])
                __update_field(connection, field_data)
        page += 1


def snake_upper_to_camel(snake_upper_str):
    components = snake_upper_str.split('_')
    camel_str = components[0].lower() + ''.join(x.capitalize() for x in components[1:])
    return camel_str


def update_missing(bpm: redflagbpm.BPMService, mnemonics: list):
    credentials = bpm.service.text("BBG_CREDENTIALS")
    with get_connection(bpm, 'FLW') as connection:
        for mnemonic in mnemonics:
            identifier = snake_upper_to_camel(mnemonic)
            # check if exists in database
            with connection.cursor() as cursor:
                sql_select = """
                    SELECT id FROM bbg.fields WHERE id = %(id)s
                """
                cursor.execute(sql_select, {"id": identifier})
                if cursor.rowcount > 0:
                    continue

            field_data = __get_field(credentials, identifier)
            __update_field(connection, field_data)


def update_field(bpm: redflagbpm.BPMService, identifier: str):
    credentials = bpm.service.text("BBG_CREDENTIALS")
    with get_connection(bpm, 'FLW') as connection:
        field_data = __get_field(credentials, identifier)
        __update_field(connection, field_data)
