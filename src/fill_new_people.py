#!python3
import psycopg2
import psycopg2.extras
import redflagbpm
from redflagbpm import PgUtils

bpm = redflagbpm.BPMService()


def _get_connection():
    # Manual connection, no config file
    conn = PgUtils.get_connection(bpm, 'FLW')
    conn.autocommit = True
    return conn


def users_not_in_table():
    sql = '''select user_id_
        from act_id_membership
        where user_id_ not in (select distinct nombre from menu.menu)
        and
        group_id_ = 'MENU'
        '''
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql)
    data = cur.fetchall()
    cur.close()
    users = [item['user_id_'] for item in data]
    return users


def insert_new_user(user):
    sql = '''INSERT
    INTO
    menu.menu(nombre,lunes,martes,miercoles,jueves,viernes)
    VALUES(%s, '','','','','');
    '''
    conn = _get_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(sql,(user,))

def main():
    users = users_not_in_table()
    for user in users:
        insert_new_user(user)
    
