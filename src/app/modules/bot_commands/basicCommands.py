from discord.ext import commands
from discord.commands import slash_command, Option, OptionChoice  # Importaciones necesarias para los comandos slash
import discord
# Importaciones de tus funciones de conexión a la base de datos
from ...environments.connection import create_connection, close_connection

def register_commands(bot):
    @bot.slash_command(name="ceo", description="Muestra quién es el CEO")
    async def ceo(ctx):
        await ctx.respond("The CEO of this project is ArturoTF")

    @bot.slash_command(name="languages", description="Muestra los idiomas disponibles para traducción")
    async def languages(ctx):
        language_list = "🇬🇧, 🇪🇸, 🇩🇪, 🇷🇺, 🇵🇹, 🇻🇳, 🇨🇳, 🇮🇹, 🇺🇸, 🇵🇱,🇺🇸,🇷🇸,🇯🇵"
        await ctx.respond(f"Languages available for translation: {language_list}")

    # Diccionario de opciones de idiomas y sus banderas
    language_options = {
    'English': '🇬🇧',
    'Spanish': '🇪🇸',
    'German': '🇩🇪',
    'Russian': '🇷🇺',
    'Portuguese': '🇵🇹',
    'Vietnamese': '🇻🇳',
    'Chinese': '🇨🇳',
    'Italian': '🇮🇹',
    'French': '🇫🇷',
    'Polish': '🇵🇱',
    'American English': '🇺🇸',
    'Serbian': '🇷🇸',
    'Japanese': '🇯🇵',
    }


    @bot.slash_command(name="language", description="Select your language")
    async def language(ctx, idioma: discord.Option(str, "Elige tu idioma", choices=[OptionChoice(name=f"{name} {flag}", value=name) for name, flag in language_options.items()])):
        # Aquí se maneja el comando y se guarda en la base de datos
        user_name = ctx.author.name

        # Conecta a la base de datos y guarda la selección del idioma
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO usuarios_idioma (name, idioma) VALUES (%s, %s) ON DUPLICATE KEY UPDATE idioma = %s",
            (user_name, idioma, idioma)
        )
        connection.commit()
        close_connection(connection)

        # Envía una respuesta al usuario con la bandera del idioma seleccionado
        await ctx.respond(f"{ctx.author.mention}, tu idioma se ha establecido a {language_options[idioma]}")

