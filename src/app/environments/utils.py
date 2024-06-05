import os
from ..environments.connection import create_connection, close_connection
from ..environments.connection import create_connection, close_connection

def get_user_language(user_id):
    try:
        connection = create_connection()
        if connection is not None:
            cursor = connection.cursor()
            query = "SELECT idioma FROM usuarios_idioma WHERE user_id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            cursor.close()
            print(result[0])
            if result:
                return result[0]
            else:
                return 'en'
        else:
            return 'en'
    except Error as e:
        print(f"Error al obtener el idioma del usuario: {e}")
        return 'en'
    finally:
        if connection and connection.is_connected():
            close_connection(connection)



# Diccionario de banderas con códigos de idioma correspondientes -> banderaDiscord : valor. Puedo añadir todos los que quiera
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
