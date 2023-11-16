"""
    Crear entidades
"""

from bd_tareaAE3 import conn

# creo cursor.

cursor = conn.cursor()

# Crear tabla Ciudad

cadena_sql = 'CREATE TABLE Ciudad (nombre TEXT, provincia TEXT, habitantes INTEGER)'

# Crear tabla Estadio

cadena_sql = 'CREATE TABLE Estadio (nombreEstadio TEXT, equipo TEXT, capacidad INTEGER)'

# ejecutar
cursor.execute(cadena_sql)

# cerrar
cursor.close()
