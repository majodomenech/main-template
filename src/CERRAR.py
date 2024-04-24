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
    cerrada = bpm.context['cerrada2']

    sql_actualizar = """
                        update colocadoras_fci.cauciones
                        set  cerrada = %s
                        where cuenta = %s
                      """

    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql_actualizar, (cerrada, cuenta,))
    return


actualizar()

# Cabeceras de la respuesta
print('Modificación exitosa')
bpm.reply({"type": "TERMINAL_UPDATE"})

