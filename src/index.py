import discord
import os
import sys
from discord.ext import commands
from app.environments.connection import create_connection, close_connection
from app.environments.logging import safe_log
from app.bot_config import bot, cargarModulos

cargarModulos()

@bot.event
async def on_ready():
    connection = create_connection()
    if connection:
        safe_log(connection, "INFO", f"Bot listo como {bot.user.name}", "on_ready")
        close_connection(connection)
    print(f'Bot listo como {bot.user.name}')
    for guild in bot.guilds:
        for channel in guild.text_channels:
            permissions = channel.permissions_for(guild.me +", ")
            print(f"Permisos en {channel.name}: {permissions}")

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
