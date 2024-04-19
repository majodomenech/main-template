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

    SET  column1 = value1, column2 = value2
    sql_actualizar1 = """
                        update colocadoras_fci.cauciones
            set """ + bpm.context['dia'] + " = %s"
    sql_actualizar2 = """
            where nombre = %s   
                    """
    sql_actualizar = sql_actualizar1 + sql_actualizar2
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql_actualizar, context)
    return

    menu = especificar_menu()
    context = (menu, bpm.context['usuario'],)
    actualizar(context)

    # Cabeceras de la respuesta
    print('Modificación exitosa')
    bpm.reply({"type": "TERMINAL_UPDATE"})
    bpm.context.setJsonValue("_responseHeaders", "content-type", "txt/html")
    bpm.context.setJsonValue("_responseHeaders", "status", "200")
