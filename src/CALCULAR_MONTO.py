#!python3
import redflagbpm

import sys
sys.path.append('../backtesting')
from backtest_data import get_backtesting_redemption_data
from GET_COTIZACIONES import get_cotizacion_cafci, get_cotizacion_provisoria, get_fci_simbolo_local
import re
from DB import _get_hg_connection, _get_flw_connection


def get_cotiz_dict(fondo_deno):
    conn = _get_hg_connection('syc')
    # BUSCO COTIZACION CAFCI#####

    # extraigo el codigo de fci, el id cafci y el id clase
    matches = re.search(r'(\d+)] CAFCI(\d+)-(\d+)', fondo_deno)
    id_fondo= matches.group(1)
    cafci_id = matches.group(2)
    id_clase = matches.group(3)

    # obtengo la cotizacion de la API de CAFCI
    cafci_dict = dict(get_cotizacion_cafci(cafci_id, id_clase))

    # agrego manualmente hora a la fecha en formato dd/MM/yyyy HH:mm:ss
    cafci_dict['fecha_cotizacion'] = cafci_dict['fecha'] + ' 23:59:59'


    ##########################

    ###BUSCO COTIZACION PROVISORIA#####
    if bpm.service.text("STAGE") == 'DEV':
        conn = _get_flw_connection('flowabletest')
    else:
        conn = _get_flw_connection('flowable')
    # read from get_cotizacion_provisoria and recover values
    manual_cotiz = get_cotizacion_provisoria(conn, id_fondo)


    ###COMPARO LAS COTIZ EN BASE A LA FECHA######
    cotiz_dict = {}

    if manual_cotiz is not None and manual_cotiz['fecha_cotizacion_manual'] > cafci_dict['fecha_cotizacion']:
        cotiz_dict['fecha_cotizacion'] = manual_cotiz['fecha_cotizacion_manual']
        cotiz_dict['precio'] = manual_cotiz['vcp_provisorio']
    else:
        cotiz_dict['fecha_cotizacion'] = cafci_dict['fecha_cotizacion']
        cotiz_dict['precio'] = cafci_dict['vcpUnitario']

    return cotiz_dict


def crearDistri(cotiz_dict):
    if cotiz_dict != None:
        ret = "<table class=\"tg\">"
        ret += "<tr><th class=\"tg-0lax center bold gray\">COMITENTE</th><th class=\"tg-0lax center bold gray\">CANTIDAD</th></tr>"
        # for c in cotiz_dict.items():
        ret += f"<tr><td class=\"tg-0lax center\">{cotiz_dict['fecha_cotizacion']}</td><td class=\"tg-0lax center\">{cotiz_dict['monto']}</td></tr>"
        ret += "</table>"

        return ret

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    #todo: comment the following outside local tests
    # get_backtesting_redemption_data(bpm)
    array_solicitud_pendiente = bpm.context['array_solicitud_pendiente']

    for solicitud in array_solicitud_pendiente:
        fondo_deno = solicitud['fondo']
        cantidad_importe = solicitud['cantidad_importe']

        cotiz_dict = get_cotiz_dict(fondo_deno)

        monto = cotiz_dict['precio'] * cantidad_importe
        cotiz_dict['monto'] = monto



    html = f"""
        {crearDistri(cotiz_dict)}
    """

    array_solicitud_pendiente['calculos'] = html
