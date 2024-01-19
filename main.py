import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('images/mem.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def randmem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
        #новый код    ю   ю ю ююю ю ю юююююю   ю ю  .ю юю ю  ю ю ю ю    ю ю ю ю  юю  ю ю ю ю ю ю ю ю юю ю ю ю ю  ю ю ю ю ю ю  юю ю
@bot.command()
async def river(ctx):
    with open('river/river1.jpg', 'rb') as f:
        # В переменную кладем файл, который преобразуется в файл библиотеки Discord!
        picture = discord.File(f)
   # Можем передавать файл как параметр!
    await ctx.send(file=picture)

@bot.command()
async def randriver(ctx):
    img_name = random.choice(os.listdir('river'))
    with open(f'river/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

bot.run("MTE5MzI0MTg3MzM4MTMzOTMyNg.GycTx_.wJnzq_Y5OAXbRbK93zMqda-_wNpPs8lCeUxlk8")