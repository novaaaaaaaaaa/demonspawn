import discord
import asyncio
from discord.ext import commands
import logging

logger = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

try:
    token_file = open('token.txt', 'r')
    token = token_file.read()
except:
    print('No token file found. Please create a file called token.txt and place your bot token inside it.')
    exit()
else:
    print('Token file found.')

intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('bang')

@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel is not None:
        await channel.send(f'{member.name} has entered the 9 rings')

client.run(token, log_handler=logger)




# class my_client(discord.Client):
#     async def on_ready(self):
#         print(f'Logged in as {self.user}')

#     async def on_message(self, message):
#         print(f'Mesage from {message.author}: {message.content}')



# intents = discord.Intents.default()
# intents.message_content = True

# client = my_client(intents=intents)
# client.run(token)