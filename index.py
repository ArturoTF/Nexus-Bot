# index.py
import discord
import os
from discord.ext import commands  # Agrega esta línea
from traductor.traductor import bot

intents = discord.Intents.default()
intents.messages = True

# Token de tu bot proporcionado por Discord Developer Portal
BOT_TOKEN = 'MTEzNTkwNDg5NzIzODMwMjcyMA.Gw0cpn.bSMuYM6cwhAjmd7TQ9p4K8XmBPWD80goDO78Mk'

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
