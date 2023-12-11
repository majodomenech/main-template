#!python3
import redflagbpm
import psycopg2
import psycopg2.extras


def _get_hg_connection(DB):
    #Manual connection, no config file
    conn = psycopg2.connect(database=DB,
                        user="consyc",
                        password="MTU1NDNjN2ZlZGU4ZDdhNDBhZTM2MjA2",
                        host="db.sycinversiones.com",
                        port="5432")
    conn.autocommit=True
    return conn

def get_caption(cuenta_id):
    conn = _get_hg_connection("syc")
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    sql = """
            with id_cliente_com_full as (
                select "ID" as id ,'['||"ID"||'] '||"DENOMINACION" as caption
                from "CTA_ESQUEMA"
                where "TIPO" in ('Comitente','Comitente vinculado','Propia')
                union
                select c."CODIGO" as id ,'['||c."CODIGO"||'] '||e."DENOMINACION" as caption
                from "CTA_ESQUEMA" e
                    inner join "CTA_CODIGO_INTEGRACION" c ON c."ESQUEMA" = e."CTA_ESQUEMA_ID"
                where "TIPO" in ('Comitente','Comitente vinculado','Propia','Prospecto')
                    and c."CODIFICACION" in ('Pershing', 'Societe Generale'))
            select caption from id_cliente_com_full
            where id = %s
    """
    cur.execute(sql, (cuenta_id,))
    rows = cur.fetchone()
    return rows['caption']

if __name__ == "__main__":
    #initialize bpm service
    bpm = redflagbpm.BPMService()
    #get process instance id
    idProcessInstance = bpm.execution.getProcessInstanceId()
    #get variable from process instance
    cuenta_id = bpm.context['cuenta']
    cuenta_denominacion = get_caption(cuenta_id)

    bpm.execution.setVariable('cuenta_denominacion', cuenta_denominacion)
