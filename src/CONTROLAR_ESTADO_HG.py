#!python3
# -*- coding: utf-8 -*-
import redflagbpm
import psycopg2
import psycopg2.extras
from redflagbpm import PgUtils
from SCRIPT_QRY_STATUS_SOLICITUDES import *
from DB import _get_hg_connection, _get_connection

def consultar_estado_solicitud(bpm, conn, cuenta_id, fondo_id, tipo_solicitud_bpm):
    # me conecto a la DB remota
    dblink = PgUtils.get_dblink(bpm, "SYC")
    conn = _get_connection(bpm)
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    sql = """
            with hg as(
                select *
                from dblink(%s,
                $$
                with solicitudes as (
                select 
                    t."IRM_TAREA_ID" as "id_origen",
                    'Rescate' AS tipo_solicitud,
                    unf."CODIGO"::bigint as codigo_fci,
                    '[' ||unf."CODIGO" ||'] ' || unf."NOMBRE" as fci,
                    c."ID"::bigint as cuenta_id,
                    '[' || c."ID" ||'] ' || c."DENOMINACION" as cuenta, 
                    uni."CODIGO" as moneda,
                    t."ESTADO" as estado, 
                    "FECHA"::date as fecha, 
                    "FECHAFIN"::date as fecha_fin, 
                    t."CANTIDAD"::decimal as cantidad,
                    t."VALORCUOTAPARTE", 
                    "CANTIDADSOLICITUD"::decimal as cantidad_cuotapartes, 
                    t."CANTIDADCUOTAPARTES" as la_otra_cantidad,
                    u."NOMBRE" as propietario_tarea
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
                    where t."CLASS" = 'com.aunesa.irmo.model.acdi.ISolicitudRescateFCI'
                        -- Filtro fondos cuyo codigo sea numérico
                        and unf."CODIGO" ~'^[0-9\\.]+$'
                union
                select 
                    t."IRM_TAREA_ID" as "id_origen",
                    'Suscripcion' AS tipo_solicitud,
                    unf."CODIGO"::bigint as codigo_fci,
                    '[' ||unf."CODIGO" ||'] ' || unf."NOMBRE" as fci,
                    c."ID"::bigint as cuenta_id,
                    '[' || c."ID" ||'] ' || c."DENOMINACION" as cuenta, 
                    uni."CODIGO" as moneda,
                    t."ESTADO" as estado, 
                    "FECHA"::date as fecha, 
                    "FECHAFIN"::date as fecha_fin, 
                    t."CANTIDAD"::decimal as cantidad,
                    t."VALORCUOTAPARTE", 
                    t."CANTIDADCUOTAPARTES"::decimal as cantidad_cuotapartes,
                    "CANTIDADSOLICITUD" as la_otra_cantidad, 
                    u."NOMBRE" as propietario_tarea
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
                    
                )
                select *
                from solicitudes
                where 
                 fecha = current_date
                order by 1 desc
                $$) as t(id_origen bigint, tipo_solicitud character varying, codigo_fci bigint, fci character varying, cuenta_id bigint,	
                       cuenta character varying, moneda character varying, estado character varying, fecha date, fecha_fin date,	 
                       cantidad decimal, VALORCUOTAPARTE decimal, cantidad_cuotapartes decimal, la_otra_cantidad decimal,  
                       propietario_tarea character varying))
            select *
            from hg
            where estado = 'Pendiente'
            and lower(tipo_solicitud) = %s
            and codigo_fci = %s
            and cuenta_id = %s 
        """
    cur.execute(sql, (dblink, tipo_solicitud_bpm, fondo_id, cuenta_id))
    qry = cur.fetchall()
    cur.close()
    conn.close()
    return qry

def main():
    bpm = redflagbpm.BPMService()


    cuenta = bpm.context['cuenta']
    fondo_id = bpm.context['fondo_id']
    tipo_solicitud_bpm = bpm.context['tipo_solicitud_bpm']
    qry = consultar_estado_solicitud(bpm=bpm, conn=None, cuenta_id='5004543', fondo_id='14209', tipo_solicitud_bpm='suscripcion')
    print(qry)
    if len(qry) != 0:
        reintentar = False
    else:
        reintentar = True
if __name__ == '__main__':
    main()


