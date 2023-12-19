#!python3

from redflagbpm import BPMService
from redflagbpm import PgUtils

def _get_hg_connection(bpm: BPMService):
    conn = PgUtils.get_connection(bpm, "SYC")
    conn.autocommit = True
    return conn

def _get_connection(bpm: BPMService):
    conn = PgUtils.get_connection(bpm, "FLW")
    conn.autocommit = True
    return conn
