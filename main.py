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


client = commands.Bot(command_prefix=get_prefix, intents=discord.Intents.all(), owner_id=475315771086602241)
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
    return ctx.author.id == client.owner_id

@client.command()
@commands.check(is_it_me)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print(f'unloaded and loaded {extension}')

@client.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.reply("You are missing a required argument.")
	
	if isinstance(error, commands.MissingPermissions):
		if len(error.missing_perms) == 1:
			perms = ''.join(error.missing_perms)
		else:
			perms = ', '.join(error.missing_perms)
		await ctx.reply(f"You need the following perms: `{perms}`.")

	if isinstance(error, commands.BotMissingPermissions):
		if len(error.missing_perms) == 1:
			perms = ''.join(error.missing_perms)
		else:
			perms = ', '.join(error.missing_perms)
		await ctx.reply(f"I need the following perms: `{perms}`.")


	mythify = client.get_user(client.owner_id)
	await mythify.send(f"Error in **{ctx.guild.name}**:\n```{str(error)}```")
	raise error

keep_alive.keep_alive()
client.run(token)
