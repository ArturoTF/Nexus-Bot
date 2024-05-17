from googletrans import Translator

translator = Translator()

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

def get_user_language(user_id, db_connection):
    cursor = db_connection.cursor()
    cursor.execute("SELECT language FROM users WHERE user_id = %s", (user_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    return 'en'  # Default to English if no language is set

def translate_text(text, dest_language):
    translated = translator.translate(text, dest=dest_language)
    return translated.text

def get_available_languages():
    return translator.LANGUAGES

def get_language_from_emoji(emoji):
    return emoji_flags.get(emoji, 'en')
