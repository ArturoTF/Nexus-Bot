import discord
from discord.ext import commands
from googletrans import Translator
from discord.commands import slash_command, Option
from ...environments.utils import get_user_language  # Importar desde utils
from ...environments.logging import safe_log

class TraductorCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.translator = Translator()

    @slash_command(name="translate", description="Traduce un mensaje específico al idioma seleccionado.")
    async def translate(self, interaction: discord.Interaction, message: Option(str, "Pega aquí el mensaje que quieres traducir"), language: Option(str, "Elige un idioma", required=False)):
        # Determinar el idioma de destino
        if not language:
            language = await get_user_language(interaction.user.id)
            if not language:
                language = 'en'  # Idioma por defecto si no se encuentra ninguno
        # Traducir el mensaje
        translated_message = self.translator.translate(message, dest=language).text
        # Enviar el mensaje traducido
        await interaction.response.send_message(translated_message)

def setup(bot):
    bot.add_cog(TraductorCommands(bot))
