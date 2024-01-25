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

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        intents.typing = False
        intents.presences = False

        super().__init__(command_prefix="!", intents=intents)

bot = MyBot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    bot.loop.create_task(change_status())

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('bang')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(welcome_channel_id)
    await channel.send(f'{member.mention} has entered the 9 rings')

# Bot status
async def change_status():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='with fire'))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='with the damned'))
        await asyncio.sleep(5)

bot.run(token)




# class my_client(discord.Client):
#     async def on_ready(self):
#         print(f'Logged in as {self.user}')

#     async def on_message(self, message):
#         print(f'Mesage from {message.author}: {message.content}')



# intents = discord.Intents.default()
# intents.message_content = True

# client = my_client(intents=intents)
# client.run(token)