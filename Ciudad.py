# archivo Ciudad.py

from bd_ciudades import conn_ciu

# creo cursor

cursorCiu = conn_ciu.cursorCiu()

# creo tabla

ciudad_sql = 'CREATE TABLE Ciudad (nombre TEXT, provincia TEXT, habitantes INTEGER)'

cursorCiu.execute(ciudad_sql)

cursorCiu.close()
