from discord.ext import commands
from discord.commands import slash_command, Option, OptionChoice
import discord
import mysql.connector
import os

from ...environments.utils import emoji_flags
from ...environments.connection import create_connection, close_connection
from ...environments.logging import safe_log

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="ceo", description="Muestra quién es el CEO")
    async def ceo(self, ctx):
        connection = create_connection()
        if connection:
            safe_log(connection, "INFO", "Comando CEO invocado", "ceo")
            close_connection(connection)
        await ctx.respond("The CEO of this project is ArturoTF")

    @slash_command(name="languages", description="Muestra los idiomas disponibles para traducción")
    async def languages(self, ctx):
        language_list = ', '.join(emoji_flags.keys())
        connection = create_connection()
        if connection:
            safe_log(connection, "INFO", "Comando languages invocado", "languages")
            close_connection(connection)
        await ctx.respond(f"Languages available for translation: {language_list}")

    @slash_command(name="version", description="Muestra la versión del bot")
    async def version(self, ctx):
        try:
            with open("setup.py", "r") as f:
                for line in f:
                    if line.startswith("version="):
                        version = line.split("=")[1].strip().strip('"').strip("'")
                        await ctx.respond(f"La versión del bot es: {version}")
                        return
            await ctx.respond("No se pudo encontrar la versión en setup.py")
        except Exception as e:
            await ctx.respond(f"Error al leer setup.py: {e}")

def setup(bot):
    bot.add_cog(BasicCommands(bot))
