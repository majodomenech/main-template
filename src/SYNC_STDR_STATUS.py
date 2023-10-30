#!python3
import json
from DB_connect import _get_flw_connection
from endpoints_santander import login_apigee, search_subscription, get_subscription, get_redemption, search_redemption
import datetime
from auxiliar import get_b_day
from write_DB import update_rescate_status, update_suscripcion_status


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

headers = login_apigee()
#listar todas las suscris confiltro de fecha de alta
resp = search_subscription(headers)
# print(resp.text)

for suscripcion in resp.json()['result']:
    # print(suscripcion)
    # #string estado to upper case
    estado = suscripcion['status'].upper()
    certif_id = suscripcion['certificateId'] if 'certificateId' in suscripcion.keys() else None
    id_origen = suscripcion['externalReference']
    fecha_alta = suscripcion['processDate']
    especie = suscripcion['fundId']
    cantidad_cp = suscripcion["netShare"]
    resp_x_id = get_subscription(headers, suscripcion['transactionId'])
    update_suscripcion_status(conn, id_origen, mensaje='Sincronizado con STDR ' + estado, estado=estado,
                          certif_id=certif_id, fecha_alta=fecha_alta, especie=especie, cantidad_cp=cantidad_cp, id_suscri = suscripcion['transactionId'])
    # print(resp_x_id.json())

##########################################################################################
############################### RECUPERAR LOS RESCATES DE STDR ##############################
##########################################################################################

# update_rescates_eliminados(conn, fecha_alta_desde=last_business_days, fecha_alta_hasta=fecha_alta_hasta)
headers = login_apigee()
resp = search_redemption(headers)
print(resp.text)
# #lista todos los rescates con filtros opcionales (puede ser igual al método anterior con los filtros adecuados)
for rescate in resp.json()['result']:
    print(rescate)
#     #string estado to upper case
    estado = rescate['status'].upper()
    certif_id = rescate['certificateId'] if 'certificateId' in rescate.keys() else None
    id_origen = rescate['externalReference']
#     id_grupo = rescate['idOrigen']
    fecha_alta = rescate['processDate']
    especie = rescate['fundId']
    cantidad_cp = rescate["netShare"]
    try:
        cantidad_cp = rescate["netShare"]
    except KeyError:
        cantidad_cp = None
    precio = rescate['shareValue']
    monto = rescate['netAmount'] if 'netAmount' in rescate.keys() else None

    update_rescate_status(conn, id_origen, mensaje='Sincronizado con STDR ' + estado, estado=estado,
                          certif_id=certif_id, fecha_alta=fecha_alta, especie=especie, cantidad_cp=cantidad_cp,
                           id_rescate=rescate['transactionId'])

