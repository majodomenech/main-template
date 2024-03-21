import datetime
import psycopg2, psycopg2.extras
import redflagbpm
from redflagbpm import PgUtils
#bpm = redflagbpm.BPMService()
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
    sql = '''select nombre, ''' + dia + '''
from menu.menu
where ''' + dia + ''' = '' '''
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    return data

def main():
    dia = obtener_dia_de_la_semana()
    get_users_to_warn(dia)
