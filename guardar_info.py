"""
Guarda información en las entidades en la base de datos
"""

from bd_tareaAE3 import conn

# se usa el objeto Connection y se accede al método cursor
# para poder realizar las acciones en la base de datos.

cursor = conn.cursor()

# a través de cursor su puede ejecutar comandos SQL mediante el método
# execute

# Crear una cadena que almacene la sentencia de ingreso de información
# se recuerda los atributos: nombre, apellido, cedula, edad
nombre = "Guayaquil"
provincia = "Guayas"
habitantes = 2746403
nombreEstadio = "George Capwell"
capacidad = 40000
equipo = "Emelec"

# dividir la cadena SQL en dos cadenas SQL separadas
cadena_sql_ciudad = """INSERT INTO Ciudad (nombre, provincia, habitantes)
VALUES ('%s', '%s', %d);""" % (nombre, provincia, habitantes)
cadena_sql_estadio = """INSERT INTO Estadio (nombreEstadio, capacidad, equipo)
VALUES ('%s', %d, '%s');""" % (nombreEstadio, capacidad, equipo)

# ejecutar la primera instrucción SQL
cursor.execute(cadena_sql_ciudad)

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# ejecutar la segunda instrucción SQL
cursor.execute(cadena_sql_estadio)

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
