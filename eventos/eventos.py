# eventos.py
import discord
from discord.ext import commands
import asyncio

# Lista para rastrear a las personas que se han apuntado al evento
personas_apuntadas = []

async def programar_evento(bot, channel_id, tiempo_finalizacion, nombre_evento):
    channel = bot.get_channel(channel_id)

    if not channel:
        print(f"No se pudo encontrar el canal con ID {channel_id}")
        return

    mensaje = await channel.send(f"{nombre_evento} - Reacciona con :green_square: para apuntarte o :red_square: para ausentarte.")

    # Agregar reacciones a los mensajes para que los usuarios puedan interactuar
    await mensaje.add_reaction('🟩')  # :green_square:
    await mensaje.add_reaction('🟥')  # :red_square:

    # Función para procesar las reacciones
    def check(reaction, user):
        return user != bot.user and str(reaction.emoji) in ['🟩', '🟥']

    try:
        reaction, user = await bot.wait_for('reaction_add', timeout=tiempo_finalizacion, check=check)
        if str(reaction.emoji) == '🟩':
            print(f"{user.name} se ha apuntado al evento.")
            personas_apuntadas.append(user.name)
            await mensaje.edit(content=f"{nombre_evento} - Reacciona con :green_square: para apuntarte o :red_square: para ausentarte.\nPersonas apuntadas: {', '.join(personas_apuntadas)}")
        elif str(reaction.emoji) == '🟥':
            print(f"{user.name} no se ha apuntado al evento.")
            await mensaje.edit(content=f"{nombre_evento} - Reacciona con :green_square: para apuntarte o :red_square: para ausentarte.\nPersonas apuntadas: {', '.join(personas_apuntadas)}")
    except asyncio.TimeoutError:
        print("El tiempo para reaccionar ha expirado.")

