#!python3
import locale

import redflagbpm

import sys
sys.path.append('../backtesting')
from backtest_data import get_backtesting_redemption_data
from GET_COTIZACIONES import get_cotizacion_cafci, get_cotizacion_provisoria
from GET_FCI_INFO import get_moneda_fondo, get_fci_simbolo_local
import re
from DB import _get_hg_connection, _get_connection


def get_cotiz_dict(codigo_fci):
    # BUSCO COTIZACION CAFCI#####

    # del simbolo local obtengo: el id cafci y el id clase
    cafci_id, id_clase = get_fci_simbolo_local(conn=_get_hg_connection(bpm), id_fondo=codigo_fci)

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
    manual_cotiz = get_cotizacion_provisoria(conn, codigo_fci)


    ###COMPARO LAS COTIZ EN BASE A LA FECHA######
    cotiz_dict = {}

    if manual_cotiz is not None and manual_cotiz['fecha_cotizacion_manual'] > cafci_dict['fecha_cotizacion']:
        cotiz_dict['fecha_cotizacion'] = manual_cotiz['fecha_cotizacion_manual']
        cotiz_dict['precio'] = float(manual_cotiz['vcp_provisorio'])
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
                "<th class=\"tg-0lax center bold gray\">Moneda</th>"
                "<th class=\"tg-0lax center bold gray\">Monto</th>"
            "</tr>"
                )

        ret += (f"<tr>"
                f"<td class=\"tg-0lax center\">{cotiz_dict['fecha_cotizacion']}</td>"
                f"<td class=\"tg-0lax center\">{cotiz_dict['precio']}</td>"
                f"<td class=\"tg-0lax center\">{cotiz_dict['moneda_fondo']}</td>"
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
        #leo el user input
        fondo_deno = solicitud['fondo']
        cantidad_importe = solicitud['cantidad_importe']
        monto = solicitud['monto']

        # extraigo el codigo de fci
        matches = re.search(r'(\d+)', fondo_deno)
        codigo_fci = matches.group(1)
        #busco la cotización más reciente
        cotiz_dict = get_cotiz_dict(codigo_fci)
        #busco la moneda original del fondo
        moneda_fondo = get_moneda_fondo(codigo_fci=codigo_fci)
        #guardo la moneda en el array original
        solicitud['moneda_fondo'] = moneda_fondo

        #guardo la moneda en el dict de la calculadora
        cotiz_dict['moneda_fondo'] = moneda_fondo

        # Set the locale format to 'es_AR' for Argentina
        locale.setlocale(locale.LC_ALL, 'es_AR.utf8')

        if monto is None and cantidad_importe is not None:
            #calculo el monto

            monto = cotiz_dict['precio'] * cantidad_importe
            #lo agrego al array original sin formatear
            solicitud['monto'] = monto
            # Format the number according to the locale
            formatted_monto = locale.format_string("%.2f", monto, grouping=True)
            #lo agrego al diccionario de cotiz formateado
            cotiz_dict['monto'] = formatted_monto

        elif monto is not None and (cantidad_importe is None or cantidad_importe == monto/cotiz_dict['precio']):
            cantidad_importe = monto/cotiz_dict['precio']
            # Truncate to 6 decimal places without rounding
            truncated_number = int(cantidad_importe * 1e6) / 1e6
            # Format nominal and amount according to the locale
            # formatted_cantidad_importe = locale.format_string("%.6f", cantidad_importe, grouping=True)
            solicitud['cantidad_importe'] = truncated_number

            formatted_monto = locale.format_string("%.6f", monto, grouping=True)
            #lo agrego al diccionario de cotiz formateado
            cotiz_dict['monto'] = formatted_monto
        else:
            error = "[[[Cargar Monto o cuotapartes pero no ambos]]]"
            bpm.fail(error)
        #saving precio to original array
        solicitud['precio'] = cotiz_dict['precio']
        #formateando el precio
        formatted_precio = locale.format_string("%.6f", cotiz_dict['precio'], grouping=True)
        cotiz_dict['precio'] = formatted_precio
        #completando el string de validacion
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



