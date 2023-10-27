#!python3
import json
from DB_connect import _get_flw_connection
from endpoints_santander import find_subscriptions, get_subscription, get_redemption, search_redemption
import datetime
from auxiliar import get_b_day
from write_DB import update_rescate_status, update_suscripcion_status, update_suscripciones_eliminadas, update_rescates_eliminados
import redflagbpm

#today in format YYYY-MM-DD
today = datetime.date.today().strftime("%Y-%m-%d")
fecha_alta_hasta = today
#get last business day given a time laps as parameter:
# for example 20 business days ago
last_business_days = get_b_day(fecha_alta_hasta, 1)
db = "flowabletest"
# conecto a la DB
conn = _get_flw_connection(db)
##########################################################################################
############################### RECUPERAR LAS SUSCRIS DE STDR ##############################
##########################################################################################

#listar todas las suscris confiltro de fecha de alta
resp = find_subscriptions()
print(resp.text)


for suscripcion in resp.json()['items']:
    print(suscripcion)
    # #string estado to upper case
    # estado = suscripcion['estado'].upper()
    # nro_pedido = suscripcion['numeroPedido'] if 'numeroPedido' in suscripcion.keys() else None
    # id_origen = suscripcion['idOrigen']
    # fecha_alta = suscripcion['fechaAlta']
    #
    # especie = suscripcion['especie']
    # cantidad_cp = suscripcion["cantidadCuotaPartes"]
    #
    # resp_x_id = bilateral_suscripcion_listar_x_id(suscripcion['id'])
    # update_suscripcion_status(conn, id_origen, mensaje='Sincronizado con STDR ' + estado, estado=estado,
    #                       nro_pedido=nro_pedido, fecha_alta=fecha_alta, especie=especie, cantidad_cp=cantidad_cp, id_suscri = suscripcion['id'])
    # print(resp_x_id.json())

##########################################################################################
############################### RECUPERAR LOS RESCATES DE STDR ##############################
##########################################################################################
# bpm = redflagbpm.BPMService()
# # tipo = bpm.context['tipo']
# # if tipo == 'Rescate':
#     #lista todos los rescates
# resp = bilateral_rescate_listar_c_filtros(fecha_alta_desde=last_business_days, fecha_alta_hasta=fecha_alta_hasta)
# print(resp.json())
#
# update_rescates_eliminados(conn, fecha_alta_desde=last_business_days, fecha_alta_hasta=fecha_alta_hasta)
#
# #lista todos los rescates con filtros opcionales (puede ser igual al método anterior con los filtros adecuados)
# for rescate in resp.json()['items']:
#     #string estado to upper case
#     estado = rescate['estado'].upper()
#     nro_pedido = rescate['numeroPedido'] if 'numeroPedido' in rescate.keys() else None
#     id_grupo = rescate['idOrigen']
#     fecha_alta = rescate['fechaAlta']
#     especie = rescate['especie']
#     try:
#         cantidad_cp = rescate["cantidadCuotaPartes"]
#     except KeyError:
#         cantidad_cp = None
#     # precio = rescate['precio']
#     # monto = rescate['monto'] if 'monto' in rescate.keys() else None
#
#     #consulta del detalle de la distribución por comitentes de un rescate
#     resp_comit = bilateral_rescate_listar_comitentes(rescate['rescateId'])
#
#     update_rescate_status(conn, id_grupo, mensaje='Sincronizado con STDR ' + estado, estado=estado,
#                           nro_pedido=nro_pedido, fecha_alta=fecha_alta, especie=especie, cantidad_cp=cantidad_cp,
#                           distribucion=json.dumps(resp_comit.json()['items']), id_rescate=rescate['rescateId'])

