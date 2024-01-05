#!python3
import json
import redflagbpm
import psycopg2
import psycopg2.extras
from redflagbpm import PgUtils

from DB import _get_hg_connection
import datetime
from decimal import Decimal
def get_solicitudes(bpm, conn, tipo_solicitud):
    # me conecto a la DB remota
    dblink = PgUtils.get_dblink(bpm, "SYC")
    sql_connect = "SELECT dblink_connect_u('hg_fci_tareas', %s)"
    sql_disconnect = "SELECT dblink_disconnect('hg_fci_tareas')"

    conn = _get_hg_connection(bpm)

    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    cur.execute(sql_connect, (dblink,))

    sql = """    
            with hg as(
                  select *
                  from dblink('hg_fci_tareas',
                  $$
                            with solicitudes as (
                            select 
                                t."IRM_TAREA_ID" as "id_origen",
                                (REGEXP_MATCHES(t."CLASS", '(Rescate)', 'g'))[1] AS tipo_solicitud,
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
                                (REGEXP_MATCHES(t."CLASS", '(Suscripcion)', 'g'))[1] AS tipo_solicitud,
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
                            select *,
                            null as template 
                            from solicitudes
                            where 
                             fecha = current_date
                            and lower(tipo_solicitud) = lower(%s)
                            order by 1 desc
                            limit 100
                  $$) as t(id_origen bigint, tipo_solicitud character varying, codigo_fci bigint, fci character varying, cuenta_id bigint,	
                           cuenta character varying, moneda character varying, estado character varying, fecha date, fecha_fin date,	 
                           cantidad decimal, VALORCUOTAPARTE decimal, cantidad_cuotapartes decimal, la_otra_cantidad decimal,  
                           propietario_tarea character varying, template character varying)
                ),
                bpm_base as (
                    select 
                        p.business_key_ as "businessKey",
                        p.start_time_ as "start",
                        p.end_time_ as "end",
                        p.start_user_id_ as "initiator",
                        coalesce(arr_pend.text_, convert_from(byte_pend.BYTES_, 'UTF8'))::jsonb ||
                        coalesce(arr_conf.text_, convert_from(byte_conf.BYTES_, 'UTF8'))::jsonb as array_pend_conf
                    from act_hi_procinst p 
                        inner join act_hi_varinst vini on p.proc_inst_id_ = vini.proc_inst_id_ and vini.name_ = 'initiator'
                        inner join act_hi_varinst arr_pend on p.proc_inst_id_ = arr_pend.proc_inst_id_ and arr_pend.name_ = 'array_solicitudes_pendientes'
                        left join ACT_GE_BYTEARRAY byte_pend ON arr_pend.BYTEARRAY_ID_ = byte_pend.ID_	
                        inner join act_hi_varinst arr_conf on p.proc_inst_id_ = arr_conf.proc_inst_id_ and arr_conf.name_ = 'array_solicitudes_confirmadas'
                        left join ACT_GE_BYTEARRAY byte_conf ON arr_pend.BYTEARRAY_ID_ = byte_conf.ID_
                    where business_key_ like 'INSTFCI%'
                ),
                bpm_explotada as (
                    select "businessKey", "start", "end", "initiator", 
                        sol#>>'{error}' as error,
                        sol#>>'{fondo}' as fondo,
                        (sol#>>'{monto}')::decimal as monto,
                        (sol#>>'{cantidad_importe}')::decimal as cantidad_importe,
                        (sol#>>'{precio}')::decimal as precio,
                        sol#>>'{moneda}' as moneda,
                        (sol#>>'{numero_solicitud}')::bigint as numero_solicitud
                    from bpm_base as bpm
                    cross join lateral jsonb_array_elements(bpm.array_pend_conf) as s (sol)
                )
                select
                (select 
                    STRING_AGG(participante, ', ') AS participante_list
                    from ds.participantes
                    where team = p.team)::character varying as team_members, *
                from bpm_explotada as bpm
                full join hg on bpm.numero_solicitud = hg.id_origen
                left join ds.participantes p on hg.propietario_tarea = p.participante
        """

    cur.execute(sql, (tipo_solicitud, ))
    qry = cur.fetchall()
    cur.execute(sql_disconnect)
    cur.close()
    conn.close()
    return qry

def main():
    bpm = redflagbpm.BPMService()
    conn = _get_hg_connection(bpm)
    qry = get_solicitudes(bpm=bpm, conn=conn, tipo_solicitud='Suscripcion')


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
