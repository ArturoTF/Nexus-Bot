import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.reactions = True
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


def cargarModulos():
    bot.load_extension('app.modules.bot_commands.basicCommands')
    bot.load_extension('app.modules.bot_commands.translatorCommands.setLanguage')
    bot.load_extension('app.modules.bot_commands.translatorCommands.translate')
    bot.load_extension("app.modules.bot_commands.weather")
    bot.load_extension("app.modules.bot_commands.news")
    bot.load_extension("app.modules.bot_commands.facts")
