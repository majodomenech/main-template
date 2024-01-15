#!python3
import requests
import json
import psycopg2, psycopg2.extras
from auxiliar import formatear
import re

def get_cotizacion_hg(bpm, codigo_fci, fecha):
    url = "https://ws.sycinversiones.com/precios"
    TOKEN = bpm.service.text("TOKEN_WS")
    headers = {
        'Accept': 'application/json',
        "Authorization": "Bearer "+TOKEN
    }
    params = {
        "fecha": fecha,
        "titulos": codigo_fci
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        json_data = response.json()
        # Process the JSON data as needed
        print(json_data)
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
    return json_data

def get_cotizacion_cafci(fci_id, class_id):
    #quinquela pesos clase B: ejemplo
    #https://api.cafci.org.ar/fondo/593/clase/1201/ficha
    url_base = "https://api.cafci.org.ar/fondo"
    url = f"{url_base}/{fci_id}/clase/{class_id}/ficha"

    headers = {
        'Accept': 'application/json, text/plain, */*'
    }
    try:
        response = requests.get(url, headers=headers, timeout=5)
        data = json.loads(response.content)['data']['info']['diaria']['actual']
    except:
        data = None
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

    with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        cur.execute(sql, (id_fondo,))
        qry = cur.fetchone()
        if qry is not None:
            qry['fecha_cotizacion_manual'] = formatear(float(qry['fecha_cotizacion_manual']))
        return qry


