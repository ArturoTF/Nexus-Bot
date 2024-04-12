import os
import mysql.connector
from mysql.connector import Error
from .logging import safe_log


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
            safe_log("INFO", f"Conectado a MySQL Server versión {db_info}", "create_connection")
            return connection
    except Error as e:
        safe_log("ERROR", f"Error al conectar a MySQL: {e}", "create_connection")
        return None

# Función para cerrar la conexión
def close_connection(connection):
    try:
        if connection.is_connected():
            connection.close()
            safe_log("INFO", "Conexión a MySQL cerrada correctamente", "close_connection")
    except Error as e:
        safe_log("ERROR", f"Error al cerrar la conexión MySQL: {e}", "close_connection")