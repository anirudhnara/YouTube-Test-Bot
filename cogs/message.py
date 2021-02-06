import discord
import asyncio
from discord.ext import commands

class Message(commands.Cog):
	def __init__(self, client):
		self.client = client
	
	@commands.command()
	@commands.bot_has_permissions(manage_guild=True)
	async def dm(self, ctx,member:discord.Member):
		await ctx.send('what do you want to say')
		def check(m):
			return m.author.id == ctx.author.id

		message = await self.client.wait_for('message', check=check)
		await ctx.send(f'sent message to {member}')

		await member.send(f'{ctx.author.mention} Has a message for you:\n{message.content}')

	@commands.command()
	@commands.has_permissions(manage_messages=True)
	async def edit_message(self, ctx, content1, time:int, content2):
		msg = await ctx.send(content1)
		await asyncio.sleep(time)
		await msg.edit(content=content2)
	

def setup(client):
	client.add_cog(Message(client))