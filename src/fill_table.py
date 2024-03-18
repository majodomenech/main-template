#!python3
import psycopg2, psycopg2.extras
import redflagbpm
from redflagbpm import PgUtils

bpm = redflagbpm.BPMService()

def _get_connection():
    # Manual connection, no config file
    conn = PgUtils.get_connection(bpm, 'FLW')
    conn.autocommit = True
    return conn

def limpiar_sql():
    print("estoy limpiando")
    conn = None
    sql_limpiar = """
                    delete from ds.especies
                """
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql_limpiar)
    return

# Con esta consulta me traigo datos  a utilizar en el pdf y en el endpoint
def consultar_usuarios():
    conn = None
    sql = """
       select * from act_id_membership where group_id_ = 'MENU'
        """
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    return data

def create_table(data):
    row = [item[0] for item in data]
    print(row)
    df = pd.DataFrame(data, columns=['Nombre'])
    # Crear una lista de los días de la semana en español
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    # Agregar las columnas con los días de la semana y valores vacíos
    for dia in dias_semana:
        df[dia] = ''
    print(df)
    df.to_csv('menu_semanal.csv', index=False)
    return df.columns
def completar_base(archivo, columnas):
    conn = None
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    try:
        cur.execute('SET search_path TO menu')
        cur.copy_from(archivo, 'menu', sep=',',
                      columns=(columnas)
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error : %s " % error)
        conn.rollback()
        cur.close()
        return 1
    cur.close()
    conn.close()

def main():
    data = consultar_usuarios()
    columnas = create_table(data)
    completar_base('menu_semanal,csv', columnas)