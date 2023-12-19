#!python3
import requests
import json
import psycopg2, psycopg2.extras
from auxiliar import formatear
import re

def get_cotizacion_cafci(fci_id, class_id):
    url_base = "https://api.cafci.org.ar/fondo"
    url = f"{url_base}/{fci_id}/clase/{class_id}/ficha"
    headers = {
        'Accept': 'application/json, text/plain, */*'
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.content)['data']['info']['diaria']['actual']
    return data

def get_cotizacion_provisoria(conn, id_fondo):
    sql = """
        with cp_collection as (
            select 
                SUBSTRING(id FROM POSITION('[' IN id) + 1 FOR POSITION(']' IN id) - POSITION('[' IN id) - 1) AS fondo_id,
                body#>>'{precio_cp_provisorio}' as vcp_provisorio,
                (body#>>'{fecha_cotizacion}')::bigint as fecha_cotizacion_manual
            from document.document
            where collection like 'INSTFCI/COLLECTION_PRECIOS_CP_PROVISORIOS'
        )
        select * 
        from cp_collection
        where fondo_id = %s
    """

    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql, (id_fondo,))
    qry = cur.fetchone()
    if qry is not None:
        qry['fecha_cotizacion_manual'] = formatear(float(qry['fecha_cotizacion_manual']))
    cur.close()
    return qry

def get_fci_simbolo_local(conn, id_fondo):
    sql = """
      select uu."SIMBOLOLOCAL" as simbolo_local
      from "UNI_UNIDAD" uu
        inner join "UNI_TIPO_TITULO" utt on uu."TIPOTITULO" = utt."UNI_TIPO_TITULO_ID"
      where uu."CLASS" like '%%UFondoComunInversion'
      and uu."CODIGO" like %s
    """
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql, (id_fondo,))
    qry = cur.fetchone()

    cur.close()
    conn.close()
    matches = re.search(r'(\d+)-(\d+)', qry["simbolo_local"])
    cafci_id = matches.group(1)
    clase_id = matches.group(2)
    return cafci_id, clase_id
