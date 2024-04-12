#!python3
import psycopg2, psycopg2.extras
import redflagbpm
from redflagbpm import PgUtils
import pandas as pd
from io import StringIO

bpm = redflagbpm.BPMService()


def _get_connection():
    # Manual connection, no config file
    conn = PgUtils.get_connection(bpm, 'FLW')
    conn.autocommit = True
    return conn


def limpiar_sql():
    print("estoy limpiando")
    conn = None
    sql_limpiar = """ delete from menu.menu """
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql_limpiar)
    return


# Con esta consulta me traigo datos  a utilizar en el pdf y en el endpoint
def consultar_usuarios():
    conn = None
    sql = """ select user_id_ from act_id_membership where group_id_ = 'MENU' """
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    return data


def create_csv(data):
    row = [item['user_id_'] for item in data]
    df = pd.DataFrame(row, columns=['nombre'])
    # Crear una lista de los días de la semana en español
    dias_semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']

    # Agregar las columnas con los días de la semana y valores vacíos
    for dia in dias_semana:
        df[dia] = ''
    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False, sep=';')
    buffer.seek(0)
    #df.to_csv('/tmp/menu.csv') otra opcion
    return buffer, tuple(df.columns)


def crear_tabla_menu(archivo, columnas):
    conn = None
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    try:
        cur.execute('SET search_path TO menu')
        cur.copy_from(archivo, 'menu', sep=';',
                      columns=(columnas))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error : %s " % error)
        conn.rollback()
        cur.close()
        return 1
    cur.close()
    conn.close()


def main():
    limpiar_sql()
    data = consultar_usuarios()
    buffer, columnas = create_csv(data)
    crear_tabla_menu(buffer, columnas)

if __name__ == "__main__":
    main()
