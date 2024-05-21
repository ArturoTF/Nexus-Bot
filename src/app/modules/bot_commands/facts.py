import requests
import discord
from discord.ext import commands
from discord.commands import slash_command

class Facts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.available_topics = ["trivia", "math", "date", "year"]

    @slash_command(name="facts", description="Muestra datos curiosos o educativos sobre diferentes temas.")
    async def facts(self, ctx, tema: str):
        if tema.lower() not in self.available_topics:
            await ctx.respond(f"El tema '{tema}' no está disponible. Usa `/list_topics` para ver los temas disponibles.")
            return

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

    @slash_command(name="list_topics", description="Muestra una lista de los temas disponibles para el comando /facts.")
    async def list_topics(self, ctx):
        topics = ", ".join(self.available_topics)
        embed = discord.Embed(
            title="Available Topics",
            description=f"The following topics are available for the /facts command: {topics}",
            color=discord.Color.blue()
        )
        await ctx.respond(embed=embed)

    def get_fact(self, tema):
        url = f"http://numbersapi.com/random/{tema}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None

def setup(bot):
    bot.add_cog(Facts(bot))
