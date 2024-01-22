#!python3
import json
from datetime import datetime
def procesar_respuesta(resp, tarea):
    if resp.status_code == 400:
        resp_json = json.loads(resp.text)
        err = resp_json['errors'][0]['detail']
        err = str(tarea)+' ' + str(err)
        print(str(err))
        return False, str(err)
    elif resp.status_code == 200 or resp.status_code == 201:
        return True, None
    elif resp.status_code == 409:
        err = tarea+' ' + 'Conflicto: ' + resp.text
        return False, str(err)
    else:
        print("Error en el request")
        err = tarea+' ' + str(resp.status_code) + ' ' + resp.text
        return False, str(err)

def formatear(milisegundos):
    #leer el formato original
    segundos = milisegundos / 1000.0
    fecha_hora = datetime.fromtimestamp(segundos)

    nuevo_formato = "%d/%m/%Y %H:%M:%S"
    fecha_formateada = fecha_hora.strftime(nuevo_formato)
    return fecha_formateada