import discord
from discord.ext import commands

class JoinLeave(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.channels, name='yeet')
        await channel.send(f'hey there, {member.mention}, hope you enjoy my server'
                        )


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.channels, name='general')
        await channel.send(f'{member.mention} has just left the server')


def setup(client):
    client.add_cog(JoinLeave(client))