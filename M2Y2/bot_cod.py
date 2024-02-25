import random
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def rec(ctx):
    recomm = ['Сортируйте мусор и выбрасывайте его по отдельности','Занимайтесь облагораживанием своего города','Экономьте топливо','Снижайте потребление электроэнергии','Экономьте воду']
    i = (random.choice(recomm))
    await ctx.send(f'Совет:{i}!')