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


@client.command()
async def hello(ctx):
    await ctx.send('hello')


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='yeet')
    await channel.send(f'hey there, {member.mention}, hope you enjoy my server'
                       )


@client.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.channels, name='general')
    await channel.send(f'{member.mention} has just left the server')


@client.command()
async def help(ctx):
    embed = discord.Embed(color=discord.Colour.teal())

    embed.add_field(
        value='`.hello`', 
        name='client replies with hello', 
        inline=False)
    embed.add_field(
        value='`.ping`', name='Latency of the client.', inline=False)
    embed.add_field(
        value='`.embed`', name='client replies with an embed', inline=False)
    embed.add_field(
        value='`.prefix`', name='change prefix', inline=False)
    await ctx.send(embed=embed)



@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f'I have deleted `{amount} messages!`')
    await asyncio.sleep(2)
    await ctx.channel.purge(limit=amount)



@client.command()
async def dm(ctx,member:discord.Member):
    await ctx.send('what do you want to say')
    def check(m):
        return m.author.id == ctx.author.id

    message = await client.wait_for('message', check=check)
    await ctx.send(f'sent message to {member}')

    await member.send(f'{ctx.author.mention} Has a message for you:\n{message.content}')

@client.command()
async def edit_message(ctx, content1, time:int, content2):
    msg = await ctx.send(content1)
    await asyncio.sleep(time)
    await msg.edit(content=content2)


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
