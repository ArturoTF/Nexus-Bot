import mysql.connector
from mysql.connector import Error

def log_to_database(connection, level, message, source):
    """ Inserta un registro en la tabla de logs de la base de datos usando la conexión proporcionada. """
    try:
        if connection.is_connected():
            cursor = connection.cursor()
            query = """
                INSERT INTO logs (level, message, source) 
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (level, message, source))
            connection.commit()
    except mysql.connector.Error as e:
        print(f"Error al insertar el log en la base de datos: {e}")
    finally:
        if cursor:
            cursor.close()

def safe_log(connection, level, message, source):
    """ Envoltura segura para log_to_database que maneja excepciones. """
    try:
        log_to_database(connection, level, message, source)
    except Exception as e:
        print(f"Error al registrar log: {e}")
