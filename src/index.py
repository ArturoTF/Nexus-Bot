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
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        safe_log("WARNING", f"Comando no encontrado: {ctx.invoked_with}", "on_command_error")
    else:
        safe_log("ERROR", f"Error inesperado en comando: {str(error)}", "on_command_error")



BOT_TOKEN = os.getenv("BOT_TOKEN")
bot.run(BOT_TOKEN)
