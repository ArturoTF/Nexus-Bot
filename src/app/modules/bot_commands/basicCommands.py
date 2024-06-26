from discord.ext import commands
from discord.commands import slash_command, Option, OptionChoice
import discord
import mysql.connector
import os

from ...environments.utils import emoji_flags
from ...environments.connection import create_connection, close_connection
from ...environments.logging import safe_log

version = "Version 1.0.0"

class BasicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="ceo", description="Muestra quién es el CEO")
    async def ceo(self, ctx):
        connection = create_connection()
        if connection:
            # safe_log(connection, "INFO", "Comando CEO invocado", "ceo")
            close_connection(connection)
        await ctx.respond("The CEO of this project is ArturoTF")

    @slash_command(name="languages", description="Muestra los idiomas disponibles para traducción")
    async def languages(self, ctx):
        language_list = ', '.join(emoji_flags.keys())
        connection = create_connection()
        if connection:
            # safe_log(connection, "INFO", "Comando languages invocado", "languages")
            close_connection(connection)
        await ctx.respond(f"Languages available for translation: {language_list}")

    @slash_command(name="version", description="Shows the bot's version")
    async def version(self, ctx):
        embed = discord.Embed(
            title="NEXUS BOT",
            description=f"**Version:** {version}\n\n**Features:**",
            color=discord.Color.blue()
        )
        
        embed.add_field(
            name="/setLanguage",
            value="Allows you to set your primary language.",
            inline=False
        )
        embed.add_field(
            name="/languages",
            value="Shows all available languages.",
            inline=False
        )
        embed.add_field(
            name="/ceo",
            value="Displays the project CEO.",
            inline=False
        )
        embed.add_field(
            name="/version",
            value="Shows the project version.",
            inline=False
        )
        embed.add_field(
            name="/translate [message]",
            value="Translates a message to your /setlanguage.",
            inline=False
        )
        embed.add_field(
            name="Emoji-based Translation",
            value="Translates messages when reacting with flag emojis.",
            inline=False
        )
        embed.add_field(
            name="Error Notification",
            value="Notifies errors during development (DB).",
            inline=False
        )
        embed.add_field(
            name="/weather [city]",
            value="Shows the weather for a city (temperature, humidity, wind speed, weather). Use /cities for available cities.",
            inline=False
        )
        embed.add_field(
            name="/news",
            value="Shows the latest news from BBC.",
            inline=False
        )
        embed.add_field(
            name="/facts",
            value="Shows interesting facts.",
            inline=False
        )

        await ctx.respond(embed=embed)
            
    @slash_command(name="help", description="Muestra la lista de comandos")
    async def help(self, ctx):
        embed = discord.Embed(
            title="Nexus Bot Helper",
            description="[] = required argument, <> = optional argument",
            color=discord.Color.blue()
        )
        
        commands_list = (
            "- /version\n"
            "- /ceo\n"
            "- /languages\n"
            "- /setLanguage [language]\n"
            "- /translate [message]\n"
            "- /list_topics\n"
            "- /facts [one topic]\n"
            "- /news\n"
            "- /cities\n"
            "- /weather [city]\n"
        )
        
        utilities_list = (
            "- You can translate a message from someone else by reacting to the message with the flag that you want to translate the message.\n"
            "  Available languages ​​/languages\n"
        )
        
        embed.add_field(name="**Commands**", value=commands_list, inline=False)
        embed.add_field(name="**Utilities**", value=utilities_list, inline=False)
        
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(BasicCommands(bot))
