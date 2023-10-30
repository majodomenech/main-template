#!python3
import redflagbpm
import json
from DB_connect import _get_flw_connection
from auxiliar import procesar_respuesta
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


def suscripcion_simulacion_ingreso(headers, selection):
    data = selection
    alta_ingresar_status_list = []
    error_list = []
    id_suscri_list = []
    for susi in data:
        suscr = {
            # "fundId": susi["codigo_fci"], #no funciona el ID de CV
            "fundId": 130,
            "type": "amount",
            "value": susi["cantidad"],
            "investmentAccount": susi["cuenta_id"],
            "paymentMethod": {
                "type": "ACCOUNT",
                # "UBK": susi['cbu']
                "UBK": "0720112320000001419672"}, #no funciona el CBU asociado al ID de CV
            "externalReference": susi['idOrigen']
        }

        resp_alta = save_suscription(headers, suscr)
        print(resp_alta.json())
        # chequeo el estado del response
        resp_alta_ok, mje = procesar_respuesta(resp_alta, error_list, None, 'Suscripcion: Alta')
        db = "flowabletest"
        # conecto a la DB
        conn = _get_flw_connection(db)
        # con el id del response del endpoint de alta llamo al endpoint de ingresar
        if resp_alta_ok:
            id_suscri_list.append(resp_alta.json()['transactionId'])
            log_suscripcion(conn, id_origen=susi['idOrigen'], mensaje=resp_alta.json()['status'],
                            id_suscri=resp_alta.json()['transactionId'], estado=resp_alta.json()['status'],
                            descripción=resp_alta.text)

            # para suscris dadas de alta llamo al endpoint de ingresar
            resp_ingresar = confirm_suscription(resp_alta.json()['transactionId'])
            resp_ingresar.json()
            # chequeo el estado del ingrso
            resp_ingresar_ok, msj = procesar_respuesta(resp_ingresar, error_list, suscr, 'Suscripcion: Ingresar')
            rta = f"Suscripción {susi['idOrigen']} dada de alta"
            alta_ingresar_status_list.append(rta)
            print('RESP CONFIRMAR \n', resp_ingresar)
            if resp_ingresar_ok:
                rta = f"Suscripción {susi['idOrigen']} ingresada"
                # si el response no arroja errores impacto en la tabla FCISTDR.suscripcion_status
                log_suscripcion(conn, id_origen=susi['idOrigen'], mensaje='Ingresado',
                                id_suscri=resp_alta.json()['id'], descripción=resp_ingresar.text)
                alta_ingresar_status_list.append(rta)
            else:
                rta = f"{susi['idOrigen']}:{msj}"
                alta_ingresar_status_list.append(rta)
                log_suscripcion(conn, id_origen=susi['idOrigen'], mensaje=msj,
                                id_suscri=resp_alta.json()['id'], estado='NO INGRESADO',
                                descripción=resp_ingresar.text)
        else:
            # si el response de alta arroja errores impacto en la tabla FCISTDR.suscripciones_status
            rta = f"{susi['idOrigen']}:{mje}"
            alta_ingresar_status_list.append(rta)
            log_suscripcion(conn, id_origen=susi['idOrigen'], mensaje=mje)

    html="""<div align="left">Resultado: <ul>"""
    for x in alta_ingresar_status_list:
        html += "<li>"+x+"</li>"
    html += "</ul></div>"
    return html, id_suscri_list

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    #Uso la selección del usuario (ve el listado de suscris de HG)
    selection = bpm.context['selection']
    selection = json.loads(selection)
    headers = login_apigee()
    html, id_suscri_list = suscripcion_simulacion_ingreso(headers, selection)
    bpm.reply(html)
