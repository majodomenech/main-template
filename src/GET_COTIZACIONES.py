#!python3
import requests
import json
import redflagbpm
import re
import psycopg2, psycopg2.extras
from auxiliar import formatear

def _get_hg_connection(DB):
    #Manual connection, no config file
    conn = psycopg2.connect(database=DB,
                        user="consyc",
                        password="MTU1NDNjN2ZlZGU4ZDdhNDBhZTM2MjA2",
                        host="db.sycinversiones.com",
                        port="5432")
    conn.autocommit = True
    return conn

def _get_flw_connection(DB):
    #Manual connection, no config file
    conn = psycopg2.connect(database=DB,
                            user="flowable",
                            password="flowable",
                            host="db.sycinversiones.com",
                            port="5432")
    conn.autocommit = True
    return conn

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
    qry['fecha_cotizacion_manual'] = formatear(float(qry['fecha_cotizacion_manual']))
    cur.close()
    return qry


if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    # id_fondo = bpm.context['id_fondo']
    id_fondo = '14410'


    conn = _get_hg_connection('syc')

    #BUSCO COTIZACION CAFCI#####
    # Busco el simbolo local en DB HG usando el codigo CV
    simbolo_local = get_fci_simbolo_local(conn, id_fondo)
    # extraigo el codigo de fci y clase
    matches = re.search(r'CAFCI(\d+)-(\d+)', simbolo_local)
    fci = matches.group(1)
    clase = matches.group(2)
    # obtengo la cotizacion de la API de CAFCI
    cafci_dict = dict(get_cotizacion_cafci(fci, clase))

    # agrego manualmente hora a la fecha en formato dd/MM/yyyy HH:mm:ss
    cafci_dict['fecha_cotizacion'] = cafci_dict['fecha'] + ' 23:59:59'
    print('CAFCI: \n', cafci_dict)
    ##########################

    ###BUSCO COTIZACION MANUAL#####
    if bpm.service.text("STAGE") == 'DEV':
        conn = _get_flw_connection('flowabletest')
    else:
        conn = _get_flw_connection('flowable')
    #read from get_cotizacion_provisoria and recover values
    manual_cotiz = get_cotizacion_provisoria(conn, id_fondo)
    print('COTIZ MANUALES: \n', manual_cotiz)

    cotiz_dict = {}
    if manual_cotiz['fecha_cotizacion_manual'] > cafci_dict['fecha_cotizacion']:
       cotiz_dict['fecha_cotizacion'] = manual_cotiz['fecha_cotizacion_manual']
       cotiz_dict['precio'] = manual_cotiz['vcp_provisorio']
    else:
       cotiz_dict['fecha_cotizacion'] = cafci_dict['fecha_cotizacion']
       cotiz_dict['precio'] = cafci_dict['vcpUnitario']

    print(cotiz_dict)





