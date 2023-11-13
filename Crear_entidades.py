"""
	Crear entidades en la base de datos
"""

#primero para Ciudad

from Ciudad import conn_ciudad

# creo "cursor" para ejecutar commandos SQL

cursorCiu = conn_ciudad.cursorCiu()

# creo tabla de Ciudad

ciudad_sql = 'CREATE TABLE Ciudad (nombre TEXT, provincia TEXT, habitantes INTEGER)'

# ejecutar SQL ciudad

cursorCiu.execute(ciudad_sql)

#cerrando

cursorCiu.close()



#Segundo para Estadio

from Estadio import conn_estadio

# creo "cursor" para ejecutar commandos SQL

cursorEst = conn_estadio.cursorEst()

# creo tabla de Estadio

estadio_sql = 'CREATE TABLE Estadio (nombre TEXT, club TEXT, capacidad INTEGER)'

# ejecutar SQL estadio

cursorEst.execute(estadio_sql)

#cerrando

cursorEst.close()
