#!python3
import json

import redflagbpm
from enpoints_hg import login, suscripcion_fci
from auxiliar import procesar_respuesta

import logging
import http.client as http_client
http_client.HTTPConnection.debuglevel = 1
#initialize logging
logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    url_base = f'https://demo.aunesa.dev:10017/Irmo/api/'
    token = login(bpm, url_base)

    fecha = bpm.context['fecha']
    cuenta = bpm.context['cuenta']
    fondo = bpm.context['fondo']
    moneda = bpm.context['moneda']
    cantidad = bpm.context['cantidad']
    integraComitente = bpm.context['integra_comitente']

    data_res = {
        "contexto": {
            "modalidad": "BILATERAL",
            "origen": "S&C",
            "acdi": "57"
        },
        "solicitud": {
            "fechaSolicitud": fecha,
            "cuentaComitente": "[145196] JUAN AUNE",
            "fondo": "14300",
            "especieMoneda": "14300",
            "cantidad": 100000,
            "rescateDinero": False,
            "aceptaReglamento": True
        }
    }


    response = suscripcion_fci(token, url_base, data)

    print(response)
    resp_alta_ok, mje = procesar_respuesta(response, 'Rescate: Alta')
    if not resp_alta_ok:
        bpm.execution.setVariable("errors", mje)

