#!/usr/bin/env python
# coding: utf-8
import psycopg2

def _get_flw_connection(DB):
    #Manual connection, no config file
    conn = psycopg2.connect(database=DB,
                            user="flowable",
                            password="flowable",
                            host="db.sycinversiones.com",
                            port="5432")
    conn.autocommit = True
    return conn

def _get_hg_connection(DB):
    #Manual connection, no config file
    conn = psycopg2.connect(database=DB,
                        user="consyc",
                        password="MTU1NDNjN2ZlZGU4ZDdhNDBhZTM2MjA2",
                        host="db.sycinversiones.com",
                        port="5432")
    conn.autocommit = True
    return conn
