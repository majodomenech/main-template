#!python3

import redflagbpm
from enpoints_hg import login, suscripcion_fci
from auxiliar import procesar_respuesta
from datetime import datetime
import logging
import http.client as http_client
import pytz
http_client.HTTPConnection.debuglevel = 1
#initialize logging
logging.basicConfig()
#logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True


def formatear(milisegundos):
    #leer el formato original
    segundos = milisegundos / 1000.0
    fecha_hora = datetime.fromtimestamp(segundos)

    nuevo_formato = "%d/%m/%Y %H:%M:%S"
    fecha_formateada = fecha_hora.strftime(nuevo_formato)
    return fecha_formateada

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    if bpm.service.text("STAGE") == 'DEV':
        url_base = f'https://demo.aunesa.dev:10017/Irmo/api/'
    else:
        url_base = f''
    token = login(url_base)

    # el form manda la fecha en milisegundos al proceso
    # y el proceso la guarda como fecha de java
    # -> uso .getTime() para obtener los milisegundos

    fecha = formatear(bpm.context['fecha.getTime()'])
    cuenta = bpm.context['cuenta']
    array_solicitudes_pendientes = bpm.context['array_solicitud_pendiente']
    try:
        array_solicitudes_confirmadas = bpm.context['array_solicitud_confirmada']
    except:
        array_solicitudes_confirmadas = []

    for solicitud in array_solicitudes_pendientes:
        fondo = solicitud['fondo']
        moneda = solicitud['moneda']
        cantidad = solicitud['cantidad']
        integraComitente = solicitud['integra_comitente']

        data = {
            "contexto": {
                "modalidad": "BILATERAL",
                "origen": "S&C",
                "acdi": "000"
            },
            "solicitud": {
                "fechaSolicitud": fecha,
                "cuentaComitente": "141390",
                "fondo": "14325",
                "especieMoneda": "ARS",
                "cantidad": cantidad,
                "integraComitente": integraComitente,
                "aceptaReglamento": True
            }
        }

        response = suscripcion_fci(token, url_base, data)

        resp_alta_ok, mje = procesar_respuesta(response, 'Suscripcion Alta:')
        if not resp_alta_ok:
            solicitud["error"] = mje
        else:
            array_solicitudes_pendientes.remove(solicitud)
            array_solicitudes_confirmadas.append(solicitud)

    if len(array_solicitudes_pendientes) == 0:
        bpm.execution.setVariable('terminado', True)
    else:
        bpm.execution.setVariable('terminado', False)
    bpm.execution.setVariable('array_solicitud_pendiente', array_solicitudes_pendientes)
    bpm.execution.setVariable('array_solicitud_confirmada', array_solicitudes_confirmadas)
