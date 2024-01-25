import discord
import asyncio
from discord.ext import commands
import logging

welcome_channel_id = 1199815193954373735

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

try:
    token_file = open('token.txt', 'r')
    token = token_file.read()
except:
    print('No token file found. Please create a file called token.txt and place your bot token inside it.')
    exit()
else:
    print('Token file found.')

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        intents.typing = False
        intents.presences = False
        super().__init__(command_prefix="~", intents=intents)

bot = Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    bot.loop.create_task(change_status())

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(welcome_channel_id)
    await channel.send(f'{member.mention} has entered the 9 rings')

@bot.command()
async def hello(ctx):
    await ctx.send('bang')

@bot.command()
async def tester(ctx):
    await ctx.send("cock 'n' ball")

# Bot status
async def change_status():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='with fire'))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='with the damned'))
        await asyncio.sleep(5)

bot.run(token)