#!python3
import json
import pandas as pd
import redflagbpm
from redflagbpm import PgUtils
import psycopg2
import psycopg2.extras
import tempfile
import os


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

def main():
    bpm = redflagbpm.BPMService()
    saldomav = bpm.context['saldomav']
    cobra = qry[0]['cobra']
    paga = qry[0]['paga']
    total = saldomav-cobra+paga

    html = f"""< table >
    < thead >
    < tr >
    < th > SALDO
    MAV < / th >
    < th > COBRAMOS / PAGAMOS < / th >

    < / tr >
    < / thead >
    < tbody >
    < tr >
    < td > {cobra} < / td >
    < td > {paga} < / td >
    < / tr >
    < / tbody >
    < / table >
    """
    bpm.reply(html)