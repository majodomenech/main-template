#!python3
import redflagbpm
import psycopg2, psycopg2.extras
import requests
import datetime
import urllib.parse





# def get_cotizacion_from_hg(bpm, id_fondo):
#     #get todays date in the format: dd/mm/yyyy
#     #url encode date
#     today = urllib.parse.quote(datetime.date.today().strftime("%d/%m/%Y"))
#     url_base = 'https://ws.sycinversiones.com'
#     url = f'{url_base}/precios?fecha={today}&titulos={id_fondo}'
#     TOKEN =bpm.service.text("TOKEN_WS")
#     headers = {
#         'Authorization': 'Bearer '+TOKEN,
#         'Content-Type': 'application/json'
#     }
#     response = requests.get(url, headers=headers)
#     return response

# def get_cotizacion(conn, id_fondo):
#
#
#     sql = """
#         select cotizacion from ds.fondos where id_fondo = %s
#     """
#
#     cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
#     cur.execute(sql, (id_fondo,))
#     cotizacion = cur.fetchone()['cotizacion']
#     cur.close()

    # return cotizacion

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()

    id_fondo = bpm.context['id_fondo']

    if bpm.service.text("STAGE") == 'DEV':
        conn = _get_flw_connection('flowabletest')
    else:
        conn = _get_flw_connection('flowable')

    # todo implementar la lectura de cotizaciones de un endpoint
    # todo :quedarme con la cotización más reciente
    cotizacion_hg = get_cotizacion_from_hg(bpm, id_fondo)
    cotizacion_hg = cotizacion_hg.json()[0]['precio']

    #todo : implementar la lectura de cotizaciones de una colección

    # cotizacion = get_cotizacion(conn, id_fondo)

    cantidad_importe = bpm.context['cantidad_importe']
