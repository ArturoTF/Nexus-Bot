# index.py
import discord
import os
from traductor.traductor import bot
from bot_commands import commands as bot_commands_module
from discord_slash import SlashCommand  # Esto ahora viene de una extensión compatible
from discord.ext import commands
import bot_commands.commands as bot_commands_module

intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="/", intents=intents)

slash = SlashCommand(bot, sync_commands=True)

commands_module.register_commands(slash)

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
