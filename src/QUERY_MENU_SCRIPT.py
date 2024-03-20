#!python3
import json
import pandas as pd
import redflagbpm
from redflagbpm import PgUtils
import psycopg2
import psycopg2.extras


def _get_connection():
    bpm = redflagbpm.BPMService()
    # Manual connection, no config file
    conn = PgUtils.get_connection(bpm, 'FLW')
    conn.autocommit = True
    return conn


def qry_todos(conn):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    sql = """    
            select *, null as template
    from menu.menu
      """

    cur.execute(sql, )
    qry = cur.fetchall()
    cur.close()
    conn.close()
    return pd.DataFrame(qry)


def qry_usuario(conn, nombre):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    sql = """ with usuario as (
select *
from menu.menu
where nombre = %s)

select 'lunes' as dia, lunes as menu, null as template
from usuario
union all
select 'martes' as dia, martes as menu, null as template
from usuario
union all
select 'miercoles' as dia, miercoles as menu, null as template
from usuario
union all
select 'jueves' as dia, jueves as menu, null as template
from usuario
union all
select 'viernes' as dia, viernes as menu, null as template
from usuario

        """

    cur.execute(sql, (nombre,))
    qry = cur.fetchall()
    cur.close()
    conn.close()
    return pd.DataFrame(qry)

def crear_dataframe(tipo, usuario):
    if tipo == 'Usuario':
        conn = _get_connection()
        df = qry_usuario(conn, usuario)
    else:
        conn = _get_connection()
        df = qry_todos(conn)
    df['tipo'] = tipo
    df['usuario'] = usuario
    return df

def main():
    bpm = redflagbpm.BPMService()
    tipo = bpm.context['tipo']
    try:
        nombre = bpm.context['usuario']
    except:
        nombre = bpm.context['userId']

    df = crear_dataframe(tipo, nombre)
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
