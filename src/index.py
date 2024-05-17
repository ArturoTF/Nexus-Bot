import discord
import os
import logging
from discord.ext import commands
from app.environments.connection import create_connection, close_connection
from app.environments.logging import safe_log

# Configurar el nivel de registro global
logging.basicConfig(level=logging.ERROR)

# Desactivar logs específicos de Discord.py
discord_logger = logging.getLogger('discord')
discord_logger.setLevel(logging.ERROR)

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='/', intents=intents)

# Cargar cogs
bot.load_extension('app.modules.bot_commands.basicCommands')
bot.load_extension('app.modules.bot_commands.traductorCommand')

@bot.event
async def on_ready():
    connection = create_connection()
    if connection:
        safe_log(connection, "INFO", f"Bot listo como {bot.user.name}", "on_ready")
        close_connection(connection)
    print(f'Bot listo como {bot.user.name}')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx, error):
    connection = create_connection()
    if isinstance(error, commands.CommandNotFound):
        if connection:
            safe_log(connection, "WARNING", f"Comando no encontrado: {ctx.invoked_with}", "on_command_error")
    else:
        if connection:
            safe_log(connection, "ERROR", f"Error inesperado en comando: {str(error)}", "on_command_error")
    if connection:
        close_connection(connection)

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot.run(BOT_TOKEN)
