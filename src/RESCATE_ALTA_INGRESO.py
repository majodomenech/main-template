#!python3
import redflagbpm
import json
from DB_connect import _get_flw_connection
from auxiliar import get_fecha_liquidacion, procesar_respuesta, get_id_from_codigo_cv
from codigo_emisor import get_codigo_emisor_byma_cuit
from endpoints_santander import login_apigee, save_redemption, confirm_redemption
from write_DB import log_rescate
from key_n_account_data import get_account_data
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
    acc_data = get_account_data()
    investmentAccount =  acc_data['investmentAccount']
    UBK = acc_data['UBK']
    for reci in data:
        print(reci)
        #calculo la fecha de liquidacion teniendo usando los días hábiles y el plazo de liquidación
        fecha_liquidacion = get_fecha_liquidacion(reci['plazo_liq'])
        # fundId = get_id_from_codigo_cv(headers, reci['codigo_fci'])
        # print(fundId)
        #rescate por cuotapartes
        resc = {
                    "fundId": reci['fund_id'],
                    "type": "share",
                    "value": reci['cantidad_cuotapartes'],
                    "investmentAccount": investmentAccount,
                    "paymentMethod": {
                        "type": "account",
                        "UBK": UBK
                    },
                    "externalReference": reci['idOrigen']
                }

        # Dar alta del rescate
        resp_alta = save_redemption(headers, resc)
        print(3*'ALTA\n', resp_alta.json())
        # chequeo el estado del response
        resp_alta_ok, msj = procesar_respuesta(resp_alta, error_list, None, 'Rescate: Alta')
        # con el id del response del endpoint de alta llamo al endpoint de ingresar
        if resp_alta_ok:
            id_rescate_list.append(resp_alta.json()['transactionId'])
            log_rescate(conn, id_origen=reci['idOrigen'], mensaje=resp_alta.json()['status'],
                                id_rescate=resp_alta.json()['transactionId'], certificate_id=resp_alta.json()['certificateId'],
                                estado=resp_alta.json()['status'],
                                descripción=resp_alta.text)

            # Para cada rescate  llamo al endpoint de confirmar
            resp_confirmar = confirm_redemption(headers, resp_alta.json()['transactionId'])
            print('RESP CONFIRMAR: \n', resp_confirmar.json())
            # chequeo el estado del response de confirmar
            resp_confirmar_ok, msj = procesar_respuesta(resp_confirmar, error_list, resp_alta.json()['transactionId'], 'Rescate: Ingresar')

            # si el response no arroja errores impacto en la tabla fcistdr.rescates_status
            if resp_confirmar_ok:
                rta = f"Rescate {reci['idOrigen']} ingresado"
                log_rescate(conn, id_origen=reci['idOrigen'], mensaje='Ingresado',
                            id_rescate=resp_alta.json()['transactionId'], estado=resp_alta.json()['status'],
                            certificate_id=resp_alta.json()['certificateId'],
                            descripción=resp_confirmar.text)
                alta_ingresar_status_list.append(rta)
            else:
                rta = f"{reci['idOrigen']}:{msj}"
                log_rescate(conn, id_origen=reci['idOrigen'], mensaje=msj,
                            id_rescate=resp_alta.json()['transactionId'], certificate_id=resp_alta.json()['certificateId'],
                            estado='NO INGRESADO', descripción=resp_confirmar.text)
                alta_ingresar_status_list.append(rta)
        else:
            # si el response de alta arroja errores impacto en la tabla fcistdr.rescates_status
            rta = f"{reci['idOrigen']}:{msj}"
            alta_ingresar_status_list.append(rta)
            log_rescate(conn, id_origen=reci['idOrigen'], mensaje=msj)

    html="""<div align="left">Resultado: <ul>"""
    for x in alta_ingresar_status_list:
        html += "<li>"+x+"</li>"
    html += "</ul></div>"
    return html, id_rescate_list

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    #Uso la selección del usuario (ve el listado de suscris y rescates de BYMA)

    selection = bpm.context['selection']
    try:
        selection = json.loads(selection)
    except Exception:
        pass

    print(80 * '\../ ', selection)
    headers = login_apigee()
    html, id_rescate_list = rescate_simulacion_ingreso(headers, bpm, selection)
    bpm.reply(html)
