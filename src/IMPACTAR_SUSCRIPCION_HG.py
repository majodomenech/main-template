#!python3
import json

import redflagbpm
from enpoints_hg import login, suscripcion_fci


import logging
import http.client as http_client
http_client.HTTPConnection.debuglevel = 1
#initialize logging
logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

bpm = redflagbpm.BPMService()
cuenta = bpm.context['cuenta']

bpm = redflagbpm.BPMService()
url_base = f'https://demo.aunesa.dev:10017/Irmo/api/'
token = login(bpm, url_base)

cuenta = bpm.context['cuenta']
fecha = bpm.context['fecha']
fondo = bpm.context['fondo']
cantidad = bpm.context['cantidad']
integraComitente = bpm.context['integraComitente']

data = {
      "contexto": {
            "modalidad": "BILATERAL",
            "origen": "S&C",
            "acdi": "57"
      },
      "solicitud": {
            "fechaSolicitud": fecha,
            "cuentaComitente": cuenta,
            "fondo": fondo,
            "especieMoneda": "ARS",
            "cantidad": cantidad,
            "integraComitente": integraComitente,
            "aceptaReglamento": True
      }
}


response = suscripcion_fci(token, url_base, data)
response = json.loads(response)
print(response)
try:
      print(response.json())
except:
      print(response["errors"])
