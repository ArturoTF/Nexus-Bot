# index.py
from traductor.traductor import bot
from eventos.eventos import programar_evento

@bot.event
async def on_ready():
    print(f'Bot listo!!!')
    await programar_evento(bot, channel_id=Tu_ID_de_Canal, hora=3600)  # 3600 segundos = 1 hora


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        pass
    # Puedes agregar más manejo de errores según sea necesario

# Token de tu bot proporcionado por Discord Developer Portal
BOT_TOKEN = 'MTEzNTkwNDg5NzIzODMwMjcyMA.Gg-DXn.s_OpKtFzO0wIrMOvR5AqLT_tSh0BArqDIlj6Nk'
bot.run(BOT_TOKEN)
