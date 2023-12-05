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




def convertir_milisegundos_a_fecha_hora(milisegundos):
    # Convertir milisegundos a segundos
    segundos = float(milisegundos) / 1000.0
    print(80*'##')
    print(milisegundos)
    print(float(milisegundos))
    print(80 * '##')
    # Crear un objeto datetime a partir de los segundos
    fecha_hora = datetime.fromtimestamp(segundos)

    # Formatear la fecha y hora según tus necesidades
    formato = "%d/%m/%Y %H:%M:%S"
    fecha_hora_formateada = fecha_hora.strftime(formato)

    return fecha_hora_formateada

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    url_base = f'https://demo.aunesa.dev:10017/Irmo/api/'
    token = login(bpm, url_base)

    milisegundos = bpm.context['fecha']
    fecha = convertir_milisegundos_a_fecha_hora(milisegundos)
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

