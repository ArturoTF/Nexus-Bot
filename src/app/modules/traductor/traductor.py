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

        # Obtener el código de idioma correcto desde emoji_flags
        lang_code = emoji_flags.get(str(reaction.emoji))

        if lang_code is not None:
            connection = create_connection()
            try:
                original_message = reaction.message.content
                if not original_message:
                    raise ValueError("El mensaje original está vacío o es None")

                safe_log(connection, "INFO", f"Mensaje original: {original_message}", "on_reaction_add")
                
                # Asegurarse de que lang_code sea el código de idioma correcto
                safe_log(connection, "INFO", f"Código de idioma detectado: {lang_code}", "on_reaction_add")
                
                translation_result = translator.translate(original_message, src='auto', dest=lang_code)
                if not translation_result or not translation_result.text:
                    raise ValueError("El resultado de la traducción es vacío o None")

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
        else:
            await reaction.message.channel.send("El emoji no está asociado a ningún código de idioma.")

def setup(bot):
    bot.add_cog(Traductor(bot))
