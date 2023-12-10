#!python3
import time

import redflagbpm
from endpoints_hg import login, suscripcion_fci
from auxiliar import procesar_respuesta
from datetime import datetime
import logging
import http.client as http_client
import re
import sys
sys.path.append('../backtesting')
from backtest_data import get_backtesting_data
import threading
import concurrent.futures


http_client.HTTPConnection.debuglevel = 1
format = "%(asctime)s: %(message)s"
# initialize logging
logging.basicConfig(format=format, level=logging.INFO, datefmt='%H:%M:%S')
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


def suscribir(fecha, cuenta, array_solicitudes_pendientes, solicitud, array_solicitudes_confirmadas, name):
    fondo_deno = solicitud['fondo']
    fondo_id = re.search(r'([\d]+)', fondo_deno).group(1)
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
    logging.info('Thread %s: starting', name)
    # response = suscripcion_fci(token, url_base, data)
    time.sleep(5+name)
    # resp_alta_ok, mje = procesar_respuesta(response, 'Suscripcion Alta:')
    resp_alta_ok, mje = True, None
    if not resp_alta_ok:
        solicitud["error"] = mje
    else:
        array_solicitudes_pendientes.remove(solicitud)
        array_solicitudes_confirmadas.append(solicitud)
    logging.info('Thread %s: finishing', name)

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    try:

        if bpm.service.text("STAGE") == 'DEV':
            url_base = f'https://demo.aunesa.dev:10017/Irmo/api/'
        else:
            url_base = f''
        # token = login(url_base)
        token = 'token_gfalso'
        # el form manda la fecha en milisegundos al proceso
        # y el proceso la guarda como fecha de java
        # -> uso .getTime() para obtener los milisegundos
        get_backtesting_data(bpm)
        fecha = formatear(bpm.context['fecha.getTime()'])
        cuenta = bpm.context['cuenta']
        array_solicitudes_pendientes = bpm.context['array_solicitud_pendiente']
        try:
            array_solicitudes_confirmadas = bpm.context['array_solicitud_confirmada']
        except:
            array_solicitudes_confirmadas = []



        thread_list = []
        i = 1
        # for solicitud in array_solicitudes_pendientes:
        #     #suscribir(fecha, cuenta, array_solicitudes_pendientes, solicitud, array_solicitudes_confirmadas)
        #     x = threading.Thread(target=suscribir, args=(
        #     fecha, cuenta, array_solicitudes_pendientes, solicitud, array_solicitudes_confirmadas, i))
        #     thread_list.append(x)
        #     logging.info('Main    :before running thread')
        #     x.start()
        #     logging.info('Main    :wait for thread to finish')
        #     i+=1
        #
        # for th in thread_list:
        #     # if th.is_alive() waits else continues
        #     th.join()

        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            i=1
            for solicitud in array_solicitudes_pendientes:
                logging.info('Main    :before running thread')
                executor.submit(suscribir, fecha, cuenta, array_solicitudes_pendientes, solicitud, array_solicitudes_confirmadas, i)
                i+=1


        if len(array_solicitudes_pendientes) == 0:
            print(len(array_solicitudes_pendientes))
        #     bpm.execution.setVariable('terminado', True)
        # else:
        #     bpm.execution.setVariable('terminado', False)
        # bpm.execution.setVariable('array_solicitud_pendiente', array_solicitudes_pendientes)
        # bpm.execution.setVariable('array_solicitud_confirmada', array_solicitudes_confirmadas)
    except:
        bpm.fail()
