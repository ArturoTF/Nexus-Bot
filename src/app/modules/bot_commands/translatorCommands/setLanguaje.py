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
    async def setlanguage(self, ctx, idioma: Option(str, "Elige tu idioma", choices=[OptionChoice(name=f"{flag} {code.upper()}", value=code) for flag, code in emoji_flags.items()])):
        user_name = ctx.author.name
        user_id = ctx.author.id
        print(user_id)
        connection = create_connection()      
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO usuarios_idioma (user_id, name, idioma) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE idioma = VALUES(idioma)",
                    (user_id, user_name, idioma)
                )
                connection.commit()
                flag = next((f for f, c in emoji_flags.items() if c == idioma), None)
                await ctx.respond(f"{ctx.author.mention}, tu idioma se ha establecido a {flag if flag else 'Unknown language'}")
                safe_log(connection, "INFO", f"Idioma actualizado para {user_name} a {idioma}", "setlanguage")
            except mysql.connector.Error as e:
                safe_log(connection, "ERROR", f"Error en setlanguage: {e}", "setlanguage")
                await ctx.respond("Error al procesar tu solicitud. Por favor, inténtalo de nuevo.")
            finally:
                close_connection(connection)
        else:
            await ctx.respond("Error al conectar con la base de datos.")

def setup(bot):
    bot.add_cog(setLanguaje(bot))
