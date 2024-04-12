import os
import mysql.connector
from mysql.connector import Error

# Función para crear una conexión a la base de datos
def create_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQLHOST'),
            database=os.getenv('MYSQLDATABASE'),
            user=os.getenv('MYSQLUSER'),
            password=os.getenv('MYSQLPASSWORD'),
            port=os.getenv('MYSQLPORT')
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado a MySQL Server versión {db_info}")
            return connection
    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

# Función para cerrar la conexión
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexión a MySQL cerrada")
