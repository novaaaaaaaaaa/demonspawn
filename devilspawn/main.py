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

intents = discord.Intents.default()
intents.members = True  # Enable the members intent
intents.message_content = True
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

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