#!python3
import json
import pandas as pd
import redflagbpm
from redflagbpm import PgUtils
import psycopg2
import psycopg2.extras
import tempfile
import os
import re

def _get_connection():
    bpm = redflagbpm.BPMService()
    # Manual connection, no config file
    conn = PgUtils.get_connection(bpm, 'FLW')
    conn.autocommit = True
    return conn


def qry_totales(conn):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    sql = """    
     select sum(cobra) as cobra, sum(paga) as paga
     from colocadoras_fci.cauciones
      """

    cur.execute(sql, )
    qry = cur.fetchall()
    cur.close()
    conn.close()
    return qry


def format_number(number):
    # Convert the number to a string
    number_str = str(number)

    # Add decimal separator
    if '.' in number_str:
        integer_part, decimal_part = number_str.split('.')
        number_str = f"{integer_part},{decimal_part.replace('.', ',')}"

    # Add thousands separator
    number_str = re.sub(r"\B(?=(\d{3})+(?!\d))", ".", number_str)

    return number_str

def main():
    bpm = redflagbpm.BPMService()
    conn = _get_connection()
    qry = qry_totales(conn)
    saldomav = bpm.context['saldomav']
    cobra = qry[0]['cobra']
    paga = qry[0]['paga']
    total = saldomav-cobra+paga
    saldomav = format_number(saldomav)
    total = format_number(total)

    style = '''
        <style type="text/css">
    .tg  {border-collapse:collapse;border-spacing:0;margin:0px auto;}
    .tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
      overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
      font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
    .tg .tg-7lt1{background-color:#96fffb;border-color:#343434;font-weight:bold;text-align:right;vertical-align:top}
    .tg .tg-u8ng{border-color:#343434;font-weight:bold;text-align:center;vertical-align:top}
    .tg .tg-554n{background-color:#fcff2f;border-color:#343434;font-weight:bold;text-align:right;vertical-align:bottom}
    </style>'''.strip()

    body = f"""<table class="tg">
        <tbody>
          <tr>
            <td class="tg-u8ng">SALDO MAV</td>
            <td class="tg-u8ng">COBRAMOS/PAGAMOS</td>
          </tr>
          <tr>
            <td class="tg-554n"><span style="font-weight:400;font-style:normal">{saldomav}</span></td>
            <td class="tg-7lt1">{total}</td>
          </tr>
        </tbody>
        </table>
            """.strip()
    html = style + body
    html = html.strip()


    bpm.reply(html)

main()