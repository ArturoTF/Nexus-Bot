import discord
from discord.ext import commands  # No cambia, py-cord usa el mismo espacio de nombres
from googletrans import Translator
from ...environments.logging import safe_log  

intents = discord.Intents.all()
intents.reactions = True

# La inicialización del bot permanece igual en py-cord
bot = commands.Bot(command_prefix='/', intents=intents)
translator = Translator()

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    emoji_flags = {
        '🇬🇧': 'en',
        '🇪🇸': 'es',
        '🇩🇪': 'de',
        '🇷🇺': 'ru',
        '🇵🇹': 'pt',
        '🇻🇳': 'vi',
        '🇨🇳': 'zh-cn',
        '🇮🇹': 'it',
        '🇫🇷': 'fr',
        '🇵🇱': 'pl',
        '🇺🇸': 'en',
        '🇷🇸': 'sr',
        '🇯🇵': 'ja',
    }

    lang_code = emoji_flags.get(str(reaction.emoji))

    if lang_code is not None:
        try:
            original_message = reaction.message.content
            translated_text = translator.translate(original_message, src='auto', dest=lang_code).text
            await reaction.message.channel.send(f"{reaction.emoji} -> {translated_text}")
            # safe_log("INFO", f"Mensaje traducido a {lang_code}: {translated_text}", "on_reaction_add")
        except Exception as e:
            safe_log("ERROR", f"Error al traducir mensaje: {e}", "on_reaction_add")
            await reaction.message.channel.send("Error al traducir el mensaje.")


