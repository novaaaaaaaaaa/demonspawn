import discord
import asyncio
from discord.ext import commands
from discord import app_commands
import logging
import requests

welcome_channel_id = 1199815193954373735

pokeapi_base_url = 'https://pokeapi.co/api/v2/pokemon/'

marvel_api_base_url = 'http://gateway.marvel.com/v1/public/'

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


try:
    with open('guild.txt', 'r') as file:
        guildID = file.read().replace('\n', '')
except OSError:
    print("Could not find guild.txt, please create it and place your guild ID inside.")
    exit()
else:
    print("Guild ID loaded successfully.")

try:
    with open('marvel_api_hash.txt', 'r') as file:
        marvelapihash = file.read().replace('\n', '')
except OSError:
    print("Could not find marvel_api_hash.txt, please create and place your marvel API hash inside.")
    exit()
else:
    print("marvel API hash loaded successfully.")

try:
    with open('marvel_api_key.txt', 'r') as file:
        marvelapikey = file.read().replace('\n', '')
except OSError:
    print("Could not find marvel_api_key.txt, please create it and place your marvel API key inside.")
    exit()
else:
    print("marvel API key loaded successfully.")

class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True
        intents.typing = False
        intents.presences = False
        super().__init__(command_prefix="~", intents=intents)
        
    async def setup_hook(self):
        await self.tree.sync(guild = discord.Object(id = guildID))
        print(f"Synced slash commands for {self.user}.")
    
    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral = True)

bot = Bot()


# Bot events
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    bot.loop.create_task(change_status())

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(welcome_channel_id)
    await channel.send(f'{member.mention} has entered the 9 rings')


# Bot slash commands
@bot.hybrid_command(name = "test", with_app_command = True, description = "Testing")
@app_commands.guilds(discord.Object(id = guildID))
@commands.has_permissions(administrator = True)
async def test(ctx: commands.Context):
    # await ctx.defer(ephemeral = True)
    await ctx.reply("Test working")

@bot.hybrid_command(name='pokemonstats', with_app_command=True, description='Get stats for a Pokemon')
@app_commands.guilds(discord.Object(id=guildID))
async def pokemonstats(ctx: commands.Context, *, arg):
    pokemon_name = arg

    pokeapi_response = requests.get(f'{pokeapi_base_url}{pokemon_name}')

    print(type(pokemon_name))
    pokemon_name = pokemon_name.capitalize()
    pokeapi_data = pokeapi_response.json()

    pokemon_hp = pokeapi_data['stats'][0]['base_stat']
    pokemon_attack = pokeapi_data['stats'][1]['base_stat']
    pokemon_defence = pokeapi_data['stats'][2]['base_stat']
    pokemon_sp_attack = pokeapi_data['stats'][3]['base_stat']
    pokemon_sp_defence = pokeapi_data['stats'][4]['base_stat']
    pokemon_speed = pokeapi_data['stats'][5]['base_stat']

    pokemon_bst = pokemon_hp + pokemon_attack + pokemon_defence + pokemon_sp_attack + pokemon_sp_defence + pokemon_speed

    await ctx.reply(f'Pokemon stats - {pokemon_name}\n\t--Base Stat Total: {pokemon_bst}\n\t--HP: {pokemon_hp}\n\t--Attack: {pokemon_attack}\n\t--Defence: {pokemon_defence}\n\t--Special Attack: {pokemon_sp_attack}\n\t--Special Defence: {pokemon_sp_defence}\n\t--Speed: {pokemon_speed}')

@bot.hybrid_command(name='marvelcharname', with_app_command=True, description='Just gets all times characters appear')
@app_commands.guilds(discord.Object(id=guildID))
async def marvelcharname(ctx: commands.Context, *, arg):
    char_name = arg

    marvel_api_response = requests.get(f'{marvel_api_base_url}/characters?ts=1&apikey={marvelapikey}&hash={marvelapihash}&name={char_name}')

    print(marvel_api_response)

    char_name = char_name.capitalize()
    marvel_api_data = marvel_api_response.json()

    comics_num = marvel_api_data['data']['results'][0]['comics']['available']
    series_num = marvel_api_data['data']['results'][0]['series']['available']
    stories_num = marvel_api_data['data']['results'][0]['stories']['available']
    events_num = marvel_api_data['data']['results'][0]['events']['available']

    await ctx.reply(f'Character appearances - {char_name}:\n\t--Comic appearances: {comics_num}\n\t--Series appearances: {series_num}\n\t--Story appearances: {stories_num}\n\t--Event appearances: {events_num}')

# Bot commands
@bot.command()
async def hello(ctx):
    await ctx.send('bang')

@bot.command()
async def tester(ctx):
    await ctx.send("cock 'n' ball")

@bot.command()
async def pokemon(ctx, *, arg):
    pokemon_id = arg

    pokeapi_response = requests.get(f'{pokeapi_base_url}{pokemon_id}')

    pokeapi_data = pokeapi_response.json()

    pokemon_name = pokeapi_data['name']

    await ctx.send(f'Pokemon name: {pokemon_name}')


# Bot status
async def change_status():
    while True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='with fire'))
        await asyncio.sleep(5)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='with the damned'))
        await asyncio.sleep(5)

bot.run(token)