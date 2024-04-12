import discord
import os
from app.modules.traductor.traductor import bot
from discord import SlashCommand  # Esto ahora viene de una extensión compatible
from app.modules.bot_commands.basicCommands import register_commands
from discord.ext import commands

# No es necesario inicializar 'bot' de nuevo si ya lo has hecho en traductor.traductor
# Sólo asegúrate de que 'intents' estén correctamente configurados allí

# Registra tus comandos slash utilizando la función adaptada a py-cord
register_commands(bot)

@bot.event
async def on_ready():
    print(f'Bot listo como {bot.user.name}')
    await bot.sync_commands()

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass  # Aquí puedes manejar errores específicos o personalizados según necesites


BOT_TOKEN = os.getenv("BOT_TOKEN")
bot.run(BOT_TOKEN)
