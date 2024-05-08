#!python3
import psycopg2, psycopg2.extras
import redflagbpm
from redflagbpm import PgUtils
import pandas as pd
from io import StringIO

bpm = redflagbpm.BPMService()


def _get_connection(SOURCE):
    # Manual connection, no config file
    conn = PgUtils.get_connection(bpm, SOURCE)
    conn.autocommit = True
    return conn


def limpiar_sql():
    print("estoy limpiando")
    conn = None
    sql_limpiar = """ delete from colocadoras_fci.cauciones """
    conn = PgUtils.get_connection(bpm, 'FLW')
    conn.autocommit = True
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql_limpiar)
    return


# Con esta consulta me traigo datos  a utilizar en el pdf y en el endpoint
def consultar_cauciones():
    conn = None
    sql = """ 
     with almost as (select 
    esq."DENOMINACION" as fondo,
    esq."ID" as cuenta,
    CASE 
          WHEN op."MONEDA"=1 THEN 'ARS'
          ELSE 'USD'
    END AS moneda,
    -- REPLACE(REPLACE(REPLACE(to_char(mov."CANTIDAD", '999,999,999,999,999,999.99'::text), ',', '*'), '.', ','),'*','.') AS monto
    mov."CANTIDAD" AS monto
    from "OP_COMPROBANTE" com 
    join "OP_OPERACION" op
    on com."OPERACION" = op."OP_OPERACION_ID"
    right join
    "CTA_ESQUEMA" esq
    ON op."CUENTA"=esq."CTA_ESQUEMA_ID"
    and esq."CARTERA"=158 --solo fci
    JOIN "OP_MOVIMIENTO" mov
    on esq."CTA_ESQUEMA_ID" = mov."CUENTA" AND mov."CONCEPTO"='F' and com."REFERENCIA" = mov."COMPROBANTE" 
    where "PARTE"='Colocadora' --solo cauciones
    AND "SESION"='Caución'
    AND op."ESTADO" !='ANULADA'
    AND com."CONCEPTO" = 'Concurrencia - Caución colocadora (Cierre)'
    and "VENCIMIENTO" = CURRENT_DATE
    and op."RESUMEN" LIKE '%MAV%'),
final as (select fondo, cuenta, moneda, sum(monto) as monto
from almost
group by 1, 2, 3),
sin_vencimiento as(
select
esq."DENOMINACION" as fondo,
esq."ID" as cuenta,
'' as moneda,
0 as monto
from "CTA_ESQUEMA" esq
where esq."CARTERA"=158
and esq."ID" not in (select cuenta from almost) 
order by 1),
casi as (
select *
from final
union all
select *
from
sin_vencimiento)
select *,
monto as cobra
from casi
     """
    conn = _get_connection('SYC')
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    return data


def create_csv(data):
    df = pd.DataFrame(data)
    # Crear una lista de los días de la semana en español
    columnas = ['cerrada', 'boletos', 'derivacion']

    # Agregar las columnas con los días de la semana y valores vacíos
    for columna in columnas:
        df[columna] = ''

    columnas = ['operado', 'cobra', 'paga']
    for columna in columnas:
        if columna =='cobra':
            df[columna] = df['monto']
        else:
         df[columna] = 0

    buffer = StringIO()
    df.to_csv(buffer, index=False, header=False, sep=';')
    buffer.seek(0)
    #df.to_csv('/tmp/menu.csv') otra opcion
    return buffer, tuple(df.columns)


def crear_tabla_cauciones(archivo, columnas):
    conn = None
    conn = _get_connection('FLW')
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    try:
        cur.execute('SET search_path TO colocadoras_fci')
        cur.copy_from(archivo, 'cauciones', sep=';',
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
    data = consultar_cauciones()
    buffer, columnas = create_csv(data)
    crear_tabla_cauciones(buffer, columnas)

if __name__ == "__main__":
    main()
