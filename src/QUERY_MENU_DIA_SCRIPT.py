#!python3
import psycopg2
import psycopg2.extras
import redflagbpm
import pandas as pd
from redflagbpm import PgUtils
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

bpm = redflagbpm.BPMService()


def _get_connection():
    # Manual connection, no config file
    conn = PgUtils.get_connection(bpm, 'FLW')
    conn.autocommit = True
    return conn


def consultar_pedidos_dia():

    dia = bpm.context['dia']

    sql_pos = """
            select CONCAT(first_, ' ', last_) as nombre,""" + dia + """
            from menu.menu m
            join act_id_user a
            on m.nombre = a.id_
            where """ + dia + """ != 'AUSENTE' and """ + dia + """!=''
            union all
            select CONCAT(first_, ' ', last_) as nombre,""" + dia + """
            from menu.menu m
            join act_id_user a 
            on m.nombre = a.id_
            where """ + dia + """ = 'AUSENTE' or """ + dia + """ = '' 
            """
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql_pos)
    data = cur.fetchall()
    cur.close()
    return pd.DataFrame(data)


def contar_pedidos():

    dia = bpm.context['dia']

    sql_pos = """   with pedidos as (select CONCAT(first_, ' ', last_) as nombre,""" + dia + """
                    from menu.menu m
                    join act_id_user a
                    on m.nombre = a.id_
                    where """ + dia + """ != 'AUSENTE' and """ + dia + """!=''
                    )
                    select count(*) as cantidad, """ + dia + """ as menu
                    from pedidos
                    group by 2
                """
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute(sql_pos)
    data = cur.fetchall()
    cur.close()
    return pd.DataFrame(data)


def generar_excel(df1, df2):
    # Create a new Excel workbook
    wb = Workbook()

    # Remove the default "Sheet"
    default_sheet = wb['Sheet']
    wb.remove(default_sheet)

    # Create a new sheet for each DataFrame
    ws1 = wb.create_sheet(title='Pedidos')
    ws2 = wb.create_sheet(title='Cantidades')

    # Write DataFrame values to respective sheets
    for row in dataframe_to_rows(df1, index=False, header=True):
        ws1.append(row)

    for row in dataframe_to_rows(df2, index=False, header=True):
        ws2.append(row)

    # Save the workbook to a file
    wb.save('/tmp/Pedidos.xlsx')

# Write DataFrame values to respective sheets with formatting


def main():
    df_pedidos = consultar_pedidos_dia()
    df_pedidos.columns = ['nombre', 'menu']

    df_cantidades = contar_pedidos()
    df_cantidades.columns = ['cantidad', 'menu']

    generar_excel(df_pedidos, df_cantidades)


main()
bpm.context.setJsonValue("_responseHeaders", "content-type", "application/vnd.ms-excel")
bpm.context.setJsonValue("_responseHeaders", "resource", "/tmp/Pedidos.xlsx")
