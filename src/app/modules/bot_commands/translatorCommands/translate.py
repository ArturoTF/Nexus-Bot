import discord
from discord.ext import commands
from googletrans import Translator
from discord.commands import slash_command, Option
from ....environments.utils import get_user_language
from ....environments.connection import create_connection, close_connection
from ....environments.logging import safe_log

class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()

    @slash_command(name="translate", description="Traduce un mensaje específico al idioma seleccionado.")
    async def translate(self, ctx, message: Option(str, "Pega aquí el mensaje que quieres traducir")):
        user_id = ctx.author.id
        print(user_id)
        
        connection = create_connection()
        if connection:
            try:
                target_language = get_user_language(user_id)
                if not target_language:
                    target_language = 'en' 
                print(target_language)
                translated_message = self.translator.translate(message, dest=target_language).text
                print(translated_message)
                await ctx.respond(translated_message)

                # safe_log(connection, "INFO", f"Mensaje traducido a {target_language}: {translated_message}", "translate")
                
            except Exception as e:
                safe_log(connection, "ERROR", f"Error en translate: {e}", "translate")
                await ctx.respond("Error al traducir el mensaje.  Tienes un lenguaje establecido? /setlanguage")
            finally:
                close_connection(connection)
        else:
            await ctx.respond("Error al conectar con la base de datos.")

def setup(bot):
    bot.add_cog(Translate(bot))
