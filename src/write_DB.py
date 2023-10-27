import datetime

import psycopg2, psycopg2.extras
import logging
import json
logger = logging.getLogger(__name__)

def log_rescate(conn, id_origen, mensaje, **kwargs):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    #generate logs dict
    log = {}
    #timestamp now
    log['timestamp'] = str(datetime.datetime.now())
    log['mensaje'] = mensaje
    # dict to json
    log = json.dumps([log])

    insert_on_conflict = "INSERT into FCISTDR.rescate_status (id_origen, "

    val_list = []
    val_list.append(id_origen)

    for k, v in kwargs.items():
        if k == 'estado':
            v = kwargs['estado'].upper()
        insert_on_conflict += str(k) + ', '
        val_list.append(v)

    val_list.append(log)
    insert_on_conflict += 'log) values (%s, '

    for i in range (len(kwargs)):
        insert_on_conflict += ' %s, '

    insert_on_conflict += '%s::jsonb) on conflict (id_origen) do update set '

    for k, v in kwargs.items():
        insert_on_conflict += str(k) + '= excluded.' + str(k) + ', '

    insert_on_conflict = insert_on_conflict[:-1]
    insert_on_conflict += ' log = FCISTDR.rescate_status.log || excluded.log ::jsonb'

    params = tuple(val_list)
    cur.execute(insert_on_conflict, params)

    cur.close()

def update_rescate_status(conn, id_grupo, mensaje, **kwargs):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    #generate logs dict
    log = {}
    #timestamp now
    log['timestamp'] = str(datetime.datetime.now())
    log['mensaje'] = mensaje
    # dict to json
    log = json.dumps([log])

    update = "UPDATE FCISTDR.rescate_status set id_grupo = %s, "

    val_list = []
    val_list.append(id_grupo)
    for k, v in kwargs.items():
        if k == 'estado':
            v = kwargs['estado'].upper()
        update += str(k) + '= %s, '
        val_list.append(v)

    update += 'log = log || %s::jsonb'
    val_list.append(log)
    val_list.append(id_grupo)
    # update = update[:-1]
    update += ' where id_grupo = %s'

    params = tuple(val_list)
    cur.execute(update, params)

    cur.close()

def update_rescates_eliminados(conn, fecha_alta_desde, fecha_alta_hasta):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    update = """
    update FCISTDR.rescate_status set estado = 'ELIMINADO' where
        fecha_alta::date between
        %s and %s 
        and estado = 'PREINGRESADO'
        """
    params = tuple([fecha_alta_desde, fecha_alta_hasta])
    cur.execute(update, params)
    cur.close()


def log_suscripcion(conn, id_origen, mensaje, **kwargs):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    #generate logs dict
    log = {}
    #timestamp now
    log['timestamp'] = str(datetime.datetime.now())
    log['mensaje'] = mensaje
    # dict to json
    log = json.dumps([log])

    insert_on_conflict = "INSERT into FCISTDR.suscripcion_status (id_origen, "

    val_list = []
    val_list.append(id_origen)

    for k, v in kwargs.items():
        if k == 'estado':
            v = kwargs['estado'].upper()
        insert_on_conflict += str(k) + ', '
        val_list.append(v)

    val_list.append(log)
    insert_on_conflict += 'log) values (%s, '

    for i in range (len(kwargs)):
        insert_on_conflict += ' %s, '

    insert_on_conflict += '%s::jsonb) on conflict (id_origen) do update set '

    for k, v in kwargs.items():
        insert_on_conflict += str(k) + '= excluded.' + str(k) + ', '

    insert_on_conflict = insert_on_conflict[:-1]
    insert_on_conflict += ' log = FCISTDR.suscripcion_status.log || excluded.log ::jsonb'

    params = tuple(val_list)
    cur.execute(insert_on_conflict, params)

    cur.close()

def update_suscripcion_status(conn, id_origen, mensaje, **kwargs):
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    #generate logs dict
    log = {}
    #timestamp now
    log['timestamp'] = str(datetime.datetime.now())
    log['mensaje'] = mensaje
    # dict to json
    log = json.dumps([log])

    update = "UPDATE FCISTDR.suscripcion_status set id_origen = %s, "

    val_list = []
    val_list.append(id_origen)
    for k, v in kwargs.items():
        if k == 'estado':
            v = kwargs['estado'].upper()
        update += str(k) + '= %s, '
        val_list.append(v)

    update += 'log = log || %s::jsonb'
    val_list.append(log)
    val_list.append(id_origen)
    # update = update[:-1]
    update += ' where id_origen = %s'

    params = tuple(val_list)
    cur.execute(update, params)

    cur.close()

