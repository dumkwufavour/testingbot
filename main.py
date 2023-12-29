import discord
from discord.ext import commands
import random
from dotenv import load_dotenv
import os


intents = discord.Intents.all()
intents.messages = True

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create an instance of the bot
bot = commands.Bot(command_prefix='!', intents=intents)

# Define a command that displays the user's name
@bot.command(name='myname')
async def display_name(ctx):
    user_name = ctx.message.author.name
    await ctx.send(f"Your Discord username is {user_name}")

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

# Run the bot with your token
bot.run(BOT_TOKEN)