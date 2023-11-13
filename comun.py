# archivo comun.py

import sqlite3

conn = sqlite3.connect('bd_tareaAE3.db')

def get_conn():
    return conn