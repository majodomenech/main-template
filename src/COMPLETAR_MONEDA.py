#!python3
import psycopg2
import psucopg2.extras
import redflagbpm
def _get_hg_connection(DB):
    #Manual connection, no config file
    conn = psycopg2.connect(database=DB,
                        user="consyc",
                        password="MTU1NDNjN2ZlZGU4ZDdhNDBhZTM2MjA2",
                        host="db.sycinversiones.com",
                        port="5432")
    conn.autocommit = True
    return conn

def get_moneda_fondo(fondo):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    sql = """
        select mon."CODIGO"
        from "UNI_UNIDAD" fci
            inner join "UNI_UNIDAD" mon on mon."UNI_UNIDAD_ID" = fci."MONEDA"
        where fci."CODIGO"=%s
        """

    cur.execute(sql, (fondo, ))
    moneda = cur.fetchone()
    cur.close()
    conn.close()
    return moneda



if __name__ == '__main__':
    bpm = redflagbpm.BPMService()
    fondo = bpm.context.input['fondo']
    conn = _get_hg_connection('syc')
    moneda = get_moneda_fondo(fondo)

    #setear moneda en el form
    bpm.context.input["moneda"] = moneda


