#!python3
import redflagbpm
import psycopg2, psycopg2.extras

from redflagbpm import PgUtils

bpm = redflagbpm.BPMService()

def _get_connection():
    conn = PgUtils.get_connection(bpm, 'FLW')
    conn.autocommit = True
    return conn


def actualizar():
    conn = None
    cuenta = bpm.context['cuenta']
    monto = bpm.context['monto']
    if bpm.context['operado2'] is None:
        operado = bpm.context['operado']
    else:
        operado = bpm.context['operado2']

    if operado > monto:
        paga = operado - monto
        cobra = 0
    elif operado < monto:
        paga = 0
        cobra = monto - operado
    else:
        paga = 0
        cobra = 0

    sql_actualizar = """
                        update colocadoras_fci.cauciones
                        set  operado = %s, cobra = %s, paga = %s
                        where cuenta = %s
                      """

    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql_actualizar, (operado,cobra,paga,cuenta,))
    return


actualizar()

# Cabeceras de la respuesta
print('Modificación exitosa')
bpm.reply({"type": "TERMINAL_UPDATE"})

