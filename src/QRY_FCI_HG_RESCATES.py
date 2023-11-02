#!python3
import json
import redflagbpm
import psycopg2
import psycopg2.extras
from DB_connect import _get_flw_connection
import datetime

def get_stdr_rescates(conn, plazo_liq):
    sql_connect = "SELECT dblink_connect_u('hg_fci', 'dbname=syc user=consyc password=MTU1NDNjN2ZlZGU4ZDdhNDBhZTM2MjA2')"
    sql_disconnect = "SELECT dblink_disconnect('hg_fci')"
    conn.autocommit = True
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql_connect)

    sql = """    
            with hg as (
                select *
                from dblink('hg_fci',
                    'with resc_fci as (
                        select 
                            t."IRM_TAREA_ID" as "idOrigen",
                            unf."CODIGO"::bigint as codigo_fci,
                            ''['' ||unf."CODIGO" ||''] '' || unf."NOMBRE" as fci,
                            p."ID" as cuit,
                            c."ID"::bigint as cuenta_id,
                            ''['' || c."ID" ||''] '' || c."DENOMINACION" as cuenta, 
                            cfci."ID" as cuenta_fci,
                            uni."CODIGO" as moneda,
                            unf."CBUPESOS",
                            unf."CBUDOLARES",
                            t."DINERO",
                            (case when t."DINERO" then ''Monto'' else ''Cuotapartes'' end) as tipo_rescate,
                            unf."PLAZOLIQUDACIONRESCATE" as plazo_liq,
                            cm."CODIGO" as mkt,
                            chro."CODIGO" as "T+0",
                            chr."CODIGO" as "T++",
                            t."ESTADO", 
                            "FECHA"::date, 
                            "FECHAFIN"::date, 
                            "PROPIETARIO",
                            t."TIPO", "SOLICITUD",
                            t."CANTIDAD" as cantidad,
                            t."VALORCUOTAPARTE", 
                            t."CANTIDADCUOTAPARTES",
                            "CANTIDADSOLICITUD"::double precision as cantidad_cuotapartes, 
                            "UNIDAD", "FECHASOLICITUD",
                            "INTEGRACOMITENTE", 
                            unf."ACPIC", p."DENOMINACION" as banco,
                            null as template
                        from "IRM_TAREA" t
                            inner join "CTA_ESQUEMA" c on c."CTA_ESQUEMA_ID"  = t."CUENTA"
                            inner join "SEC_USUARIO" u on u."SEC_USUARIO_ID" = t."PROPIETARIO"
                            inner join "UNI_UNIDAD" unf on unf."UNI_UNIDAD_ID"=t."FCI" 
                            inner join "GNT_PERSONA" p on p."GNT_PERSONA_ID" = unf."ACPIC"
                            left join "CTA_CODIGO_INTEGRACION" cm on unf."CUENTAAAPIC"=cm."ESQUEMA" and cm."CODIFICACION"=''Modo operativo FCI''
                            left join "CTA_CODIGO_INTEGRACION" chro on unf."CUENTAAAPIC"=chro."ESQUEMA" and chro."CODIFICACION"=''Límite presentación rescate FCI T+0''
                            left join "CTA_CODIGO_INTEGRACION" chr on unf."CUENTAAAPIC"=chr."ESQUEMA" and chr."CODIFICACION"=''Límite presentación rescate FCI T++''
                            left join "CTA_CODIGO_INTEGRACION" chs on unf."CUENTAAAPIC"=chs."ESQUEMA" and chs."CODIFICACION"=''Límite presentación suscripción FCI''
                            left join "CTA_ESQUEMA" cfci on cfci."CTA_ESQUEMA_ID" = unf."CUENTAAAPIC"
                            inner join "UNI_UNIDAD" uni on uni."UNI_UNIDAD_ID"=unf."MONEDA"
                        where t."CLASS" = ''com.aunesa.irmo.model.acdi.ISolicitudRescateFCI''
                            and t."ESTADO" = ''Liquidación pendiente''
                            and (unf."PLAZOLIQUDACIONRESCATE" = 0) = ('%s'= ''T+0'')
                            and "FECHA"::date = current_date
                            -- Filtro la familia santander
                            -- and cfci."ID" like ''%%SANTANDER RIO ASSET%%''
                            order by 1
                        )
                    select * from resc_fci')as f("idOrigen" bigint, codigo_fci bigint, fci character varying, 
                        cuit character varying, cuenta_id bigint, cuenta character varying, cuenta_fci character varying, 
                        moneda character varying, cbu_pesos character varying, cbu_dolares character varying, 
                        dinero boolean, tipo_rescate character varying, plazo_liq integer, mkt character varying, 
                        "T+0" character varying, "T++" character varying, estado character varying, fecha date, 
                        fechafin date, propietario bigint, tipo character varying, solicitud character varying, 
                        cantidad double precision, valorcuotaparte double precision, cantidadcuotapartes double precision, 
                        cantidad_cuotapartes double precision, unidad bigint, fechasolicitud date, integracomitente boolean,
                         acpic bigint, banco character varying, template character varying))
            select * 
            from hg 
                -- Joineo con la tabla de rescates stdr por idOrigen para filtrar los ya procesados
                left join fcistdr.rescate_status st_rs on hg."idOrigen" = st_rs.id_origen
            where (st_rs.estado is null or st_rs.estado != 'CONFIRMADO')
        """

    cur.execute(sql, (plazo_liq,))
    qry = cur.fetchall()
    cur.execute(sql_disconnect)
    cur.close()
    conn.close()
    return qry

def main():
    bpm = redflagbpm.BPMService()
    if bpm.service.text("STAGE") == "DEV":
        conn = _get_flw_connection('flowabletest')
    else:
        conn = _get_flw_connection('flowable')
    qry = get_stdr_rescates(conn, bpm.context['plazo_liq'])
    print(qry)
    class DateEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()
            return super().default(obj)

    qry = json.dumps(qry, cls=DateEncoder)
    qry = json.loads(qry)
    with open('/tmp/qry_rescates.json', 'w') as f:
        json.dump(qry, f)

    _responseHeaders = bpm.context.json._responseHeaders
    _responseHeaders['status'] = '200'
    _responseHeaders['Content-Type'] = 'application/json'
    _responseHeaders["Content-Encoding"] = "UTF-8"
    _responseHeaders["resource"] = "/tmp/qry_rescates.json"

if __name__ == '__main__':
    main()
