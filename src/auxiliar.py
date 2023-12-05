#!python3

def procesar_respuesta(resp, tarea):
    if resp.status_code == 400:
        err = str(tarea)+' ' + resp["errors"]['descripcion']
        return False, str(err)
    elif resp.status_code == 200 or resp.status_code == 201:
        return True, None
    elif resp.status_code == 409:
        err = tarea+' ' + 'Conflicto: ' + resp.text
        return False, str(err)
    else:
        print("Error en el request")
        print(resp)
        err = tarea+' ' + str(resp.status_code) + ' ' + resp.text
        return False, str(err)
