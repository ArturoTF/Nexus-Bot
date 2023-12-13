# index.py
from discord.ext import commands  # Agrega esta línea
from traductor.traductor import bot
from eventos.eventos import programar_evento

# Token de tu bot proporcionado por Discord Developer Portal
BOT_TOKEN = 'MTEzNTkwNDg5NzIzODMwMjcyMA.Gw0cpn.bSMuYM6cwhAjmd7TQ9p4K8XmBPWD80goDO78Mk'

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
