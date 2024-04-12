from discord.ext import commands
from discord.commands import slash_command, Option  # Importa Option para las opciones del comando slash
import discord

# Aquí agregarías las importaciones de tus funciones de conexión a la base de datos
from app.environments.connection import create_connection, close_connection

def register_commands(bot):
    @bot.slash_command(name="ceo", description="Muestra quién es el CEO")
    async def ceo(ctx):
        await ctx.respond("The CEO of this project is ArturoTF")

    @bot.slash_command(name="languages", description="Muestra los idiomas disponibles para traducción")
    async def languages(ctx):
        languages = "🇬🇧, 🇪🇸, 🇩🇪, 🇷🇺, 🇵🇹, 🇻🇳, 🇨🇳, 🇮🇹, 🇺🇸, 🇵🇱,🇺🇸,🇷🇸,🇯🇵"
        await ctx.respond(f"Languages ​​available for translation: {languages}")

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


    @bot.slash_command(
        name="language",
        description="Select your language",
        options=[
            Option(
                name="idioma",
                description="Elige tu idioma",
                required=True,
                choices=[discord.OptionChoice(name=lang, value=flag) for lang, flag in language_options.items()],
            ),
        ]
    )
    async def language(ctx, idioma: str):
        # Aquí se maneja el comando y se guarda en la base de datos
        user_id = ctx.author.id
        user_name = ctx.author.name
        language_flag = idioma
        language_name = [lang for lang, flag in language_options.items() if flag == idioma][0]

        # Conecta a la base de datos y guarda la selección del idioma
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO usuarios_idioma (name, idioma) VALUES (%s, %s) ON DUPLICATE KEY UPDATE idioma = %s", 
            (user_name, language_name, language_name)
        )   

        connection.commit()
        close_connection(connection)

        # Envía una respuesta al usuario con la bandera del idioma seleccionado
        await ctx.respond(f"{ctx.author.mention}, tu idioma se ha establecido a {language_flag}")
