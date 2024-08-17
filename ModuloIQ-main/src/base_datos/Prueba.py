import sys
sys.path.append('c:/Users/Tomas/OneDrive/Documentos/Requisitos 2024-1/ModuloIQ-main')

import pickle
import sqlite3
import os

directorio = os.path.dirname(os.path.abspath(__file__))
ruta_base_datos = os.path.join(directorio, 'prueba.db')
conn = sqlite3.connect(ruta_base_datos)

c = conn.cursor()

try:
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tablas = c.fetchall()

    for tabla in tablas:
        nombre_tabla = tabla[0]
        print(f"\nDatos de la tabla {nombre_tabla}:")

        c.execute(f"PRAGMA table_info({nombre_tabla})")
        filas = c.fetchall()

        c.execute(f"PRAGMA table_info({nombre_tabla})")
        columnas = c.fetchall()
        nombres_columnas = [columna[1] for columna in columnas]

        print(" | ".join(nombres_columnas))
        print("-" * (len(nombres_columnas) * 20))

        for fila in filas:
            print(" | ".join(str(valor) for valor in fila))

except sqlite3.Error as e:
    print(f"Error de SQLite: {e}")

finally:
    conn.close()



#Crear tabla
#c.execute("""CREATE TABLE estudiantes(
#                ID INTEGER PRIMARY KEY AUTOINCREMENT,
#                Sede TEXT
#)""")
#Agregar un dato a la tabla
#c.execute("INSERT INTO estudiantes VALUES ('mark', 27, 1.90)")
#todos_estudiantes = [
#    ('Juan', 30, 1.80),
#    ('Pepe', 20, 1.60),
#    ('Messi', 80, 1.70),
#    ('Cr7', 40, 1.90)
#]
#Agregar varios datos a la tabla
#c.executemany("INSERT INTO estudiantes VALUES (?, ?, ?)", todos_estudiantes)
#Abrir los datos de la tabla

#c.execute("SELECT * FROM maestros")
#lista = c.fetchall()
#for ID, maestro in lista:
    #print(ID, pickle.loads(maestro))
#conn.commit()
#conn.close()

