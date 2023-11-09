#!python3
import redflagbpm
import json
from DB_connect import _get_flw_connection
from auxiliar import procesar_respuesta
from key_n_account_data import get_account_data
# from codigo_emisor import get_codigo_emisor_byma_cuit
# from endpoints_fci_byma import alta_bilateral_suscripcion, ingresar_bilateral_suscripcion

from endpoints_santander import save_suscription, confirm_suscription, login_apigee
from write_DB import log_suscripcion
import logging
import http.client as http_client
http_client.HTTPConnection.debuglevel = 1
#initialize logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def suscripcion_simulacion_ingreso(headers, bpm, selection):
    data = selection
    alta_ingresar_status_list = []
    error_list = []
    id_suscri_list = []
    if bpm.service.text("STAGE") == 'DEV':
        db = "flowabletest"
    else:
        db = "flowable"
    conn = _get_flw_connection(db)
    investmentAccount = get_account_data()['investmentAccount']
    UBK = get_account_data()['UBK']
    # print(get_account_data())
    for susi in data:
        #suscripción por monto
        suscr = {
            "fundId": susi["fund_id"],
            "type": "amount",
            "value": susi["cantidad"],
            "investmentAccount": investmentAccount,
            "paymentMethod": {
                "type": "ACCOUNT",
                "UBK": UBK
            }, #no funciona el CBU asociado al ID de CV
            "externalReference": susi['idOrigen']
        }
        # Dar alta la suscri (simular)
        resp_alta = save_suscription(headers, suscr)
        print(3*f'ALTA\n', resp_alta.json())
        # chequeo el estado del response
        resp_alta_ok, mje = procesar_respuesta(resp_alta, error_list, None, 'Suscripcion: Alta')

        # con el id del response del endpoint de alta llamo al endpoint de ingresar
        if resp_alta_ok:
            id_suscri_list.append(resp_alta.json()['transactionId'])
            log_suscripcion(conn, id_origen=susi['idOrigen'], mensaje=resp_alta.json()['status'],
                            id_suscri=resp_alta.json()['transactionId'], certificate_id=resp_alta.json()['certificateId'],
                            estado=resp_alta.json()['status'], monto = susi['cantidad'],
                            descripción=resp_alta.text, usr_message="Ingresado")
            # break
            # para suscris dadas de alta llamo al endpoint de ingresar
            resp_confirmar = confirm_suscription(headers, resp_alta.json()['transactionId'])
            print(3*'CONFIRMACIÓN\n', resp_confirmar.json())
            # chequeo el estado del ingrso
            resp_confirmar_ok, msj = procesar_respuesta(resp_confirmar, error_list, suscr, 'Suscripcion: Ingresar')
            rta = f"Suscripción {susi['idOrigen']} dada de alta"
            alta_ingresar_status_list.append(rta)
            # print('RESP CONFIRMAR \n', resp_confirmar)
            if resp_confirmar_ok:
                rta = f"Suscripción {susi['idOrigen']} ingresada"
                # si el response no arroja errores impacto en la tabla FCISTDR.suscripcion_status
                log_suscripcion(conn, id_origen=susi['idOrigen'], mensaje='Ingresado',
                                id_suscri=resp_alta.json()['transactionId'], certificate_id=resp_confirmar.json()['certificateId'],
                                estado=resp_confirmar.json()['status'],
                                descripción=resp_confirmar.text, usr_message=resp_confirmar.json()['status'])
                alta_ingresar_status_list.append(rta)
            else:
                rta = f"{susi['idOrigen']}:{msj}"
                alta_ingresar_status_list.append(rta)
                log_suscripcion(conn, id_origen=susi['idOrigen'], mensaje=msj,
                                id_suscri=resp_alta.json()['transactionId'],
                                # certificate_id=resp_confirmar.json()['certificateId'],
                                estado='NO CONFIRMADO',
                                descripción=resp_confirmar.text, usr_message=msj)
        else:
            # si el response de alta arroja errores impacto en la tabla FCISTDR.suscripciones_status
            rta = f"{susi['idOrigen']}:{mje}"
            alta_ingresar_status_list.append(rta)
            log_suscripcion(conn, id_origen=susi['idOrigen'], mensaje=mje, estado=f"ALTA ERROR",
                            usr_message=f"Alta Error: {mje}")

    html="""<div align="left">Resultado: <ul>"""
    for x in alta_ingresar_status_list:
        html += "<li>"+x+"</li>"
    html += "</ul></div>"
    return html, id_suscri_list

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    #Uso la selección del usuario (ve el listado de suscris de HG)

    selection = bpm.context['selection']
    try:
        selection = json.loads(selection)
    except Exception:
        pass

    headers = login_apigee()
    html, id_suscri_list = suscripcion_simulacion_ingreso(headers, bpm, selection)
    bpm.reply(html)
