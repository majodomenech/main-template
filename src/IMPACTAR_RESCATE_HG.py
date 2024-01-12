#!python3
import time
import redflagbpm
from endpoints_hg import rescate_fci, setup_url_base, login
from auxiliar import procesar_respuesta
from datetime import datetime
import logging
import http.client as http_client
import re
import sys
sys.path.append('../backtesting')
from backtest_data import get_backtesting_redemption_data
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


def rescatar(fecha, cuenta_id, array_solicitudes_pendientes, solicitud, array_solicitudes_confirmadas, thread_name):
    fondo_deno = solicitud['fondo']
    fondo_id = re.search(r'([\d]+)', fondo_deno).group(1)
    solicitud['fondo_id'] = fondo_id
    # rescateDinero = solicitud['rescate_dinero']
    rescateDinero = False
    cantidadImporte = solicitud['cantidad_importe']

    if bpm.service.text("STAGE") == 'DEV':
        data = {
            "contexto": {
                "modalidad": "BILATERAL",
                "origen": "S&C",
                "acdi": "000"
            },
            "solicitud": {
                "fechaSolicitud": fecha,
                "cuentaComitente": "145196",
                "fondo": "14300",
                "rescateDinero": rescateDinero,
                "cantidadImporte": cantidadImporte
            }
        }
    else:
        data = {
            "contexto": {
                "modalidad": "BILATERAL",
                "origen": "S&C",
                "acdi": "000"
            },
            "solicitud": {
                "fechaSolicitud": fecha,
                "cuentaComitente": cuenta_id,
                "fondo": fondo_id,
                "rescateDinero": rescateDinero,
                "cantidadImporte": cantidadImporte
            }
        }

    logging.info('Thread %s: starting', thread_name)
    response = rescate_fci(token=token, url_base=url_base, data=data)
    # time.sleep(5)
    resp_alta_ok, mje = procesar_respuesta(response, 'Rescate Alta:')
    # backtesting si no anda hg test
    # resp_alta_ok, mje = False, "error inventado"
    # resp_alta_ok, mje = True, None
    if not resp_alta_ok:
        solicitud["error"] = mje
        return mje
    else:
        array_solicitudes_pendientes.remove(solicitud)
        solicitud["numero_solicitud"] = response.json()["solicitud"]['numeroSolicitud']
        array_solicitudes_confirmadas.append(solicitud)
        return None
    logging.info('Thread %s: finishing', thread_name)

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    try:
        url_base = setup_url_base(bpm)
        token = login(bpm,url_base)

        #todo unncoment in local tests only
        # get_backtesting_redemption_data(bpm)

        # el form manda la fecha en milisegundos al proceso
        # y el proceso la guarda como fecha de java
        # -> uso .getTime() para obtener los milisegundos
        fecha = formatear(bpm.context['fecha.getTime()'])
        cuenta_id = bpm.context['cuenta']
        array_solicitudes_pendientes = bpm.context['array_solicitudes_pendientes']
        try:
            array_solicitudes_confirmadas = bpm.context['array_solicitudes_confirmadas']
        except:
            array_solicitudes_confirmadas = []

        #defino la lista future_results donde almaceno la "promesa" de la respuesta de todos
        # los threads
        future_results = []
        i = 1
        with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
            i=1
            for solicitud in array_solicitudes_pendientes:
                logging.info('Main    :before running thread')
                futuro = executor.submit(rescatar, fecha=fecha, cuenta_id=cuenta_id, array_solicitudes_pendientes=array_solicitudes_pendientes, solicitud=solicitud, array_solicitudes_confirmadas=array_solicitudes_confirmadas, thread_name=i)
                future_results.append(futuro)
                i+=1

        final_results = [result.result() for result in future_results]

        if len(array_solicitudes_pendientes) == 0:
            bpm.execution.setVariable('accion', "continuar")
            error_x_duplicado = False
        else:
            pattern = '(Ya existe una solicitud pendiente con estos datos. Por favor actualice la solicitud previa.)'
            # itero el resultado de todos los threads
            for res in final_results:
                # comparo con el error de solicitud repetida
                try:
                    err_solicitud_duplicada = re.search(pattern, res).group(1)
                except AttributeError:
                    err_solicitud_duplicada = None
                # si no hay error o es un error por otro motivo -> error x duplicado es falso
                if err_solicitud_duplicada is None:
                    error_x_duplicado = False
                # si el error es por solicitud repetida-> error x duplicado es verdadero (y sobreescribe le valor anterior)
                else:
                    error_x_duplicado = True

        # si hay algún error por solicitud repetida -> accion: reintentar
        if error_x_duplicado:
            bpm.execution.setVariable('accion', 'reintentar')
        # si hay error pero no de duplicados ->accion: corregir
        else:
            bpm.execution.setVariable('accion', 'corregir')

        bpm.execution.setVariable('array_solicitudes_pendientes', array_solicitudes_pendientes)
        bpm.execution.setVariable('array_solicitudes_confirmadas', array_solicitudes_confirmadas)
    except:
        bpm.fail()
