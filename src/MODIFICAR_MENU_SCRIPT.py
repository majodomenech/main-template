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
    sql_actualizar1 = """
                        update menu.menu
            set """ + bpm.context['dia'] + " = %s"
    sql_actualizar2 = """
            where nombre = %s   
                    """
    sql_actualizar = sql_actualizar1 + sql_actualizar2
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql_actualizar, context)
    return

def especificar_menu():
    if bpm.context['comentario'] is None:
        comentario = ''
    else:
        comentario = bpm.context['comentario']

    if bpm.context['menu2'] == 'Otro':
        menu = comentario
    elif comentario != '':
        menu = bpm.context['menu2'] + ' ' + comentario
    else:
        menu = bpm.context['menu2']
    return menu.strip()

if bpm.context['tipo'] == 'Usuario':

    menu = especificar_menu()
    context = (menu, bpm.context['usuario'],)
    actualizar(context)

    # Cabeceras de la respuesta
    print('Modificación exitosa')
    bpm.reply({"type": "TERMINAL_UPDATE"})
    bpm.context.setJsonValue("_responseHeaders", "content-type", "txt/html")
    bpm.context.setJsonValue("_responseHeaders", "status", "200")

else:
    print("La modificación debe hacerse desde la consulta usuario")
    bpm.context.setJsonValue("_responseHeaders", "content-type", "txt/html")
    bpm.context.setJsonValue("_responseHeaders", "status", "200")