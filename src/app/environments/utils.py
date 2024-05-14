import os
from app.environments.connection import create_connection,close_connection
from ...environments.logging import safe_log

def get_user_language(user_id):
    """
    Recupera el idioma preferido de un usuario basado en su ID.
    Retorna 'en' si el usuario no ha especificado un idioma.
    """
    try:
        # Crea una conexión a la base de datos
        connection = create_connection()
        if connection is not None:
            cursor = connection.cursor()
            # Preparar la consulta SQL para obtener el idioma del usuario
            query = "SELECT idioma FROM usuarios_idioma WHERE name = %s"
            cursor.execute(query, (user_id,))
            # Obtener el resultado
            result = cursor.fetchone()
            cursor.close()
            # Comprueba si se encontró un idioma y retorna el resultado
            if result:
                return result[0]
            else:
                return 'en'  # Idioma por defecto si no se encuentra en la base de datos
        else:
            return 'en'  # Retorna inglés por defecto si la conexión falla
    except Error as e:
        print(f"Error al obtener el idioma del usuario: {e}")
        return 'en'  # Retorna inglés por defecto en caso de error
    finally:
        # Cierra la conexión a la base de datos
        if connection and connection.is_connected():
            close_connection(connection)


# Diccionario de banderas con códigos de idioma correspondientes
emoji_flags = {
    '🇬🇧': 'en',  # Inglés
    '🇪🇸': 'es',  # Español
    '🇩🇪': 'de',  # Alemán
    '🇷🇺': 'ru',  # Ruso
    '🇵🇹': 'pt',  # Portugués
    '🇻🇳': 'vi',  # Vietnamita
    '🇨🇳': 'zh-cn', # Chino (simplificado)
    '🇮🇹': 'it',  # Italiano
    '🇫🇷': 'fr',  # Francés
    '🇵🇱': 'pl',  # Polaco
    '🇺🇸': 'en',  # Inglés Americano
    '🇷🇸': 'sr',  # Serbio
    '🇯🇵': 'ja',  # Japonés
}
