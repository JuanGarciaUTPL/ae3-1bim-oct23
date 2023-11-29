"""
Consulta de información en las entidades en la base de datos
"""

from bd_tareaAE3 import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear variables para almacenar los nombres de las tablas
nombre_tabla_ciudad = "Ciudad"
nombre_tabla_estadio = "Estadio"

# hace consultas a la base de datos
cadena_consulta_sql_ciudad = "SELECT * from %s" % nombre_tabla_ciudad
cursor.execute(cadena_consulta_sql_ciudad)
informacion_ciudad = cursor.fetchall()

cadena_consulta_sql_estadio = "SELECT * from %s" % nombre_tabla_estadio
cursor.execute(cadena_consulta_sql_estadio)
informacion_estadio = cursor.fetchall()

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante de la tabla Ciudad
for d in informacion_ciudad:
    print("%s - %s - %d" % (d[0], d[1], d[2]))

# se realiza un ciclo repetitivo para recorrer la secuencia de información
# resultante de la tabla Estadio
for d in informacion_estadio:
    print("%s - %d - %s" % (d[0], d[1], d[2]))

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
