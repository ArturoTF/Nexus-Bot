import os
from .connection import create_connection, close_connection
from mysql.connector import Error

def log_to_database(level, message, source):
    """ Inserta un registro en la tabla de logs de la base de datos. """
    connection = create_connection()
    if connection is not None:
        try:
            cursor = connection.cursor()
            query = """
                INSERT INTO logs (level, message, source) 
                VALUES (%s, %s, %s)
            """
            cursor.execute(query, (level, message, source))
            connection.commit()
        except Error as e:
            print(f"Error al insertar el log en la base de datos: {e}")
        finally:
            cursor.close()
            close_connection(connection)
    else:
        print("Conexión a la base de datos no establecida.")

def safe_log(level, message, source):
    """ Envoltura segura para log_to_database que maneja excepciones. """
    try:
        log_to_database(level, message, source)
    except Exception as e:
        print(f"Error al registrar log: {e}")

# Ejemplo de cómo podrías usar estas funciones en tu aplicación:
if __name__ == "__main__":
    # Realiza una prueba de registro de log
    safe_log("INFO", "Prueba de registro de log", "sistema_de_logs")