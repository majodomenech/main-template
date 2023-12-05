#!python3
import json

def procesar_respuesta(resp, tarea):
    if resp.status_code == 400:
        resp = json.loads(resp.text)
        err = resp['errors'][0]['detail']
        err = str(tarea)+' ' + str(err)
        return False, str(err)
    elif resp.status_code == 200 or resp.status_code == 201:
        return True, None
    elif resp.status_code == 409:
        resp = json.loads(resp.text)
        err = tarea+' ' + 'Conflicto: ' + resp
        return False, str(err)
    else:
        print("Error en el request")
        resp = json.loads(resp.text)
        err = tarea+' ' + str(resp.status_code) + ' ' + resp
        return False, str(err)
