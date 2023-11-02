#!python3
import json
import re
import urllib
from datetime import date, timedelta
import redflagbpm
from decimal import Decimal
import psycopg2
import psycopg2.extras

from DB_connect import _get_hg_connection
from endpoints_santander import login_apigee, get_all_funds, get_fund_by_id, get_fund_by_id_details

def call_stdr_fund_endpoints(headers):
    response = get_all_funds(headers)
    all_funds = json.dumps(response.json(), indent=4, sort_keys=True, ensure_ascii=False)
    all_funds = json.loads(all_funds)
    for fund in all_funds['results']:
        response_by_id_details = get_fund_by_id_details(headers, fund['id'])
        response_by_id_details = json.dumps(response_by_id_details.json(), indent=4, sort_keys=True, ensure_ascii=False)
        response_by_id_details = json.loads(response_by_id_details)
        fund['codigo_cv'] = response_by_id_details['CVCode']

    # pretty print all_funds
    pretty_all_funds = json.dumps(all_funds, indent=4, sort_keys=True, ensure_ascii=False)
    return pretty_all_funds

def insert_strdr_fund_id(conn, **kwargs):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    """
    SQL para escribir el campo cada vez (no hacemos insert on conflict)
    """

    # update = """
    #  """
    # val_list = []
    #
    # params = tuple(val_list)
    # cur.execute(update, params)
    # cur.close()

    for k, v in kwargs.items():
        print(k, v)
    pass

#!python3
import redflagbpm
from redflagbpm import PgUtils

bpm = redflagbpm.BPMService()

def update_fund_id(conn, **kwargs):
    conn.autocommit = False
    sql_actualizar = """
                        update public."UNI_ATRIBUTO"
                        set "VALOR"= %s
                        where "UNIDAD"=(select "UNI_UNIDAD_ID" from "UNI_UNIDAD" where "SUBCODIGO"= %s)
                        and "ATRIBUTO" = %s;
                    """
    sql_insertar = """
                            INSERT INTO public."UNI_ATRIBUTO"("UNIDAD", "ATRIBUTO", "VALOR")
                            VALUES ((select "UNI_UNIDAD_ID" from "UNI_UNIDAD" where "SUBCODIGO"=%s), %s, %s);
                        """
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    for k, v in kwargs.items():
        print(k,v)
    conn.autocommit = False




def main():
    headers = login_apigee()
    # bpm = redflagbpm.BPMService()
    conn = _get_hg_connection('syc')
    funds_w_cv_code = call_stdr_fund_endpoints(headers)
    update_fund_id(conn, **{'stdr_fund_id': 1, 'cv_id': 1})
    for i in json.loads(funds_w_cv_code)['results']:
        insert_strdr_fund_id(conn, **{'stdr_fund_id': i['id'], 'cv_id': i['codigo_cv']})


if __name__ == '__main__':
    main()
