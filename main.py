import discord
from discord.ext import commands
from json import load

bot = commands.Bot(command_prefix='>')

# Read secrets
with open('./secret/secret.json', 'r') as f:
    secret = load(f)
    token = secret['token']


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)
