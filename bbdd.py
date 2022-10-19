import sqlite3, os

from data import *

# Crea la base de datos con los resultados del test
def llena_db():

    try:
        conn = sqlite3.connect('mirrors.db')
        cursor= conn.cursor()

    except:
        print("\n[!] No se ha podido conectar con la base de datos mirror.db")

    try:
        insert_results = """
        DROP TABLE IF EXISTS repos;
        CREATE TABLE repos(ID integer PRIMARY KEY AUTOINCREMENT, mirror VARCHAR(100), tamaño_archivo INT(50), vel_descarga INT(20), tiempo_conex INT(20), tiempo_total INT(20));
        """

        cursor.executescript(insert_results)

        conn.commit()

    except:
        print("\n[!] No se ha podido crear la tabla en mirrors.db\n")

    try:
        cursor.executemany("INSERT INTO repos(mirror, tamaño_archivo, vel_descarga, tiempo_conex, tiempo_total) VALUES(?,?,?,?,?)", get_datos(get_mirrorList()))

        conn.commit()

    except:
        print("\n[!] No se han podido introducir los datos en la base de datos\n")

    finally:
        cursor.close()
        conn.close()

#Retorna una lista ordenada los resultados en base a los parametros indicados
def ordenar(modo_orden, limit):

    if os.path.isfile("mirrors.db"):

        if limit != "":
            limit = " LIMIT " + limit

        if modo_orden == "vel_descarga":
            modo_orden += " DESC"
        
        try:
            conn = sqlite3.connect('mirrors.db')
            cursor= conn.cursor()

        except:
            print("\n[!] No se ha podido conectar con la base de datos mirror.db\n")

        try:
            cursor.execute("SELECT * FROM repos ORDER BY " + modo_orden + limit)
            filas = cursor.fetchall()
            return filas

        except:
            print("\n[!] No se pueden mostrar los resutaldos o no existen datos.")
            print("[!] Utiliza el parámetro -t para hacer el test\n")

        finally:
            cursor.close()
            conn.close()

    else:
        print("\n[!] Utiliza el parámetro -t para hacer el test\n")

#Retorna una lista con los datos de los ID's indicados
def server_sel(select):

    try:
        conn = sqlite3.connect('mirrors.db')
        cursor= conn.cursor()

    except:
        print("\n[!] No se ha podido conectar con la base de datos mirror.db\n")

    try:
        cursor.execute("SELECT * FROM repos WHERE ID IN (" + select + ")")
        sel = cursor.fetchall()
        return sel

    except:
        print("\n[!] No se pueden mostrar los resutaldos o no existen esos datos.")
        print("[!] Utiliza el parámetro -t para hacer un nuevo test\n")

    finally:
        cursor.close()
        conn.close()