import os
import requests
import discord
from discord.ext import commands
from discord.commands import slash_command
from ...environments.logging import safe_log


NEWS_API_KEY = os.getenv('NEWS_API_KEY')

class News(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="news", description="Get the latest news headlines")
    async def news(self, ctx):
        news_data = self.get_news()
        if news_data:
            embed = discord.Embed(
                title="Latest News Headlines",
                description="Here are the top news headlines:",
                color=discord.Color.blue()
            )
            for article in news_data[:5]:
                embed.add_field(
                    name=article['title'],
                    value=f"[Read more]({article['url']})",
                    inline=False
                )
            await ctx.respond(embed=embed)
            # safe_log(news_data, "INFO", "Comando news invocado", "news")
        else:
            await ctx.respond("Could not retrieve news. Please try again later.")
            safe_log(news_data, "ERROR", "error en news", "news")

    def get_news(self):
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['articles']
        else:
            safe_log("Api Error", "ERROR", "Comando news, no se ha obtenido la solicitud", "news")
            return None
def setup(bot):
    bot.add_cog(News(bot))
