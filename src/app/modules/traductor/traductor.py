import discord
from discord.ext import commands
from googletrans import Translator
from ...environments.utils import emoji_flags
from ...environments.connection import create_connection, close_connection
from ...environments.logging import safe_log

intents = discord.Intents.all()
intents.reactions = True

bot = commands.Bot(command_prefix='/', intents=intents)
translator = Translator()

class Traductor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.bot:
            return

        lang_code = emoji_flags.get(str(reaction.emoji))

        if lang_code is not None:
            connection = create_connection()
            try:
                original_message = reaction.message.content
                if original_message is None:
                    raise ValueError("Mensaje original es None")
                
                safe_log(connection, "INFO", f"Mensaje original: {original_message}", "on_reaction_add")
                
                translation_result = translator.translate(original_message, src='auto', dest=lang_code)
                if translation_result is None or translation_result.text is None:
                    raise ValueError("Resultado de la traducción es None")
                
                translated_text = translation_result.text
                safe_log(connection, "INFO", f"Texto traducido: {translated_text}", "on_reaction_add")
                
                await reaction.message.channel.send(f"{reaction.emoji} -> {translated_text}")
                if connection:
                    safe_log(connection, "INFO", f"Mensaje traducido a {lang_code}: {translated_text}", "on_reaction_add")
            except Exception as e:
                if connection:
                    safe_log(connection, "ERROR", f"Error al traducir mensaje: {e}", "on_reaction_add")
                await reaction.message.channel.send("Error al traducir el mensaje.")
            finally:
                if connection:
                    close_connection(connection)

def setup(bot):
    bot.add_cog(Traductor(bot))
