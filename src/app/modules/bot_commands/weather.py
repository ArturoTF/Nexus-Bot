import os
import requests
import discord
from discord.ext import commands
from discord.commands import slash_command
from ...environments.logging import safe_log

WEATHER_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="weather", description="Get the current weather for a city")
    async def weather(self, ctx, city: str):
        weather_data = self.get_weather(city)
        if weather_data:
            embed = discord.Embed(
                title=f"Weather in {city}",
                description=f"{weather_data['description']}",
                color=discord.Color.blue()
            )
            embed.add_field(name="Temperature", value=f"{weather_data['temperature']}°C")
            embed.add_field(name="Humidity", value=f"{weather_data['humidity']}%")
            embed.add_field(name="Wind Speed", value=f"{weather_data['wind_speed']} m/s")
            await ctx.respond(embed=embed)
            safe_log(weather_data, "INFO", "Comando weather invocado", "weather")
        else:
            await ctx.respond(f"Could not retrieve weather data for {city}. Please try again. You can check the list of available cities here: http://bulk.openweathermap.org/sample/")
            safe_log(weather_data, "ERROR", "Error weather", "weather")

    @slash_command(name="cities", description="Get a link to the list of available cities for /weather")
    async def cities(self, ctx):
        await ctx.respond("You can check the list of available cities here: http://bulk.openweathermap.org/sample/")

    def get_weather(self, city):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_info = {
                "description": data["weather"][0]["description"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"]
            }
            return weather_info
        else:
            safe_log("Api", "ERROR", "Error weather, no se ha obtenido la solicitud", "weather")
            return None

def setup(bot):
    bot.add_cog(Weather(bot))
