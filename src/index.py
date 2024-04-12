import discord
import os
from app.modules.traductor.traductor import bot
from discord import SlashCommand  # Esto ahora viene de una extensión compatible
from app.modules.bot_commands.basicCommands import register_commands
from discord.ext import commands
from app.environments.connection import create_connection, close_connection
from app.environments.logging import safe_log


# No es necesario inicializar 'bot' de nuevo si ya lo has hecho en traductor.traductor
# Sólo asegúrate de que 'intents' estén correctamente configurados allí

# Registra tus comandos slash utilizando la función adaptada a py-cord
register_commands(bot)

@bot.event
async def on_ready():
    connection = create_connection()
    if connection:
        safe_log(connection, "INFO", f"Bot listo como {bot.user.name}", "on_ready")
        close_connection(connection)
    print(f'Bot listo como {bot.user.name}')
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
