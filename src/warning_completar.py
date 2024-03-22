#!python3
import datetime
import psycopg2
import psycopg2.extras
import redflagbpm
from redflagbpm import PgUtils

bpm = redflagbpm.BPMService()


def obtener_dia_de_la_semana():
    dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    hoy = datetime.datetime.today().weekday()
    return dias_semana[hoy]


def _get_connection():
    # Manual connection, no config file
    conn = PgUtils.get_connection(bpm, 'FLW')
    conn.autocommit = True
    return conn


def get_users_to_warn(dia):
    conn = None
    sql =   '''
            select nombre, ''' + dia + '''
            from menu.menu
            where ''' + dia + ''' = ''
            '''
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    users = [item['nombre'] for item in data]
    return users


def warn_user(user):
    bpm.service.notifyUser(user, title="Completar comida!", description="Si no completás la comida no comesssss",
                           sound=True)


def warn_all_users(users):
    for user in users:
        warn_user(user)


def main():
    dia = obtener_dia_de_la_semana()
    users = get_users_to_warn(dia)
    warn_all_users(users)


main()
