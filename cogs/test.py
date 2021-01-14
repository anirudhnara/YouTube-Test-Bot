import discord
from discord.ext import commands

class TestCog(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self, ctx):
        latency = self.client.latency
        trueLatency = latency * 1000
        await ctx.send(f'It takes me {round(trueLatency)} milliseconds to respond.'
                    )
    
    @commands.Cog.listener()
    async def on_message(self, message):
        print(f"{message.author} said {message.content}")

def setup(client):
    client.add_cog(TestCog(client))