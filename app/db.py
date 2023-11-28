# app/db.py

import mysql.connector
from flask import g
from config import get_config

def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(**get_config().DB_CONFIG)
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()