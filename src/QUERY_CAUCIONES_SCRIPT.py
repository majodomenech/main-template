#!python3
import json
import pandas as pd
import redflagbpm
from redflagbpm import PgUtils
import psycopg2
import psycopg2.extras
import tempfile
import os

def _get_connection():
    bpm = redflagbpm.BPMService()
    # Manual connection, no config file
    conn = PgUtils.get_connection(bpm, 'FLW')
    conn.autocommit = True
    return conn


def crear_dataframe(conn):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    sql = """    
            select *
    from colocadoras_fci.cauciones
    order by fondo
      """

    cur.execute(sql, )
    qry = cur.fetchall()
    cur.close()
    conn.close()
    return pd.DataFrame(qry)

def main():
    bpm = redflagbpm.BPMService()
    conn = _get_connection()
    df = crear_dataframe(conn)
    data = df.to_dict(orient='records')

    fd, temp_path = tempfile.mkstemp(suffix='.json')
    with os.fdopen(fd, 'w',encoding='utf-8') as temp_file:
        json.dump(data, temp_file, ensure_ascii=False, indent=4)
    #with open('/tmp/qry_menu.json', 'w', encoding='utf-8') as f:
    #    json.dump(data, f, ensure_ascii=False, indent=4)

    _responseHeaders = bpm.context.json._responseHeaders
    _responseHeaders["status"] = "200"
    _responseHeaders["Content-Type"] = "application/json"
    _responseHeaders["Content-Encoding"] = "UTF-8"
#    _responseHeaders["resource"] = "/tmp/qry_menu.json"
    _responseHeaders["resource"] = temp_path
#>>>>>>>
if __name__ == '__main__':
    main()
