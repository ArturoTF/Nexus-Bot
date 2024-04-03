from discord.ext import commands
from discord.commands import slash_command  # Importa el decorador para comandos slash

def register_commands(bot):
    @bot.slash_command(name="Ceo", description="Muestra quién es el CEO")
    async def ceo(ctx):
        await ctx.respond("The CEO of this project is ArturoTF")

    @bot.slash_command(name="Languages", description="Muestra los idiomas disponibles para traducción")
    async def languages(ctx):
        languages = "🇬🇧, 🇪🇸, 🇩🇪, 🇷🇺, 🇵🇹, 🇻🇳, 🇨🇳, 🇮🇹, 🇺🇸, 🇵🇱"
        await ctx.respond(f"Languages ​​available for translation: {languages}")
