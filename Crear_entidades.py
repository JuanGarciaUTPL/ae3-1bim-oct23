"""
    Crear entidades
"""

from bd_tareaAE3 import conn

# creo cursor.

cursor = conn.cursor()

# Lista de tablas a crear

tablas = [
    ('Ciudad', ('nombre', 'provincia', 'habitantes')),
    ('Estadio', ('nombreEstadio', 'capacidad', 'equipo')),
]

for tabla in tablas:
    nombre, columnas = tabla

    cadena_sql = 'CREATE TABLE {} ({})'.format(nombre, ','.join(columnas))

    cursor.execute(cadena_sql)



# cerrar
cursor.close()

