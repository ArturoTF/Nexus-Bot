import discord
from discord.ext import commands
from ...environments.utils import get_user_language, translate_text, get_available_languages, get_language_from_emoji
from ...environments.connection import get_db_connection

class TraductorCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='translate')
    async def translate(self, ctx, *, message: str = None):
        db_connection = get_db_connection()
        user_language = get_user_language(ctx.author.id, db_connection)

        if message:
            translated_text = translate_text(message, user_language)
            await ctx.send(translated_text)
        else:
            async for msg in ctx.channel.history(limit=2):
                if msg.id != ctx.message.id:
                    translated_text = translate_text(msg.content, user_language)
                    await ctx.send(translated_text)
                    break

    @commands.command(name='translate_to')
    async def translate_to(self, ctx, lang_or_emoji: str, *, message: str = None):
        available_languages = get_available_languages()

        if lang_or_emoji in emoji_flags:
            dest_language = get_language_from_emoji(lang_or_emoji)
        elif lang_or_emoji in available_languages.values():
            dest_language = lang_or_emoji
        else:
            await ctx.send(f"El idioma {lang_or_emoji} no está disponible.")
            return

        if message:
            translated_text = translate_text(message, dest_language)
            await ctx.send(translated_text)
        else:
            async for msg in ctx.channel.history(limit=2):
                if msg.id != ctx.message.id:
                    translated_text = translate_text(msg.content, dest_language)
                    await ctx.send(translated_text)
                    break

def setup(bot):
    bot.add_cog(TraductorCommand(bot))
