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
                SELECT data
                FROM bbg.fields
                WHERE id = %s or mnemonic = %s
                LIMIT 1
            """
            cursor.execute(sql, (field, field))
            if cursor.rowcount == 0:
                return {}
            row = cursor.fetchone()['data']
            return row
