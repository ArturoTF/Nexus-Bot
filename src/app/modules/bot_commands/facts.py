import requests
import discord
from discord.ext import commands
from discord.commands import slash_command

class Facts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="facts", description="Muestra datos curiosos o educativos sobre diferentes temas.")
    async def facts(self, ctx, tema: str):
        fact = self.get_fact(tema)
        if fact:
            embed = discord.Embed(
                title=f"Curious Fact about {tema.capitalize()}",
                description=f"{fact}",
                color=discord.Color.green()
            )
            await ctx.respond(embed=embed)
        else:
            await ctx.respond(f"Could not retrieve a fact about {tema}. Please try another topic.")

    def get_fact(self, tema):
        url = f"http://numbersapi.com/random/{tema}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None

def setup(bot):
    bot.add_cog(Facts(bot))
