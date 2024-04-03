from discord.ext import commands
from discord.commands import slash_command  # Importa el decorador para comandos slash

def register_commands(bot):
    @bot.slash_command(name="ceo", description="Muestra quién es el CEO")
    async def ceo(ctx):
        await ctx.respond("El CEO es ArturoTF")

    @bot.slash_command(name="languages", description="Muestra los idiomas disponibles para traducción")
    async def languages(ctx):
        languages = "🇬🇧, 🇪🇸, 🇩🇪, 🇷🇺, 🇵🇹, 🇻🇳, 🇨🇳, 🇮🇹, 🇺🇸, 🇵🇱"
        await ctx.respond(f"Idiomas disponibles para traducción: {languages}")
