import discord
import os
from discord.ext import commands
from traductor.traductor import bot  # Asegúrate de que esta importación se hace correctamente
from bot_commands.commands import register_commands  # Función ajustada para py-cord

# No es necesario inicializar 'bot' de nuevo si ya lo has hecho en traductor.traductor
# Sólo asegúrate de que 'intents' estén correctamente configurados allí

# Registra tus comandos slash utilizando la función adaptada a py-cord
register_commands(bot)

@bot.event
async def on_ready():
    print(f'Bot listo como {bot.user.name}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass  # Maneja los errores según sea necesario

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot.run(BOT_TOKEN)
