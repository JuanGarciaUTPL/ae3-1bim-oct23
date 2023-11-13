# archivo Ciudad.py

from comun import get_conn

conn_ciudad = get_conn()


cursorCiu = conn_ciudad.cursorCiu()

ciudad_sql = 'CREATE TABLE Ciudad (nombre TEXT, provincia TEXT, habitantes INTEGER)'

cursorCiu.execute(ciudad_sql)

cursorCiu.close()