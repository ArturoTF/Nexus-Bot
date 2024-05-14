import discord
from discord.ext import commands
from googletrans import Translator
from ...environments.utils import get_user_language # Importar desde utils
from ...environments.logging import safe_log

class TraductorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()

    @commands.slash_command(name="translate", description="Traduce el mensaje respondido al idioma establecido o seleccionado.")
    async def translate(self, ctx, language: discord.Option(str, "Elige un idioma", required=False)):
        # Recuperar el mensaje respondido
        reference = ctx.message.reference
        if reference and isinstance(reference.resolved, discord.Message):
            original_message = reference.resolved.content
            # Determinar el idioma de destino
            if not language:
                language = await get_user_language(ctx.author.id)
            # Traducir el mensaje
            translated_message = self.translator.translate(original_message, dest=language).text
            # Enviar el mensaje traducido
            await ctx.respond(translated_message)
        else:
            await ctx.respond("Por favor, responde a un mensaje para traducir.")

def setup(bot):
    bot.add_cog(TraductorCommands(bot))
