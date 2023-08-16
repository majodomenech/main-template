import redflagbpm
from redflagbpm.PgUtils import get_connection
from psycopg2.extensions import QuotedString
from psycopg2.extras import RealDictCursor


def queryDataPoint(bpm: redflagbpm.BPMService, isin: str, fields: list = None):
    with get_connection(bpm, 'FLW') as connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            sql = """
                SELECT data
                FROM bbg.des
                WHERE id = %s
                LIMIT 1
            """
            cursor.execute(sql, (isin,))
            if cursor.rowcount == 0:
                return {}
            row = cursor.fetchone()['data']
            if fields is None:
                return row
            else:
                return {f: row[f] if f in row else None for f in fields}


def queryChashFlow(bpm: redflagbpm.BPMService, isin: str):
    with get_connection(bpm, 'FLW') as connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            sql = """
                SELECT cash_flow
                FROM bbg.des
                WHERE id = %s
                LIMIT 1
            """
            cursor.execute(sql, (isin,))
            if cursor.rowcount == 0:
                return {}
            row = cursor.fetchone()['cash_flow']
            return row


def queryFactorSchedule(bpm: redflagbpm.BPMService, isin: str):
    with get_connection(bpm, 'FLW') as connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            sql = """
                SELECT factor_schedule
                FROM bbg.des
                WHERE id = %s
                LIMIT 1
            """
            cursor.execute(sql, (isin,))
            if cursor.rowcount == 0:
                return {}
            row = cursor.fetchone()['factor_schedule']
            return row


def queryDataHistory(bpm: redflagbpm.BPMService, isin: str, start_date: str, end_date: str, fields: list = None):
    with get_connection(bpm, 'FLW') as connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            sql = """
                SELECT data
                FROM bbg.his
                WHERE id = %s
                AND target_date BETWEEN %s::date AND %s::date
            """
            cursor.execute(sql, (isin, start_date, end_date))
            if cursor.rowcount == 0:
                return []
            rows = [i['data'] for i in cursor.fetchall()]
            if fields is None:
                return rows
            else:
                return [{f: row[f] if f in row else None for f in fields} for row in rows]


def queryField(bpm: redflagbpm.BPMService, field: str):
    with get_connection(bpm, 'FLW') as connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            sql = """
                SELECT row_to_json(fc) as data
                FROM bbg.field_catalog fc
                WHERE id = %s or mnemonic = %s or clean_name = %s
                LIMIT 1
            """
            cursor.execute(sql, (field, field, field))
            if cursor.rowcount == 0:
                return {}
            row = cursor.fetchone()['data']
            return row


def queryFields(bpm: redflagbpm.BPMService, filter: str):
    with get_connection(bpm, 'FLW') as connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            sql = """
                SELECT id, mnemonic, clean_name, description, get_history, get_fundamentals, get_company, definition
                FROM bbg.field_catalog fc
                WHERE mnemonic like '%%'||%s||'%%'
                    or clean_name like '%%'||%s||'%%'
                    or description like '%%'||%s||'%%'
                    or definition like '%%'||%s||'%%'
            """
            cursor.execute(sql, (filter, filter, filter, filter))
            if cursor.rowcount == 0:
                return {}
            return cursor.fetchall()

def queryWatchList(bpm: redflagbpm.BPMService):
    with get_connection(bpm, 'SYC') as connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            sql = """
                select string_agg(trim(upper(u."CODIGOISIN")),',') as isins
                from "UNI_ATRIBUTO" a
                inner join "UNI_UNIDAD" u ON u."UNI_UNIDAD_ID" = a."UNIDAD"
                where trim(upper(a."VALOR")) not in ('NO','FALSE','FALSO')
                and a."ATRIBUTO"='Bloomberg'
            """
            cursor.execute(sql)
            if cursor.rowcount == 0:
                return None
            return cursor.fetchone()['isins'].split(',')
