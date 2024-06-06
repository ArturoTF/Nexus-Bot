import discord
from discord.ext import commands
from googletrans import Translator
from ...environments.utils import emoji_flags
from ...environments.connection import create_connection, close_connection
from ...environments.logging import safe_log
from ...bot_config import bot

intents = discord.Intents.all()
intents.reactions = True

translator = Translator()

@bot.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return

    lang_code = emoji_flags.get(str(reaction.emoji))

    if lang_code is not None:
        connection = create_connection()
        try:
            original_message = reaction.message.content
            translated_text = translator.translate(original_message, src='auto', dest=lang_code).text
            await reaction.message.channel.send(f"{reaction.emoji} -> {translated_text}")
            if connection:
                safe_log(connection, "INFO", f"Mensaje traducido a {lang_code}: {translated_text}", "on_reaction_add")
        except Exception as e:
            if connection:
                safe_log(connection, "ERROR", f"Error al traducir mensaje: {e}", "on_reaction_add")
            await reaction.message.channel.send("Error al traducir el mensaje. Tienes un lenguaje establecido? /setlanguage")
        finally:
            if connection:
                close_connection(connection)
