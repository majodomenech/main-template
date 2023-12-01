#!python3
import redflagbpm
from enpoints_hg import login, suscripcion_fci

bpm = redflagbpm.BPMService()
cuenta = bpm.context['cuenta']

bpm = redflagbpm.BPMService()
url_base = f'https://demo-4.aunesa.dev:10064/Irmo/api/'
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

