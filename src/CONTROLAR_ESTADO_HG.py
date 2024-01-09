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
                                'Rescate' AS tipo_solicitud,
                                unf."CODIGO"::bigint as codigo_fci,
                                c."ID"::bigint as cuenta_id,
                                t."ESTADO" as estado
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
                                    and unf."CODIGO" ~'^[0-9\.]+$'
                            union
                            select 
                                'Suscripcion' AS tipo_solicitud,
                                unf."CODIGO"::bigint as codigo_fci,
                                c."ID"::bigint as cuenta_id,
                                t."ESTADO" as estado
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
                                and unf."CODIGO" ~'^[0-9\.]+$'
                                
                            )
                            select *
                            from solicitudes
                  $$) as t(tipo_solicitud character varying, codigo_fci bigint, cuenta_id bigint,	
                           estado character varying)
                )
				select estado
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

    cuenta_id = bpm.context['cuenta_id']
    fondo_id = bpm.context['fondo_id']
    tipo_solicitud_bpm = bpm.context['tipo_solicitud_bpm']

    qry = consultar_estado_solicitud(bpm=bpm, conn=None, cuenta_id=cuenta_id, fondo_id=fondo_id, tipo_solicitud_bpm=tipo_solicitud_bpm)
    print(qry)
    if len(qry) != 0:
        estado_hg_pendiente = True
    else:
        estado_hg_pendiente = False
if __name__ == '__main__':
    main()


