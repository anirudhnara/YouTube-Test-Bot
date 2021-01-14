import asyncio
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
    
    
    @commands.command()
    async def hello(self, ctx):
        await ctx.send('hello')




    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=3):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'I have deleted `{amount} messages!`')
        await asyncio.sleep(2)
        await ctx.channel.purge(limit=1)

def setup(client):
    client.add_cog(TestCog(client))