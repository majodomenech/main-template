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

def rescate_alta_ingreso(bpm, selection):
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
        max_ord = []
        resumen_orden = json.loads(reci['resumen_orden'])

        for acc in resumen_orden:
            for order in acc["origenes"]:
                max_ord.append(order["idOrden"])
        #get maximum value from max_ord and define a unique id_origen
        max_id_origen = max(max_ord)

        #calculo la fecha de liquidacion teniendo usando los días hábiles y el plazo de liquidación
        fecha_liquidacion = get_fecha_liquidacion(reci['plazo_liq'])

        resc_hg = {"emisor": {"codigo": get_codigo_emisor_byma_cuit(reci['cuit'])},
                "cantidadCuotaPartes": reci["cp_total"],
                "fechaLiquidacion": fecha_liquidacion,
                "especie": reci["codigo_fci"],
                'idOrigen': max_id_origen, 'precio': 0, 'monedaPago': 0, 'liquidaEnBYMA': False}

        #rescate por cuotapartes
        resc = {
                # "fundId": reci["codigo_fci"], #no funciona el ID de CV
                "fundId": 130,
                "type": "share",
                "value": reci["cp_total"],
                "investmentAccount": 41621350,
                "paymentMethod": {
                    "type": "ACCOUNT",
                    "UBK": "0720112320000001419672"
                },
                "externalReference": 484670111111111
            }
        # Dar alta del rescate
        resp_alta = save_redemption(headers, resc)
        print(resp_alta.json())
        # chequeo el estado del response
        resp_alta_ok, msj = procesar_respuesta(resp_alta, error_list, None, 'Rescate: Alta')


        if resp_alta_ok:
            # si el response no arroja errores impacto en la tabla fcimkt.rescates_status
            # un registro por cada comitente en el batch de rescates agrupados por fondo.
            # elijo la DB que contiene la tabla de status rescates
            for acc in resumen_orden:
                for order in acc["origenes"]:
                    rta= f"Rescate {order['idOrden']} dado de alta"
                    alta_ingresar_status_list.append(rta)
                    id_rescate_list.append(resp_alta.json()['id'])
                    log_rescate(conn, id_origen=order["idOrden"], mensaje=resp_alta.json()['estado'], id_grupo=max_id_origen,
                                id_rescate=resp_alta.json()['id'], estado=resp_alta.json()['estado'],
                                descripción=resp_alta.text)

                # ditribución de VN por cuenta
                comit = {"comitente": acc['cuenta'], "cantidad": acc['cantidad']}

                # llamo al endpoint de alta de comitentes usando únicamente los campos que soporta el endpoint
                resp_distribuir_comitentes = bilateral_rescate_alta_comitente(resp_alta.json()['id'],
                                                                              {"comitente": comit['comitente'],
                                                                               "cantidad": comit['cantidad']})
                # chequeo el estado del response de distribución de comitentes
                resp_distrib_comits_ok, msj = procesar_respuesta(resp_distribuir_comitentes, error_list,
                                                                 {"comitente": comit['comitente'],
                                                                  "cantidad": comit['cantidad']},
                                                                 'Rescate: distribuir comitentes')
                # si el response no arroja errores impacto en la tabla fcimkt.rescates_status
                # sino también impacto en la tabla fcimkt.rescates_status
                if resp_distrib_comits_ok:
                    for order in acc["origenes"]:
                        # rta = f"Rescate {order['idOrden']} dado de alta"
                        log_rescate(conn, id_origen=order["idOrden"],
                                    mensaje=resp_alta.json()['estado'] + ' - Comitentes asignados', id_grupo=max_id_origen,
                                    id_rescate=resp_alta.json()['id'],
                                    estado=resp_alta.json()['estado'] + ' - Comitentes asignados',
                                    descripción=resp_distribuir_comitentes.text)
                else:
                    for order in acc["origenes"]:
                        log_rescate(conn, id_origen=order["idOrden"], mensaje=msj, id_grupo=max_id_origen,
                                    id_rescate=resp_alta.json()['id'],
                                    estado=resp_alta.json()['estado'] + ' - Comitentes no asignados',
                                    descripción=resp_distribuir_comitentes.text)

            # Para cada rescate agrupado por fondo llamo al endpoint de ingresar
            resp_ingresar = ingresar_bilateral_rescate(resp_alta.json()['id'])
            # chequeo el estado del response de ingresar
            resp_ingresar_ok, msj = procesar_respuesta(resp_ingresar, error_list, resp_alta.json()['id'], 'Rescate: Ingresar')
            print('RESP INGRESAR: \n', resp_ingresar)
            # si el response no arroja errores impacto en la tabla fcimkt.rescates_status
            if resp_ingresar_ok:
                for acc in resumen_orden:
                    for order in acc["origenes"]:
                        rta = f"Rescate {order['idOrden']} ingresado"
                        log_rescate(conn, id_origen=order["idOrden"], mensaje='Ingresado', id_grupo=max_id_origen,
                                    id_rescate=resp_alta.json()['id'], estado='Ingresado', descripción=resp_ingresar.text)
                        alta_ingresar_status_list.append(rta)
            else:
                for acc in resumen_orden:
                    for order in acc["origenes"]:
                        rta = f"{order['idOrden']}:{msj}"
                        log_rescate(conn, id_origen=order["idOrden"], mensaje=msj, id_grupo=max_id_origen,
                                    id_rescate=resp_alta.json()['id'], estado='NO INGRESADO', descripción=resp_ingresar.text)
                        alta_ingresar_status_list.append(rta)
        else:
            # si el response de alta arroja errores impacto en la tabla fcimkt.rescates_status
            for acc in resumen_orden:
                for order in acc["origenes"]:
                    rta = f"{order['idOrden']}:{msj}"
                    alta_ingresar_status_list.append(rta)
                    log_rescate(conn, id_origen=order["idOrden"], mensaje=msj, id_grupo=max_id_origen)

    html="""<div align="left">Resultado: <ul>"""
    for x in alta_ingresar_status_list:
        html += "<li>"+x+"</li>"
    html += "</ul></div>"
    return html, id_rescate_list

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    #Uso la selección del usuario (ve el listado de suscris y rescates de BYMA)
    seleccionados = bpm.context['selection']
    print(80*'*', seleccionados)
    # data = json.dumps(seleccionados)
    html, id_rescate_list = rescate_alta_ingreso(bpm, seleccionados)
    bpm.reply(html)
