# archivo Estadio.py

global conn_estadio

from comun import get_conn

conn_estadio = get_conn()

cursorEst = conn_estadio.cursorEst()

estadio_sql = 'CREATE TABLE Estadio (nombre TEXT, club TEXT, capacidad INTEGER)'

cursorEst.execute(estadio_sql)

cursorEst.close()
