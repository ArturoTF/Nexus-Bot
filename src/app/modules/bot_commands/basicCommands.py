from discord.ext import commands
from discord.commands import slash_command, Option, OptionChoice  # Importaciones necesarias para los comandos slash
import discord
# Importaciones de tus funciones de conexión a la base de datos
from ...environments.connection import create_connection, close_connection
from ...environments.logging import safe_log

def register_commands(bot):
    @bot.slash_command(name="ceo", description="Muestra quién es el CEO")
    async def ceo(ctx):
        connection = create_connection()
        if connection:
            safe_log(connection, "INFO", "Comando CEO invocado", "ceo")
            close_connection(connection)
        await ctx.respond("The CEO of this project is ArturoTF")

    @bot.slash_command(name="languages", description="Muestra los idiomas disponibles para traducción")
    async def languages(ctx):
        language_list = "🇬🇧, 🇪🇸, 🇩🇪, 🇷🇺, 🇵🇹, 🇻🇳, 🇨🇳, 🇮🇹, 🇺🇸, 🇵🇱,🇺🇸,🇷🇸,🇯🇵"
        connection = create_connection()
        if connection:
            safe_log(connection, "INFO", "Comando languages invocado", "languages")
            close_connection(connection)
        await ctx.respond(f"Languages available for translation: {language_list}")

    # Diccionario de opciones de idiomas y sus banderas
    language_options = {
    'English': '🇬🇧',
    'Spanish': '🇪🇸',
    'German': '🇩🇪',
    'Russian': '🇷🇺',
    'Portuguese': '🇵🇹',
    'Vietnamese': '🇻🇳',
    'Chinese': '🇨🇳',
    'Italian': '🇮🇹',
    'French': '🇫🇷',
    'Polish': '🇵🇱',
    'American English': '🇺🇸',
    'Serbian': '🇷🇸',
    'Japanese': '🇯🇵',
    }


    @bot.slash_command(name="setlanguage", description="Select your language")
    async def setlanguage(ctx, idioma: discord.Option(str, "Elige tu idioma", choices=[OptionChoice(name=f"{name} {flag}", value=name) for name, flag in language_options.items()])):
        user_name = ctx.author.name
        connection = create_connection()
        try:
            if not connection:
                raise Exception("Failed to connect to database")
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO usuarios_idioma (name, idioma) VALUES (%s, %s) ON DUPLICATE KEY UPDATE idioma = VALUES(idioma)",
                (user_name, idioma)
            )
            connection.commit()
            await ctx.respond(f"{ctx.author.mention}, tu idioma se ha establecido a {language_options[idioma]}")
            safe_log(connection, "INFO", f"Idioma actualizado para {user_name} a {idioma}", "setlanguage")
        except Exception as e:
            if connection:
                safe_log(connection, "ERROR", f"Error en setlanguage: {e}", "setlanguage")
            await ctx.respond("Error al procesar tu solicitud. Por favor, inténtalo de nuevo.")
        finally:
            if connection:
                close_connection(connection)


