"""
    Guarda información
"""

from bd_tareaAE3 import conn

# cursor

cursor = conn.cursor()

# cadenas Ciudad

nombre = "Quito"
provincia = "Pichincha"
habitantes = "2827106"
cadena_sql = """INSERT INTO Ciudad (nombre, provincia, habitantes) \
VALUES ('%s', '%s', %s);""" % (nombre, provincia, habitantes)

# ejecutar el SQL
cursor.execute(cadena_sql)

# confirmar los cambios a través del objeto importado de tip Connection
conn.commit()

# cerrar el enlace a la base de datos (recomendado)
cursor.close()
