import discord
import asyncio
import os
import keep_alive
import json
import datetime
from discord.ext import commands


def get_prefix(client, message):
    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)]


client = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all())
client.remove_command('help')
token = os.environ.get("DISCORD_BOT_SECRET")





@client.event
async def on_ready():
    print('client is online')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{len(client.guilds)} servers | {len(client.users)} users | Type .help for commands'))





for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


def is_it_me(ctx):
    return ctx.author.id == 475315771086602241

@client.command()
@commands.check(is_it_me)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'unloaded and loaded {extension}')

  


keep_alive.keep_alive()
client.run(token)
