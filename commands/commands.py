from discord_slash.utils.manage_commands import create_option, create_choice

def register_commands(slash):
    @slash.slash(
        name="ceo",
        description="Muestra quién es el CEO",
        options=[]
    )
    async def ceo(ctx):
        await ctx.send("El CEO es ArturoTF")

    @slash.slash(
        name="languages",
        description="Muestra los idiomas disponibles para traducción",
        options=[]
    )
    async def languages(ctx):
        languages = "🇬🇧, 🇪🇸, 🇩🇪, 🇷🇺, 🇵🇹, 🇻🇳, 🇨🇳, 🇮🇹, 🇺🇸, 🇵🇱"
        await ctx.send(f"Idiomas disponibles para traducción: {languages}")

