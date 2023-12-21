#!python3
import locale

import redflagbpm

import sys
sys.path.append('../backtesting')
from backtest_data import get_backtesting_redemption_data
from GET_COTIZACIONES import get_cotizacion_cafci, get_cotizacion_provisoria, get_fci_simbolo_local
import re
from DB import _get_hg_connection, _get_connection


def get_cotiz_dict(fondo_deno):
    # BUSCO COTIZACION CAFCI#####
    # extraigo el codigo de fci
    matches = re.search(r'(\d+)', fondo_deno)
    id_fondo= matches.group(1)
    # del simbolo local obtengo: el id cafci y el id clase
    cafci_id, id_clase = get_fci_simbolo_local(conn=_get_hg_connection(bpm), id_fondo=id_fondo)

    # obtengo la cotizacion de la API de CAFCI
    cafci_dict = dict(get_cotizacion_cafci(fci_id=cafci_id, class_id=id_clase))

    # agrego manualmente hora a la fecha en formato dd/MM/yyyy HH:mm:ss
    cafci_dict['fecha_cotizacion'] = cafci_dict['fecha'] + ' 23:59:59'


    ##########################

    ###BUSCO COTIZACION PROVISORIA#####
    if bpm.service.text("STAGE") == 'DEV':
        conn = _get_connection(bpm)
    else:
        #todo: revisar cómo se comporta en prod
        conn = _get_connection('flowable')
    # read from get_cotizacion_provisoria and recover values
    manual_cotiz = get_cotizacion_provisoria(conn, id_fondo)


    ###COMPARO LAS COTIZ EN BASE A LA FECHA######
    cotiz_dict = {}

    if manual_cotiz is not None and manual_cotiz['fecha_cotizacion_manual'] > cafci_dict['fecha_cotizacion']:
        cotiz_dict['fecha_cotizacion'] = manual_cotiz['fecha_cotizacion_manual']
        cotiz_dict['precio'] = manual_cotiz['vcp_provisorio']
    else:
        cotiz_dict['fecha_cotizacion'] = cafci_dict['fecha_cotizacion']
        cotiz_dict['precio'] = float(cafci_dict['vcpUnitario'])

    return cotiz_dict


def crearDistri(cotiz_dict):
    if cotiz_dict != None:
        ret = "<table class=\"tg\">"
        ret += (
            "<tr>"
                "<th class=\"tg-0lax center bold gray\">Fecha cotización</th>"
                "<th class=\"tg-0lax center bold gray\">Cotización CP</th>"
                "<th class=\"tg-0lax center bold gray\">Monto</th>"
            "</tr>"
                )

        ret += (f"<tr>"
                f"<td class=\"tg-0lax center\">{cotiz_dict['fecha_cotizacion']}</td>"
                f"<td class=\"tg-0lax center\">{cotiz_dict['precio']}</td>"
                f"<td class=\"tg-0lax center\">{cotiz_dict['monto']}</td>"
                f"</tr>")
        ret += "</table>"

        return ret

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    #todo: comment the following outside local tests
    # get_backtesting_redemption_data(bpm)
    calcular_solicitar_string = ""
    array_solicitud_pendiente = bpm.context['array_solicitud_pendiente']

    for solicitud in array_solicitud_pendiente:
        fondo_deno = solicitud['fondo']
        cantidad_importe = solicitud['cantidad_importe']

        cotiz_dict = get_cotiz_dict(fondo_deno)

        monto = cotiz_dict['precio'] * cantidad_importe
        #saving to original array
        solicitud['precio'] = cotiz_dict['precio']
        solicitud['monto'] = monto


        # Set the locale to 'es_AR' for Argentina
        locale.setlocale(locale.LC_ALL, 'es_AR.utf8')
        # Format the number according to the locale
        formatted_monto = locale.format_string("%.2f", monto, grouping=True)
        cotiz_dict['monto'] = formatted_monto

        formatted_precio = locale.format_string("%.2f", cotiz_dict['precio'], grouping=True)
        cotiz_dict['precio'] = formatted_precio
        calcular_solicitar_string += f"{fondo_deno}_{cantidad_importe}_{monto}"

        html = """
        <div>
            <style type="text/css">
            .tg  {border-collapse:collapse;border-spacing:0;margin:0px auto; width:100%;}
            .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
              overflow:hidden;padding:10px 5px;word-break:normal;}
            .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;overflow:hidden;padding:10px 5px;word-break:normal;}
            .tg .tg-0lax{text-align:left;vertical-align:top;}
            .center{text-align:center !important;}
            .bold{font-weight:700;}
            .gray{background-color: lightgray;}
            .fiftyw{width:52.5%;}
            .leftp{padding-left: 30px !important;}
            </style> """+f"""{crearDistri(cotiz_dict)}
        </div>
        """
        solicitud['calculos'] = html

    print(f"ARRAY SOLICITUD PENDIENTE: \n{array_solicitud_pendiente}")

    bpm.context.input['array_solicitud_pendiente'] = array_solicitud_pendiente
    bpm.context.input['calcular_solicitar_string'] = calcular_solicitar_string

    #debugging
    try:
        array_solicitud_confirmada = bpm.context.input['array_solicitud_confirmada']
        print(f"ARRAY SOLICITUD CONFIRMADA: \n{array_solicitud_confirmada}")
    except KeyError:
        print("El array_solicitud_confirmada no existe")


