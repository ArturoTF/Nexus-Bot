# eventos.py
import discord
from discord.ext import commands
import asyncio

async def programar_evento(bot, channel_id, hora):
    channel = bot.get_channel(channel_id)

    if not channel:
        print(f"No se pudo encontrar el canal con ID {channel_id}")
        return

    mensaje = await channel.send("Reacciona con :green_square: para apuntarte o :red_square: para no apuntarte.")

    # Agregar reacciones a los mensajes para que los usuarios puedan interactuar
    await mensaje.add_reaction('🟩')  # :green_square:
    await mensaje.add_reaction('🟥')  # :red_square:

    # Función para procesar las reacciones
    def check(reaction, user):
        return user != bot.user and str(reaction.emoji) in ['🟩', '🟥']

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=hora, check=check)
        if str(reaction.emoji) == '🟩':
            print(f"{user.name} se ha apuntado al evento.")
            # Agregar lógica para agregar a la lista de apuntados
        elif str(reaction.emoji) == '🟥':
            print(f"{user.name} no se ha apuntado al evento.")
            # Agregar lógica para agregar a la lista de no apuntados
    except asyncio.TimeoutError:
        print("El tiempo para apuntarse ha expirado.")

