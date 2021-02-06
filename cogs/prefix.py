import discord
import json
from discord.ext import commands

class Prefix(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('/home/runner/youtube-test-bot/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(guild.id)] = '.'

        with open('/home/runner/youtube-test-bot/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)


    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        with open('/home/runner/youtube-test-bot/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('/home/runner/youtube-test-bot/prefixes.json', 'w') as f:
            json.dump(prefixes, f)


    @commands.command()
    @commands.has_permissions(administrator=True, manage_guild=True)
    async def prefix(self, ctx, prefix):
        with open('/home/runner/youtube-test-bot/prefixes.json', 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = prefix

        with open('/home/runner/youtube-test-bot/prefixes.json', 'w') as f:
            json.dump(prefixes, f)
        await ctx.send(f'Prefix is now {prefix}!')

def setup(client):
    client.add_cog(Prefix(client))	