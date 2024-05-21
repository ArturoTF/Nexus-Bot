import discord
from discord.ext import commands

intents = discord.Intents.default()  # Asegúrate de activar los intents necesarios
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='/', intents=intents)


def cargarModulos():
    bot.load_extension('app.modules.bot_commands.basicCommands')
    bot.load_extension('app.modules.bot_commands.translatorCommands.setLanguaje')
    bot.load_extension('app.modules.bot_commands.translatorCommands.translate')
    bot.load_extension("app.modules.bot_commands.weather")
    bot.load_extension("app.modules.bot_commands.news")
    bot.load_extension("app.modules.bot_commands.facts")
