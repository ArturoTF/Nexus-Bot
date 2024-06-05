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
            permissions = channel.permissions_for(guild.me)
            print(f"Permisos en {channel.name}: {permissions.value}")
            check_permissions(permissions.value)

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

def check_permissions(permissions_value):
    permissions = {
        'CREATE_INSTANT_INVITE': 1 << 0,
        'KICK_MEMBERS': 1 << 1,
        'BAN_MEMBERS': 1 << 2,
        'ADMINISTRATOR': 1 << 3,
        'MANAGE_CHANNELS': 1 << 4,
        'MANAGE_GUILD': 1 << 5,
        'ADD_REACTIONS': 1 << 6,
        'VIEW_AUDIT_LOG': 1 << 7,
        'PRIORITY_SPEAKER': 1 << 8,
        'STREAM': 1 << 9,
        'READ_MESSAGES': 1 << 10,
        'SEND_MESSAGES': 1 << 11,
        'SEND_TTS_MESSAGES': 1 << 12,
        'MANAGE_MESSAGES': 1 << 13,
        'EMBED_LINKS': 1 << 14,
        'ATTACH_FILES': 1 << 15,
        'READ_MESSAGE_HISTORY': 1 << 16,
        'MENTION_EVERYONE': 1 << 17,
        'USE_EXTERNAL_EMOJIS': 1 << 18,
        'VIEW_GUILD_INSIGHTS': 1 << 19,
        'CONNECT': 1 << 20,
        'SPEAK': 1 << 21,
        'MUTE_MEMBERS': 1 << 22,
        'DEAFEN_MEMBERS': 1 << 23,
        'MOVE_MEMBERS': 1 << 24,
        'USE_VAD': 1 << 25,
        'CHANGE_NICKNAME': 1 << 26,
        'MANAGE_NICKNAMES': 1 << 27,
        'MANAGE_ROLES': 1 << 28,
        'MANAGE_WEBHOOKS': 1 << 29,
        'MANAGE_EMOJIS_AND_STICKERS': 1 << 30,
        'USE_APPLICATION_COMMANDS': 1 << 31,
        'REQUEST_TO_SPEAK': 1 << 32,
        'MANAGE_EVENTS': 1 << 33,
        'MANAGE_THREADS': 1 << 34,
        'CREATE_PUBLIC_THREADS': 1 << 35,
        'CREATE_PRIVATE_THREADS': 1 << 36,
        'USE_EXTERNAL_STICKERS': 1 << 37,
        'SEND_MESSAGES_IN_THREADS': 1 << 38,
        'USE_EMBEDDED_ACTIVITIES': 1 << 39,
        'MODERATE_MEMBERS': 1 << 40
    }

    required_permissions = [
        'READ_MESSAGES',
        'SEND_MESSAGES',
        'ADD_REACTIONS',
        'READ_MESSAGE_HISTORY'
    ]

    for perm in required_permissions:
        if permissions_value & permissions[perm] != permissions[perm]:
            print(f"Falta el permiso: {perm}")

BOT_TOKEN = os.getenv("BOT_TOKEN")
bot.run(BOT_TOKEN)
