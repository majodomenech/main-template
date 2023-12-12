#!python3
import requests
import json
import redflagbpm
import re
import psycopg2, psycopg2.extras

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

    return data['fecha'], data['vcpUnitario']

def get_cotizacion_provisoria(conn, id_fondo):
    sql = """
        select cotizacion from ds.fondos where id_fondo = %s
    """

    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql, (id_fondo,))
    cotizacion = cur.fetchone()['cotizacion']
    cur.close()
    return cotizacion


if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    # id_fondo = bpm.context['id_fondo']
    id_fondo = '14410'

    conn = _get_hg_connection('syc')
    # Busco el simbolo local en DB HG usando el codigo CV
    simbolo_local = get_fci_simbolo_local(conn, id_fondo)
    # extraigo el codigo de fci y clase
    matches = re.search(r'CAFCI(\d+)-(\d+)', simbolo_local)
    fci = matches.group(1)
    clase = matches.group(2)
    # obtengo la cotizacion de la API de CAFCI
    fecha, vcp = get_cotizacion_cafci(fci, clase)
    # agrego manualmente hora a la fecha en formato dd/MM/yyyy HH:mm:ss
    fecha = fecha + ' 23:59:59'

    if bpm.service.text("STAGE") == 'DEV':
        conn = _get_flw_connection('flowabletest')
    else:
        conn = _get_flw_connection('flowable')

    fecha, precio_cp = get_cotizacion_provisoria(conn, id_fondo)
    print(fecha)
