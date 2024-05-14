from discord.ext import commands
from discord.commands import slash_command, Option, OptionChoice
import discord
import mysql.connector
from ...environments.utils import emoji_flags  # Importar desde utils
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
        language_list = ', '.join(emoji_flags.keys())
        connection = create_connection()
        if connection:
            safe_log(connection, "INFO", "Comando languages invocado", "languages")
            close_connection(connection)
        await ctx.respond(f"Languages available for translation: {language_list}")

    @bot.slash_command(name="setlanguage", description="Select your language")
    async def setlanguage(ctx, idioma: discord.Option(str, "Elige tu idioma", choices=[OptionChoice(name=f"{flag} {code.upper()}", value=code) for flag, code in emoji_flags.items()])):
        user_name = ctx.author.name
        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO usuarios_idioma (name, idioma) VALUES (%s, %s) ON DUPLICATE KEY UPDATE idioma = VALUES(idioma)",
                    (user_name, idioma)
                )
                connection.commit()
                await ctx.respond(f"{ctx.author.mention}, tu idioma se ha establecido a {flag} {code.upper()}")
                safe_log(connection, "INFO", f"Idioma actualizado para {user_name} a {idioma}", "setlanguage")
            except mysql.connector.Error as e:
                safe_log(connection, "ERROR", f"Error en setlanguage: {e}", "setlanguage")
                await ctx.respond("Error al procesar tu solicitud. Por favor, inténtalo de nuevo.")
            finally:
                close_connection(connection)
        else:
            await ctx.respond("Error al conectar con la base de datos.")