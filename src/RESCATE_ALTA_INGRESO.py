#!python3
import redflagbpm
import json
from DB_connect import _get_flw_connection
from auxiliar import get_fecha_liquidacion, procesar_respuesta
from codigo_emisor import get_codigo_emisor_byma_cuit
from endpoints_santander import login_apigee, save_redemption, confirm_redemption
from write_DB import log_rescate
import logging
import http.client as http_client
http_client.HTTPConnection.debuglevel = 1
#initialize logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

def rescate_simulacion_ingreso(headers, bpm, selection):
    data = selection
    alta_ingresar_status_list = []
    error_list = []
    id_rescate_list = []
    if bpm.service.text("STAGE") == 'DEV':
        db = "flowabletest"
    else:
        db = "flowable"
    conn = _get_flw_connection(db)
    for reci in data:
        #calculo la fecha de liquidacion teniendo usando los días hábiles y el plazo de liquidación
        fecha_liquidacion = get_fecha_liquidacion(reci['plazo_liq'])

        resc = {
                    # "fundId": reci["codigo_fci"], #no funciona el ID de CV
                    "fundId": 130,
                    "type": "share",
                    "value": reci['cantidad_cuotapartes'],
                    "investmentAccount": reci['cuenta_id'],
                    "paymentMethod": {
                        "type": "ACCOUNT",
                        # "UBK": reci['cbu'],
                        "UBK": "0720112320000001419672"
                    },
                    "externalReference": reci['idOrigen']
                }

        # Dar alta del rescate
        resp_alta = save_redemption(headers, resc)
        print(resp_alta.json())
        # chequeo el estado del response
        resp_alta_ok, msj = procesar_respuesta(resp_alta, error_list, None, 'Rescate: Alta')
        if resp_alta_ok:
            id_rescate_list.append(resp_alta.json()['transactionId'])
            log_rescate(conn, id_origen=resc['idOrigen'], mensaje=resp_alta.json()['status'],
                                id_rescate=resp_alta.json()['transactionId'], estado=resp_alta.json()['status'],
                                descripción=resp_alta.text)

            # Para cada rescate  llamo al endpoint de confirmar
            resp_confirmar = confirm_redemption(headers, resp_alta.json()['transactionId'])
            print('RESP CONFIRMAR: \n', resp_confirmar.json())
            # chequeo el estado del response de confirmar
            resp_confirmar_ok, msj = procesar_respuesta(resp_confirmar, error_list, resp_alta.json()['transactionId'], 'Rescate: Ingresar')

            # si el response no arroja errores impacto en la tabla fcistdr.rescates_status
            if resp_confirmar_ok:
                rta = f"Rescate {order['idOrden']} ingresado"
                log_rescate(conn, id_origen=resc['idOrigen'], mensaje='Ingresado',
                            id_rescate=resp_alta.json()['transactionId'], estado='Ingresado', descripción=resp_confirmar.text)
                alta_ingresar_status_list.append(rta)
            else:
                rta = f"{resc['idOrigen']}:{msj}"
                log_rescate(conn, id_origen=resc['idOrigen'], mensaje=msj,
                            id_rescate=resp_alta.json()['transactionId'], estado='NO INGRESADO', descripción=resp_confirmar.text)
                alta_ingresar_status_list.append(rta)
        else:
            # si el response de alta arroja errores impacto en la tabla fcistdr.rescates_status
            rta = f"{resc['idOrigen']}:{msj}"
            alta_ingresar_status_list.append(rta)
            log_rescate(conn, id_origen=resc['idOrigen'], mensaje=msj)

    html="""<div align="left">Resultado: <ul>"""
    for x in alta_ingresar_status_list:
        html += "<li>"+x+"</li>"
    html += "</ul></div>"
    return html, id_rescate_list

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    #Uso la selección del usuario (ve el listado de suscris y rescates de BYMA)
    selection = bpm.context['selection']
    print(80*'\../ ', selection)
    selection = json.loads(selection)
    headers = login_apigee()
    html, id_rescate_list = rescate_simulacion_ingreso(headers, bpm, selection)
    bpm.reply(html)
