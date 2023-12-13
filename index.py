# index.py
from discord.ext import commands  # Agrega esta línea
from traductor.traductor import bot
from eventos.eventos import programar_evento

# Token de tu bot proporcionado por Discord Developer Portal
BOT_TOKEN = 'MTEzNTkwNDg5NzIzODMwMjcyMA.Gw0cpn.bSMuYM6cwhAjmd7TQ9p4K8XmBPWD80goDO78Mk'

@bot.command()
async def programarCanalEventos(ctx, idChannel):
    # Obtener la ID del canal desde la mención
    channel_id = int(idChannel[2:-1])  # Ignorar los primeros 2 caracteres ("<#") y el último (">")
    
    # Obtener el objeto TextChannel usando la ID del canal
    channel = bot.get_channel(channel_id)
    
    if channel and isinstance(channel, discord.TextChannel):
        print(f'Canal programado en {channel.name}')
        await programar_evento(bot, ctx, hora)
    else:
        await ctx.send("Canal no encontrado o no es un canal de texto válido.")

@bot.command()
async def programar(ctx, hora: int):
    # Asegúrate de proporcionar un ID de canal válido en la mención
    await ctx.send("Por favor, menciona un canal válido para programar el evento, por ejemplo: `!programarCanalEventos #nombre-del-canal`.")

@bot.command()
async def programar(ctx, hora: int):
    await programar_evento(bot, ctx, hora)

@bot.event
async def on_ready():
    print(f'Bot listo como {bot.user.name}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    # Puedes agregar más manejo de errores según sea necesario

bot.run(BOT_TOKEN)
