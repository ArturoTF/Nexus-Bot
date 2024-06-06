import discord
from discord.ext import commands
from googletrans import Translator
from discord.commands import slash_command, Option, OptionChoice
import mysql.connector
import os
from ....environments.utils import emoji_flags
from ....environments.connection import create_connection, close_connection
from ....environments.logging import safe_log

class setLanguaje(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()

    @slash_command(name="setlanguage", description="Select your language")
    async def setlanguage(self, ctx, 
                          idioma: Option(str, 
                                         "Elige tu idioma", 
                                         choices=[OptionChoice(name=f"{flag} {code.upper()}", value=code) for flag, code in emoji_flags.items()])):
        user_id = ctx.author.id
        username = str(ctx.author)

        connection = create_connection()
        if connection:
            try:
                cursor = connection.cursor()
                query = """INSERT INTO usuarios_idioma (user_id, name, idioma)
                           VALUES (%s, %s, %s)
                           ON DUPLICATE KEY UPDATE idioma = VALUES(idioma)"""
                cursor.execute(query, (user_id, username, idioma))
                connection.commit()
                flag = next((f for f, c in emoji_flags.items() if c == idioma), None)
                await ctx.respond(f"{ctx.author.mention}, tu idioma se ha establecido a {flag if flag else 'Unknown language'}")
                # safe_log(connection, "INFO", f"Idioma de usuario {username} establecido a {idioma}", "setlanguage")
            except mysql.connector.Error as err:
                await ctx.respond(f"Error al establecer el idioma: {err}")
                safe_log(connection, "ERROR", f"Error al establecer idioma para {username}: {err}", "setlanguage")
            finally:
                cursor.close()
                close_connection(connection)
        else:
            await ctx.respond("No se pudo conectar a la base de datos")


def setup(bot):
    bot.add_cog(setLanguaje(bot))
