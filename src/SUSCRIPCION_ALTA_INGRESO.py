#!python3
import redflagbpm
import json
from DB_connect import _get_flw_connection
from auxiliar import procesar_respuesta
from codigo_emisor import get_codigo_emisor_byma_cuit
from endpoints_fci_byma import alta_bilateral_suscripcion, ingresar_bilateral_suscripcion

from endpoints_santander import save_suscription, confirm_suscription
from write_DB import log_suscripcion

def suscripcion_simulacion_ingreso(bpm, seleccionados):
    data = seleccionados
    alta_ingresar_status_list = []
    error_list = []
    id_suscri_list = []
    for susi in data:
        suscr = {
            "fundId": susi["codigo_fci"],
            "type": "amount",
            "value": susi["cantidad"],
            "investmentAccount": susi["cuenta_id"],
            "paymentMethod": {
                "type": "ACCOUNT",
                "UBK": "0720112320000001419672"
            },
            "externalReference": susi['idOrigen']
        }
        # suscr = {"emisor": {"codigo": get_codigo_emisor_byma_cuit(susi['cuit'])},
        #          "cantidadCuotaPartes": susi["cantidad_cuotapartes"],
        #          "especie": susi["codigo_fci"], 'idOrigen': susi["idOrigen"]}
        # Simular suscripción APIC
        resp_alta = save_suscription(suscr)
        print(resp_alta.json())
        # chequeo el estado del response
        resp_alta_ok, mje = procesar_respuesta(resp_alta, error_list, None, 'Suscripcion: Alta')
        db = "flowabletest"
        # conecto a la DB
        conn = _get_flw_connection(db)
        # con el id del response del endpoint de alta llamo al endpoint de ingresar
        if resp_alta_ok:
            id_suscri_list.append(resp_alta.json()['id'])
            log_suscripcion(conn, id_origen=susi['idOrigen'], mensaje=resp_alta.json()['estado'],
                            id_suscri=resp_alta.json()['id'], estado=resp_alta.json()['estado'],
                            descripción=resp_alta.text)

            # para suscris dadas de alta llamo al endpoint de ingresar
            resp_ingresar = confirm_suscription(resp_alta.json()['id'])
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
    seleccionados = bpm.context['selection']
    html, id_suscri_list = suscripcion_simulacion_ingreso(bpm, seleccionados)
    bpm.reply(html)
