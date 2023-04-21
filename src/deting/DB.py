#!/usr/bin/env python
# coding: utf-8
import psycopg2
from psycopg2.extensions import connection


def _get_hg_connection() -> connection:
    # Manual connection, no config file
    conn = psycopg2.connect(database="syc",
                            user="consyc",
                            password="MTU1NDNjN2ZlZGU4ZDdhNDBhZTM2MjA2",
                            host="db.sycinversiones.com",
                            port="5432")
    conn.autocommit = True
    return conn


def _get_persh_connection() -> connection:
    # Manual connection, no config file
    conn = psycopg2.connect(database="bi",
                            user="consyc",
                            password="MTU1NDNjN2ZlZGU4ZDdhNDBhZTM2MjA2",
                            host="db.sycinversiones.com",
                            port="5432")
    conn.autocommit = True
    return conn
