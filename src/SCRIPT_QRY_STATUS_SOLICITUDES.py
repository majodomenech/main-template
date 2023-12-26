#!python3
import json
import redflagbpm
import psycopg2
import psycopg2.extras
from redflagbpm import PgUtils

from DB import _get_hg_connection
import datetime
from decimal import Decimal
def get_solicitudes(bpm, tipo_solicitud):
    conn = _get_hg_connection(bpm)

    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    sql = """    
            with solicitudes as (
            select 
                t."IRM_TAREA_ID" as "idOrigen",
                unf."CODIGO"::bigint as codigo_fci,
                '[' ||unf."CODIGO" ||'] ' || unf."NOMBRE" as fci,
                fid."VALOR" as fund_id,
                p."ID" as cuit,
                c."ID"::bigint as cuenta_id,
                '[' || c."ID" ||'] ' || c."DENOMINACION" as cuenta, 
                cfci."ID" as cuenta_fci,
                uni."CODIGO" as moneda,
                case when uni."CODIGO"  = 'ARS'
                then unf."CBUPESOS"
                when uni."CODIGO"  = 'USD' then unf."CBUDOLARES"
                end as cbu,
                t."DINERO",
                (case when t."DINERO" then 'Monto' else 'Cuotapartes' end) as tipo_rescate,
                (case when t."DINERO" then uni."CODIGO" else '[' ||unf."CODIGO" ||'] ' || unf."NOMBRE" end) as especie_moneda,
                unf."PLAZOLIQUDACIONRESCATE" as plazo_liq,
                cm."CODIGO" as mkt,
                chro."CODIGO" as "T+0",
                chr."CODIGO" as "T++",
                t."ESTADO", 
                "FECHA"::date, 
                "FECHAFIN"::date, 
                "PROPIETARIO",
                t."TIPO", 
                "SOLICITUD",
                t."CANTIDAD"::double precision as cantidad,
                t."VALORCUOTAPARTE", 
                "CANTIDADSOLICITUD"::double precision as cantidad_cuotapartes, 
                t."CANTIDADCUOTAPARTES" as la_otra_cantidad,
                t."UNIDAD", "FECHASOLICITUD",
                "INTEGRACOMITENTE", 
                unf."ACPIC", p."DENOMINACION" as banco, 
                u."NOMBRE", 
                "EMAIL", 
                "NOMBREREAL",
                t."CLASS" as tipo_solicitud
            from "IRM_TAREA" t
                inner join "CTA_ESQUEMA" c on c."CTA_ESQUEMA_ID"  = t."CUENTA"
                inner join "SEC_USUARIO" u on u."SEC_USUARIO_ID" = t."PROPIETARIO"
                inner join "UNI_UNIDAD" unf on unf."UNI_UNIDAD_ID"=t."FCI" 
                inner join "GNT_PERSONA" p on p."GNT_PERSONA_ID" = unf."ACPIC"
                left join "CTA_CODIGO_INTEGRACION" cm on unf."CUENTAAAPIC"=cm."ESQUEMA" and cm."CODIFICACION"='Modo operativo FCI'
                left join "CTA_CODIGO_INTEGRACION" chro on unf."CUENTAAAPIC"=chro."ESQUEMA" and chro."CODIFICACION"='Límite presentación rescate FCI T+0'
                left join "CTA_CODIGO_INTEGRACION" chr on unf."CUENTAAAPIC"=chr."ESQUEMA" and chr."CODIFICACION"='Límite presentación rescate FCI T++'
                left join "CTA_CODIGO_INTEGRACION" chs on unf."CUENTAAAPIC"=chs."ESQUEMA" and chs."CODIFICACION"='Límite presentación suscripción FCI'
                left join "CTA_ESQUEMA" cfci on cfci."CTA_ESQUEMA_ID" = unf."CUENTAAAPIC"
                inner join "UNI_UNIDAD" uni on uni."UNI_UNIDAD_ID"=unf."MONEDA"
                left join "UNI_ATRIBUTO" fid on fid."UNIDAD"=t."FCI" and fid."ATRIBUTO"='FundId Santander'
                where t."CLASS" = 'com.aunesa.irmo.model.acdi.ISolicitudRescateFCI'
            -- 		and t."ESTADO" = 'Liquidación pendiente'
                --  and (unf."PLAZOLIQUDACIONRESCATE" = 0) = ('T+0'= 'T+0')
                    and "FECHA"::date = current_date
                    -- Filtro la familia santander
                    and unf."CODIGO" ~'^[0-9\\.]+$'
            --     order by 1
            union
            select 
                t."IRM_TAREA_ID" as "idOrigen",
                unf."CODIGO"::bigint as codigo_fci,
                '[' ||unf."CODIGO" ||'] ' || unf."NOMBRE" as fci,
                null as fund_id,
                p."ID" as cuit,
                c."ID"::bigint as cuenta_id,
                '[' || c."ID" ||'] ' || c."DENOMINACION" as cuenta, 
                cfci."ID" as cuenta_fci,
                uni."CODIGO" as moneda,
                case when uni."CODIGO"  = 'ARS'
                then unf."CBUPESOS"
                when uni."CODIGO"  = 'USD' then unf."CBUDOLARES"
                end as cbu,
                t."DINERO",
                null as tipo_rescate,
                null as especie_moneda,
                null as plazo_liq,
                cm."CODIGO" as mkt,
                chro."CODIGO" as "T+0",
                chr."CODIGO" as "T++",
                t."ESTADO", 
                "FECHA"::date, 
                "FECHAFIN"::date,
                "PROPIETARIO",
                t."TIPO",
                "SOLICITUD",
                t."CANTIDAD"::double precision as cantidad,
                t."VALORCUOTAPARTE", 
                t."CANTIDADCUOTAPARTES"::double precision as cantidad_cuotapartes,
                "CANTIDADSOLICITUD" as la_otra_cantidad, 
                t."UNIDAD", "FECHASOLICITUD",
                "INTEGRACOMITENTE",
                unf."ACPIC", p."DENOMINACION" as banco,
                u."NOMBRE", 
                "EMAIL", 
                "NOMBREREAL",
                t."CLASS" as tipo_solicitud
            from "IRM_TAREA" t
                inner join "CTA_ESQUEMA" c on c."CTA_ESQUEMA_ID"  = t."CUENTA"
                inner join "SEC_USUARIO" u on u."SEC_USUARIO_ID" = t."PROPIETARIO"
                inner join "UNI_UNIDAD" unf on unf."UNI_UNIDAD_ID"=t."FCI" 
                inner join "GNT_PERSONA" p on p."GNT_PERSONA_ID" = unf."ACPIC"
                left join "CTA_CODIGO_INTEGRACION" cm on unf."CUENTAAAPIC"=cm."ESQUEMA" and cm."CODIFICACION"='Modo operativo FCI'
                left join "CTA_CODIGO_INTEGRACION" chro on unf."CUENTAAAPIC"=chro."ESQUEMA" and chro."CODIFICACION"='Límite presentación rescate FCI T+0'
                left join "CTA_CODIGO_INTEGRACION" chr on unf."CUENTAAAPIC"=chr."ESQUEMA" and chr."CODIFICACION"='Límite presentación rescate FCI T++'
                left join "CTA_CODIGO_INTEGRACION" chs on unf."CUENTAAAPIC"=chs."ESQUEMA" and chs."CODIFICACION"='Límite presentación suscripción FCI'
                left join "CTA_ESQUEMA" cfci on cfci."CTA_ESQUEMA_ID" = unf."CUENTAAAPIC"
                inner join "UNI_UNIDAD" uni on uni."UNI_UNIDAD_ID"=t."UNIDAD"
            where t."CLASS" = 'com.aunesa.irmo.model.acdi.ISolicitudSuscripcionFCI'
                and unf."CODIGO" ~'^[0-9\\.]+$'
            --     and t."ESTADO" = 'Pendiente'
                and t."FECHA"::date = current_date
            limit 100)
            select *,
            null as template 
            from solicitudes
            where 
            -- tipo_solicitud like '%Suscripcion%'
            tipo_solicitud like '%%s%'
            -- and "ESTADO" = 'Pendiente'
        """

    cur.execute(sql, (tipo_solicitud, ))
    qry = cur.fetchall()
    cur.close()
    conn.close()
    return qry

def main():
    bpm = redflagbpm.BPMService()
    conn = _get_hg_connection(bpm)
    qry = get_solicitudes(bpm, conn, tipo_solicitud=tipo_solicitud)


    print(qry)
    class Encoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (datetime.date, datetime.datetime)):
                return obj.isoformat()
            if isinstance(obj, Decimal):
                return float(obj)
            return super().default(obj)

    with open('/tmp/qry_solicitudes.json', 'w') as f:
        json.dump(qry, f, cls=Encoder)

    _responseHeaders = bpm.context.json._responseHeaders
    _responseHeaders['status'] = '200'
    _responseHeaders['Content-Type'] = 'application/json'
    _responseHeaders["Content-Encoding"] = "UTF-8"
    _responseHeaders["resource"] = "/tmp/qry_rescates.json"

if __name__ == '__main__':
    main()
