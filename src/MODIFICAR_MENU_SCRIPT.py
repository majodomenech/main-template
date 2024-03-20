#!python3
import redflagbpm
import psycopg2, psycopg2.extras

from redflagbpm import PgUtils

bpm = redflagbpm.BPMService()


def _get_connection():
    conn = PgUtils.get_connection(bpm, 'FLW')
    conn.autocommit = True
    return conn


def actualizar(context):
    conn = None
    sql_actualizar = """
                    update menu.menu
        set  %s = %s
        where nombre = %s   
                """
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql_actualizar, context)
    return

context = (bpm.context['dia'], bpm.context['menu'], bpm.context['usuario'])

actualizar(context)