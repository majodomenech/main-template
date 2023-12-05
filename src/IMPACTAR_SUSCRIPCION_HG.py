#!python3
import json

import redflagbpm
from enpoints_hg import login, suscripcion_fci
from auxiliar import procesar_respuesta
from datetime import datetime
import logging
import http.client as http_client
http_client.HTTPConnection.debuglevel = 1
#initialize logging
logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True




def formatear(fecha):
    #leer el formato original
    fecha_hora = datetime.strptime(fecha, "%a %b %d %H:%M:%S %Z %Y")
    # Formatear la fecha y hora
    nuevo_formato = "%d/%m/%Y %H:%M:%S"
    fecha_formateada = fecha_hora.strftime(nuevo_formato)
    return fecha_formateada

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    url_base = f'https://demo.aunesa.dev:10017/Irmo/api/'
    token = login(bpm, url_base)

    fecha = formatear(bpm.context['fecha'])
    cuenta = bpm.context['cuenta']
    fondo = bpm.context['fondo']
    moneda = bpm.context['moneda']
    cantidad = bpm.context['cantidad']
    integraComitente = bpm.context['integra_comitente']

    data = {
        "contexto": {
            "modalidad": "BILATERAL",
            "origen": "S&C",
            "acdi": "000"
        },
        "solicitud": {
            "fechaSolicitud": fecha,
            "cuentaComitente": "02597",
            "fondo": "14325",
            "especieMoneda": "ARS",
            "cantidad": cantidad,
            "integraComitente": integraComitente,
            "aceptaReglamento": True
        }
    }


    response = suscripcion_fci(token, url_base, data)

    # print(response)
    resp_alta_ok, mje = procesar_respuesta(response, 'Suscripcion Alta:')
    if not resp_alta_ok:
        bpm.execution.setVariable("errors", mje)

