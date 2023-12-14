#!python3
import asyncio
import json
import requests_async as requests
# import requests
import json
import redflagbpm
import re
import psycopg2, psycopg2.extras
from auxiliar import formatear
from DB import _get_hg_connection, _get_flw_connection
import time

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
    return qry["simbolo_local"]

async def get_cotizacion_cafci(fci_id, class_id):
    url_base = "https://api.cafci.org.ar/fondo"
    url = f"{url_base}/{fci_id}/clase/{class_id}/ficha"
    headers = {
        'Accept': 'application/json, text/plain, */*'
    }
    response = await requests.get(url, headers=headers)
    data = json.loads(response.content)['data']['info']['diaria']['actual']

    return data

async def get_cotizacion_provisoria(conn, id_fondo):
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
    qry['fecha_cotizacion_manual'] = formatear(float(qry['fecha_cotizacion_manual']))
    cur.close()
    return qry

async def get_cotizaciones_1(fci_id, class_id):
    print("Antes de CAFCI")
    cotizacion = await get_cotizacion_cafci(fci_id=fci_id, class_id=class_id)
    print("Después de CAFCI")
    return cotizacion

async def get_cotizaciones_2(conn, id_fondo):
    print("Antes de PROVISORIA")
    cotizacion = await get_cotizacion_provisoria(conn=conn, id_fondo=id_fondo)
    print("Después de PROVISORIA")
    return cotizacion

async def main(fci, clase, id_fondo):
    bpm = redflagbpm.BPMService()
    if bpm.service.text("STAGE") == 'DEV':
        conn = _get_flw_connection('flowabletest')
    else:
        conn = _get_flw_connection('flowable')
    res = await asyncio.gather(get_cotizaciones_1(fci, clase), get_cotizaciones_2(conn, id_fondo))
    return res


if __name__ == '__main__':
    start = time.perf_counter()
    conn = _get_hg_connection('syc')
    id_fondo = '14410'
    # Busco el simbolo local en DB HG usando el codigo CV
    simbolo_local = get_fci_simbolo_local(conn, id_fondo)
    # extraigo el codigo de fci y clase
    matches = re.search(r'CAFCI(\d+)-(\d+)', simbolo_local)
    fci = matches.group(1)
    clase = matches.group(2)
    args = [fci, clase, id_fondo]

    cafci, provisoria = asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")