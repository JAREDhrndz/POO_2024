import mysql.connector
from mysql.connector import Error

def conexionBD():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='maquinaexpendedora'
        )
        if connection.is_connected():
            print("Conexión a la base de datos establecida correctamente.")
            return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def cerrarConexion(connection):
    try:
        if connection and connection.is_connected():
            connection.close()
            print("Conexión a la base de datos cerrada")
    except mysql.connector.Error as e:
        print(f"Error al cerrar la conexión: {e}")

def ejecutar_query(connection, query, params=None):
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
    except mysql.connector.Error as e:
        print(f"Error en la consulta: {e}")
    finally:
        cursor.close()

def fetch_all(connection, query, params=None):
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchall()
    except mysql.connector.Error as e:
        print(f"Error en la consulta: {e}")
        return []
    finally:
        cursor.close()
def fetch_one(connection, query, params=None):
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        return cursor.fetchone()  
    except mysql.connector.Error as e:
        print(f"Error en la consulta: {e}")
        return None
    finally:
        cursor.close()
def esperarTecla():
  print("\n \t \tOprima cualquier tecla para continuar ...")
  input()  
def borrarPantalla():
    import os
    sistema = os.name
    if sistema == 'posix':
        os.system('clear')
    elif sistema == 'nt':
        os.system('cls')