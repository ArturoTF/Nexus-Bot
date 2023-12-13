# index.py
from discord.ext import commands  # Agrega esta línea
from traductor.traductor import bot
# from eventos.eventos import programar_evento     

# Token de tu bot proporcionado por Discord Developer Portal
BOT_TOKEN = 'MTEzNTkwNDg5NzIzODMwMjcyMA.Gw0cpn.bSMuYM6cwhAjmd7TQ9p4K8XmBPWD80goDO78Mk'

# Variable global para almacenar la ID del canal
canal_id_eventos = None

@bot.command()
async def configurarCanalEventos(ctx, idChannel):
    global canal_id_eventos
    try:
        # Obtener la ID del canal desde la mención
        canal_id_eventos = int(idChannel[2:-1])  # Ignorar los primeros 2 caracteres ("<#") y el último (">")

        # Obtener el objeto TextChannel usando la ID del canal
        channel = bot.get_channel(canal_id_eventos)

        if channel and isinstance(channel, discord.TextChannel):
            print(f'Canal de eventos configurado en {channel.name}. ID: {canal_id_eventos}')
            await ctx.send(f"Canal de eventos configurado en {channel.name}. ID: {canal_id_eventos}")
        else:
            await ctx.send("Canal no encontrado o no es un canal de texto válido.")
    except Exception as e:
        print(f"Error durante la configuración del canal de eventos: {e}")
        await ctx.send("Hubo un error durante la configuración del canal de eventos.")


@bot.command()
async def programar(ctx, nombre_evento, tiempo_finalizacion: int):
    global canal_id_eventos
    if canal_id_eventos is None:
        await ctx.send("Por favor, primero configura un canal para eventos usando !configurarCanalEventos.")
        return
    
    channel = bot.get_channel(canal_id_eventos)
    if not channel or not isinstance(channel, discord.TextChannel):
        await ctx.send("Canal no encontrado o no es un canal de texto válido.")
        return
    
    # Llama a la función actualizada de programar_evento con la ID del canal y el nombre del evento
    await programar_evento(bot, canal_id_eventos, tiempo_finalizacion, nombre_evento)

@bot.event
async def on_ready():
    print(f'Bot listo como {bot.user.name}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    # Puedes agregar más manejo de errores según sea necesario

bot.run(BOT_TOKEN)
