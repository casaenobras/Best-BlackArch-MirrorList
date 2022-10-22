import sqlite3, os

from data import *

# Create the database with the test results
def create_db():

    try:
        conn = sqlite3.connect('mirrors.db')
        cursor= conn.cursor()

    except:
        print("\n[!] Unable to connect to database mirror.db")

    try:
        insert_results = """
        DROP TABLE IF EXISTS repos;
        CREATE TABLE repos(ID integer PRIMARY KEY AUTOINCREMENT, mirror VARCHAR(100), tamaño_archivo INT(50), download_speed INT(20), connect_time INT(20), total_time INT(20));
        """

        cursor.executescript(insert_results)

        conn.commit()

    except:
        print("\n[!] Unable to create table in mirrors.db\n")

    try:
        cursor.executemany("INSERT INTO repos(mirror, tamaño_archivo, download_speed, connect_time, total_time) VALUES(?,?,?,?,?)", get_datos(get_mirrorList()))

        conn.commit()

    except:
        print("\n[!] Unable to enter data into database\n")

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
            print("\n[!] Could not connect to mirror database.db\n")

        try:
            cursor.execute("SELECT * FROM repos ORDER BY " + order_mode + limit)
            rows = cursor.fetchall()
            return rows

        except:
            print("\n[!] Resolves cannot be displayed or no data exists.")
            print("[!] Use the -t parameter to take the test\n")

        finally:
            cursor.close()
            conn.close()

    else:
        print("\n[!] Use the -t parameter to take the test\n")

# Returns a list with the data of the indicated ID's
def server_sel(select):

    try:
        conn = sqlite3.connect('mirrors.db')
        cursor= conn.cursor()

    except:
        print("\n[!] Could not connect to mirror database.db\n")

    try:
        cursor.execute("SELECT * FROM repos WHERE ID IN (" + select + ")")
        sel = cursor.fetchall()
        return sel

    except:
        print("\n[!] Resolves cannot be displayed or such data does not exist.")
        print("[!] Use the -t parameter to take the test\n")

    finally:
        cursor.close()
        conn.close()