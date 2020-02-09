# Copyright 2020 Ngô Ngọc Đức Huy
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import discord
from discord.ext import commands
import random
from json import load

description = """An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here."""

bot = commands.Bot(command_prefix='dd ')

# Read secrets
with open('./secret/secret.json', 'r') as f:
    secret = load(f)
    token = secret['token']


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def introduce(ctx):
    """Introduces the bot"""
    await ctx.send('I will apply Google\'s algorithm *DeepDream* to your image')


@bot.command()
async def dream(ctx, image_link):
    """Apply DeepDream to your image"""
    ctx.send('Not implemented yet')


bot.run(token)
