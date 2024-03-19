#!python3
import json
import re
import urllib
from datetime import date, timedelta

import pandas as pd
import redflagbpm
from decimal import Decimal
from UTILS import call_json_endpoint, _get_connection, call_endpoint_gara, get_comit_responsable_nd_team, \
    get_esp_representacion, get_operador_hg
import psycopg2
import psycopg2.extras

def qry_todos(conn):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    sql = """    
            select *
    from menu.menu
      """

    cur.execute(sql, )
    qry = cur.fetchall()
    cur.close()
    conn.close()
    return pd.DataFrame(qry)

def qry_usuario(conn):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    sql = """ with usuario as (
select *
from menu.menu
where nombre = %s)

select 'lunes' as dia, lunes
from usuario
union all
select 'martes' as dia, martes
from usuario
union all
select 'miercoles' as dia, miercoles
from usuario
union all
select 'jueves' as dia, jueves
from usuario
union all
select 'viernes' as dia, viernes
from usuario

        """

    cur.execute(sql,(nombre,))
    qry = cur.fetchall()
    cur.close()
    conn.close()
    return pd.DataFrame(qry)

def main():
    bpm = redflagbpm.BPMService()
    tipo = bpm.context['tipo']

    if tipo == 'Usuario':
        conn = _get_connection(bpm)
        df = qry_usuario(conn)
    else:
        conn = _get_connection(bpm)
        df = qry_todos(conn)

    data = df.to_dict(orient='records')

    with open('/tmp/qry_menu.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    _responseHeaders = bpm.context.json._responseHeaders
    _responseHeaders["status"] = "200"
    _responseHeaders["Content-Type"] = "application/json"
    _responseHeaders["Content-Encoding"] = "UTF-8"
    _responseHeaders["resource"] = "/tmp/qry_menu.json"

if __name__ == '__main__':
    main()
