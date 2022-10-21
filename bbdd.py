import sqlite3, os

from data import *

# Create the database with the test results
def create_db():

    try:
        conn = sqlite3.connect('mirrors.db')
        cursor= conn.cursor()

    except:
        print("\n[!] No se ha podido conectar con la base de datos mirror.db")

    try:
        insert_results = """
        DROP TABLE IF EXISTS repos;
        CREATE TABLE repos(ID integer PRIMARY KEY AUTOINCREMENT, mirror VARCHAR(100), tamaño_archivo INT(50), download_speed INT(20), connect_time INT(20), total_time INT(20));
        """

        cursor.executescript(insert_results)

        conn.commit()

    except:
        print("\n[!] No se ha podido crear la tabla en mirrors.db\n")

    try:
        cursor.executemany("INSERT INTO repos(mirror, tamaño_archivo, download_speed, connect_time, total_time) VALUES(?,?,?,?,?)", get_datos(get_mirrorList()))

        conn.commit()

    except:
        print("\n[!] No se han podido introducir los datos en la base de datos\n")

    finally:
        cursor.close()
        conn.close()

# Returns a list ordered the results based on the indicated parameters
def order(order_mode, limit):

    if os.path.isfile("mirrors.db"):

        if limit != "":
            limit = " LIMIT " + limit

        if order_mode == "download_speed":
            order_mode += " DESC"
        
        try:
            conn = sqlite3.connect('mirrors.db')
            cursor= conn.cursor()

        except:
            print("\n[!] No se ha podido conectar con la base de datos mirror.db\n")

        try:
            cursor.execute("SELECT * FROM repos ORDER BY " + order_mode + limit)
            rows = cursor.fetchall()
            return rows

        except:
            print("\n[!] No se pueden mostrar los resutaldos o no existen datos.")
            print("[!] Utiliza el parámetro -t para hacer el test\n")

        finally:
            cursor.close()
            conn.close()

    else:
        print("\n[!] Utiliza el parámetro -t para hacer el test\n")

# Returns a list with the data of the indicated ID's
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