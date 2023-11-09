#!python3
import json
import redflagbpm
import psycopg2
import psycopg2.extras
from DB_connect import _get_flw_connection
import datetime
from decimal import Decimal
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
                            fid."VALOR" as fund_id,
                            p."ID" as cuit,
                            c."ID"::bigint as cuenta_id,
                            ''['' || c."ID" ||''] '' || c."DENOMINACION" as cuenta, 
                            cfci."ID" as cuenta_fci,
                            uni."CODIGO" as moneda,
							case when uni."CODIGO"  = ''ARS''
                            then unf."CBUPESOS"
							when uni."CODIGO"  = ''USD'' then unf."CBUDOLARES"
							end as cbu,
                            t."DINERO",
                            (case when t."DINERO" then ''Monto'' else ''Cuotapartes'' end) as tipo_rescate,
                            (case when t."DINERO" then uni."CODIGO" else ''['' ||unf."CODIGO" ||''] '' || unf."NOMBRE" end) as especie_moneda,
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
                            t."UNIDAD", "FECHASOLICITUD",
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
                            left join "UNI_ATRIBUTO" fid on fid."UNIDAD"=t."FCI" and fid."ATRIBUTO"=''FundId Santander''
                        where t."CLASS" = ''com.aunesa.irmo.model.acdi.ISolicitudRescateFCI''
                            and t."ESTADO" = ''Liquidación pendiente''
                            and (unf."PLAZOLIQUDACIONRESCATE" = 0) = ('%s'= ''T+0'')
                            and "FECHA"::date = current_date
                            -- Filtro la familia santander
                            and cfci."ID" like ''%%SANTANDER RIO ASSET%%''
                            and unf."CODIGO" ~''^[0-9\\.]+$''
                            order by 1
                        )
                    select * from resc_fci')as f("idOrigen" bigint, codigo_fci bigint, fci character varying, fund_id bigint, 
                        cuit character varying, cuenta_id bigint, cuenta character varying, cuenta_fci character varying, 
                        moneda character varying, cbu character varying, 
                        dinero boolean, tipo_rescate character varying, especie_moneda character varying, 
                        plazo_liq integer, mkt character varying, 
                        "T+0" character varying, "T++" character varying, estado character varying, fecha date, 
                        fechafin date, propietario bigint, tipo character varying, solicitud character varying, 
                        cantidad double precision, valorcuotaparte double precision, cantidadcuotapartes double precision, 
                        cantidad_cuotapartes double precision, unidad bigint, fechasolicitud date, integracomitente boolean,
                         acpic bigint, banco character varying, template character varying))
            select * 
            from hg 
                -- Joineo con la tabla de rescates stdr por idOrigen para filtrar los ya procesados
                inner join fcistdr.rescate_status st_rs on hg."idOrigen" = st_rs.id_origen
            where (st_rs.estado is null or st_rs.estado != 'CONFIRMED')
            order by 1 desc
        """

    cur.execute(sql, (plazo_liq,))
    qry = cur.fetchall()
    cur.execute(sql_disconnect)
    cur.close()
    conn.close()
    return qry

def main():
    bpm = redflagbpm.BPMService()
    if bpm.service.text("STAGE") == 'DEV':
        conn = _get_flw_connection('flowabletest')
    else:
        conn = _get_flw_connection('flowable')
    qry = get_stdr_rescates(conn, bpm.context['plazo_liq'])


    print(qry)
    class Encoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()
            if isinstance(obj, Decimal):
                return float(obj)
            return super().default(obj)

    with open('/tmp/qry_rescates.json', 'w') as f:
        json.dump(qry, f, cls=Encoder)

    _responseHeaders = bpm.context.json._responseHeaders
    _responseHeaders['status'] = '200'
    _responseHeaders['Content-Type'] = 'application/json'
    _responseHeaders["Content-Encoding"] = "UTF-8"
    _responseHeaders["resource"] = "/tmp/qry_rescates.json"

if __name__ == '__main__':
    main()
