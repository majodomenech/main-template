#!python3
import locale

import redflagbpm

import sys
sys.path.append('../backtesting')
from backtest_data import get_backtesting_redemption_data
from GET_COTIZACIONES import get_cotizacion_cafci, get_cotizacion_provisoria, get_cotizacion_hg
from GET_FCI_INFO import get_moneda_fondo, get_fci_simbolo_local
import re
from DB import _get_hg_connection, _get_connection
from datetime import datetime


def get_cotiz_dict(codigo_fci):
    # BUSCO COTIZACION CAFCI#####
    # del simbolo local obtengo: el id cafci y el id clase
    cafci_id, id_clase = get_fci_simbolo_local(conn=_get_hg_connection(bpm), id_fondo=codigo_fci)

    # intento obtener la cotizacion de la CAFCI
    try:
        cafci_dict = dict(get_cotizacion_cafci(fci_id=cafci_id, class_id=id_clase))
    except TypeError:
        cafci_dict = None
    if cafci_dict is not None:
        # agrego manualmente hora a la fecha en formato dd/MM/yyyy HH:mm:ss y lo convierto a datetime
        cafci_dict['fecha_cotizacion'] = datetime.strptime(cafci_dict['fecha'] + ' 23:59:59', '%d/%m/%Y %H:%M:%S')
    else:
        # si no hay cotizacion de la CAFCI, busco en el WS de HG
        #get today's date
        fecha = datetime.today().strftime('%d/%m/%Y')
        hg_dict = dict(get_cotizacion_hg(bpm, codigo_fci=codigo_fci, fecha=fecha))
        # agrego manualmente hora a la fecha en formato dd/MM/yyyy HH:mm:ss y lo convierto a datetime (especificando el formato que recibe)
        hg_dict[codigo_fci]['fecha_cotizacion'] = datetime.strptime(hg_dict[codigo_fci]['fecha'] + ' 19:00:00', '%Y-%m-%d %H:%M:%S')


    ##########################
    ###BUSCO COTIZACION PROVISORIA#####
    conn = _get_connection(bpm)
    # read from get_cotizacion_provisoria and recover values
    manual_cotiz = get_cotizacion_provisoria(conn, codigo_fci)
    if manual_cotiz is not None:
        manual_cotiz['fecha_cotizacion_manual'] = datetime.strptime(manual_cotiz['fecha_cotizacion_manual'],
                                                                    '%d/%m/%Y %H:%M:%S')


    ###COMPARO LAS COTIZ EN BASE A LA FECHA######

    cotiz_dict = {}
    # si la cotizacion manual no es None y la cotizacion de la cafci no es None
    if manual_cotiz is not None:
        if cafci_dict is not None:
            #si la cotizacion manual es mas reciente que la de la cafci -> uso la manual
            if manual_cotiz['fecha_cotizacion_manual'] > cafci_dict['fecha_cotizacion']:
                cotiz_dict['fecha_cotizacion'] = manual_cotiz['fecha_cotizacion_manual']
                cotiz_dict['precio'] = float(manual_cotiz['vcp_provisorio'])
                cotiz_dict['fuente'] = 'Manual'
            #si la cotizacion manual es mas vieja que la de la cafci -> uso la de la cafci
            else:
                cotiz_dict['fecha_cotizacion'] = cafci_dict['fecha_cotizacion']
                cotiz_dict['precio'] = float(cafci_dict['vcpUnitario'])
                cotiz_dict['fuente'] = 'CAFCI'
        #si la cotizacion manual no es None y la cotizacion de la cafci es None -> busco en el WS de HG
        #si la cotizacion manual es mas reciente que la de HG -> uso la manual
        elif cafci_dict is None and manual_cotiz['fecha_cotizacion_manual'] > hg_dict[codigo_fci]['fecha_cotizacion']:
            cotiz_dict['fecha_cotizacion'] = manual_cotiz['fecha_cotizacion_manual']
            cotiz_dict['precio'] = float(manual_cotiz['vcp_provisorio'])
            cotiz_dict['fuente'] = 'Manual'
        #si la cotizacion manual es mas vieja que la de HG -> uso la de HG
        else:
            cotiz_dict['fecha_cotizacion'] = hg_dict[codigo_fci]['fecha_cotizacion']
            cotiz_dict['precio'] = hg_dict[codigo_fci]['cotizacion']
            cotiz_dict['fuente'] = 'HG'
    #si la cotizacion manual es None y la cotizacion de la cafci no es None -> uso la de la cafci
    elif cafci_dict is not None:
        cotiz_dict['fecha_cotizacion'] = cafci_dict['fecha_cotizacion']
        cotiz_dict['precio'] = float(cafci_dict['vcpUnitario'])
        cotiz_dict['fuente'] = 'CAFCI'
    #si la cotizacion manual es None y la cotizacion de la cafci es None -> busco en el WS de HG
    else:
        cotiz_dict['fecha_cotizacion'] = hg_dict['fecha_cotizacion']
        cotiz_dict['precio'] = hg_dict[codigo_fci]['cotizacion']
        cotiz_dict['fuente'] = 'HG'
    return cotiz_dict


def crearDistri(cotiz_dict):
    if cotiz_dict != None:
        ret = "<table class=\"tg\">"
        ret += (
            "<tr>"
                "<th class=\"tg-0lax center bold gray\">Fuente</th>"
                "<th class=\"tg-0lax center bold gray\">Fecha cotización</th>"
                "<th class=\"tg-0lax center bold gray\">Cotización CP</th>"
            "</tr>"
                )

        ret += (f"<tr>"
                f"<td class=\"tg-0lax center\">{cotiz_dict['fuente']}</td>"
                f"<td class=\"tg-0lax center\">{cotiz_dict['fecha_cotizacion'].strftime('%d/%m/%Y %H:%M:%S')}</td>"
                f"<td class=\"tg-0lax center\">{cotiz_dict['moneda_fondo']} {cotiz_dict['precio']}</td>"
                f"</tr>")
        ret += "</table>"
        return ret

if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    #todo: comment the following outside local tests
    # get_backtesting_redemption_data(bpm)
    calcular_solicitar_string = ""
    array_solicitudes_pendientes = bpm.context['array_solicitudes_pendientes']

    for solicitud in array_solicitudes_pendientes:
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

        # if monto is not None and absolute value of the diference is less than 0.000001 (bc quantity is truncated to 6 decimal places
        elif monto is not None and (cantidad_importe is None or abs(cantidad_importe - monto/cotiz_dict['precio']) < 0.000001):
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

    print(f"ARRAY SOLICITUD PENDIENTE: \n{array_solicitudes_pendientes}")

    bpm.context.input['array_solicitudes_pendientes'] = array_solicitudes_pendientes
    bpm.context.input['calcular_solicitar_string'] = calcular_solicitar_string



