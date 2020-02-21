import os
import random
import math

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='nim')
async def play_nim(ctx):
    await ctx.send("Still working on it, kiddo.")

@bot.command(name="flip_coin")
async def flip_coin(ctx):
    await ctx.send(random.choice(["Heads", "Tails"]))

@bot.command(name="average")
async def average(ctx, *args):
    await ctx.send( sum(args)/2 )

@bot.command(name="birthday_color")
async def birthday_color(ctx, month):
    month = month.lower()
    unwanted = "!@#$%^&*(),./[]"
    colors = {"january": "Brown", 
              "feburary": "Purple", 
              "march": "Baby Blue", 
              "april": "Light Red",
              "may": "Green",
              "june": "Yellow",
              "july": "Pink",
              "august": "Orange",
              "september": "Navy Blue",
              "october": "Light Blue",
              "november": "Maroon",
              "december": "Bayou"}
    for char in unwanted:
        month = month.replace(char, "")              
    if month not in colors.keys():
        await ctx.send("Please use a valid month.")
    else:
        await ctx.send(colors[month])

bot.run(token)
# this is cool I guess - Iris
