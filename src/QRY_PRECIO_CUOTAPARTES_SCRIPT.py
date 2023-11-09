#!python3
import json

import psycopg2
import redflagbpm
import psycopg2.extras
from DB_connect import _get_hg_connection
from endpoints_santander import login_apigee, get_all_funds, get_fund_by_id

def get_codigo_fci(conn, fundId):

    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    sql = """
        select uni."CODIGO", '['|| uni."CODIGO" ||'] ' || uni."NOMBRE" as fci
        --        atr."VALOR" as fund_id
        from "UNI_UNIDAD" uni
            inner join "UNI_ATRIBUTO" atr on atr."UNIDAD"=uni."UNI_UNIDAD_ID" and atr."ATRIBUTO" = 'FundId Santander'
        where atr."VALOR" = %s
    """
    cur.execute(sql, (fundId,))
    row = cur.fetchone()
    if row:
        return row
    else:
        return None
    cur.close()
    conn.close()
    return row


def main():
    headers = login_apigee()
    response = get_all_funds(headers)
    all_funds = json.dumps(response.json(), indent=4, sort_keys=True, ensure_ascii=False)
    all_funds = json.loads(all_funds)
    conn = _get_hg_connection('syc')
    for fund in all_funds['results']:
        response_by_id = get_fund_by_id(headers, fund['id'])
        response_by_id = json.dumps(response_by_id.json(), indent=4, sort_keys=True, ensure_ascii=False)
        response_by_id = json.loads(response_by_id)
        fund['precio_cp'] = response_by_id['currentShareValue']
        fund['status_precio'] = response_by_id['status']
        fund['fecha_valuacion'] = response_by_id['valueDate']
        try:
            fund['codigo_fci'] = get_codigo_fci(conn, str(fund['id']))['CODIGO']
            fund['name'] = get_codigo_fci(conn, str(fund['id']))['fci']
        except TypeError:
            fund['codigo_fci'] = None
            fund['name'] = None


    #pretty print all_funds
    all_funds_results = json.dumps(all_funds['results'], indent=4, sort_keys=True, ensure_ascii=False)
    print(all_funds_results)
    all_funds_results = json.loads(all_funds_results)
    with open('/tmp/qry_precio_cp.json', 'w') as f:
        json.dump(all_funds_results, f)

    bpm = redflagbpm.BPMService()
    _responseHeaders = bpm.context.json._responseHeaders
    _responseHeaders["status"] = "200"
    _responseHeaders["Content-Type"] = "application/json"
    _responseHeaders["Content-Encoding"] = "UTF-8"
    _responseHeaders["resource"] = "/tmp/qry_precio_cp.json"

if __name__ == '__main__':
    main()
