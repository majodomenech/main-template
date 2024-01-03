#!python3
import json
import re
import sys
sys.path.append('../backtesting')
from backtest_data import get_backtesting_redemption_data
import redflagbpm
from endpoints_hg import login, rescate_fci
from auxiliar import procesar_respuesta, formatear
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



if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    try:
        if bpm.service.text("STAGE") == 'DEV':
            url_base = f'https://demo.aunesa.dev:10017/Irmo/api/'
        else:
            url_base = f''
        token = login(url_base)
        #todo unncoment in local tests only
        # get_backtesting_redemption_data(bpm)
        fecha = formatear(bpm.context['fecha.getTime()'])
        cuenta = bpm.context['cuenta']

        array_solicitudes_pendientes = bpm.context['array_solicitudes_pendientes']
        try:
            array_solicitudes_confirmadas = bpm.context['array_solicitudes_confirmadas']
        except:
            array_solicitudes_confirmadas = []

        for solicitud in array_solicitudes_pendientes:
            fondo_deno = solicitud['fondo']
            fondo_id = re.search(r'([\d]+)', fondo_deno).group(1)

            rescateDinero = solicitud['rescate_dinero']
            cantidadImporte = solicitud['cantidad_importe']

            if bpm.service.text("STAGE") == 'DEV':
                data_res = {
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
                data_res = {
                    "contexto": {
                        "modalidad": "BILATERAL",
                        "origen": "S&C",
                        "acdi": "000"
                    },
                    "solicitud": {
                        "fechaSolicitud": fecha,
                        "cuentaComitente": cuenta,
                        "fondo": fondo_id,
                        "rescateDinero": rescateDinero,
                        "cantidadImporte": cantidadImporte
                    }
                }

            response = rescate_fci(token=token, url_base=url_base, data=data_res)

            resp_alta_ok, mje = procesar_respuesta(response, 'Rescate: Alta')
            if not resp_alta_ok:
                solicitud["error"] = mje
            else:
                array_solicitudes_pendientes.remove(solicitud)
                array_solicitudes_confirmadas.append(solicitud)


        if len(array_solicitudes_pendientes) == 0:
            bpm.execution.setVariable('terminado', True)
        else:
            bpm.execution.setVariable('terminado', False)
        bpm.execution.setVariable('array_solicitudes_pendientes', array_solicitudes_pendientes)
        bpm.execution.setVariable('array_solicitudes_confirmadas', array_solicitudes_confirmadas)
    except:
        bpm.fail()
