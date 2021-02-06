import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def help(self, ctx):
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



def setup(client):
	client.add_cog(HelpCommand(client))

