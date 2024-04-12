# index.py
import discord
import os
from traductor.traductor import bot  # Asume que este es el bot ya inicializado
from discord_slash import SlashCommand  # Esto ahora viene de una extensión compatible
from bot_commands.BasicCommands import register_commands  # Asume que has renombrado tu módulo a bot_commands y tiene una función register_commands

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="/", intents=intents)

# Inicializa el soporte de comandos slash
slash = SlashCommand(bot, sync_commands=True)

# Registra tus comandos slash utilizando la función que los registra
register_commands(slash)

# Variable global para almacenar la ID del canal
canal_id_eventos = None

@bot.event
async def on_ready():
    print(f'Bot listo como {bot.user.name}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    # Puedes agregar más manejo de errores según sea necesario
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot.run(BOT_TOKEN)
