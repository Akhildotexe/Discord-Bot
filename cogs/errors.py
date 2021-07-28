import discord
from discord import Embed
from discord.ext import commands
from datetime import datetime, timedelta

class colc(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.Cog.listener()
  async def on_command_error(self, ctx, error): 
    if isinstance(error, commands.MissingRequiredArgument): 
        mra = discord.Embed(title=f"Error!!!", description=f" `{error}`", color=0xff0000) 
        await ctx.reply(embed=mra)
    elif isinstance(error, commands.MissingPermissions): 
        cmp = discord.Embed(title=f":x: Missing perms", description=f"`{error}`", color=0xff0000)  
        await ctx.reply(embed=cmp)
    elif isinstance(error, commands.CommandNotFound): 
        cnt = discord.Embed(title=f":x: Invalid command used", description=f" `{error}`,pls enter a valid cmd or `,help`", color=0xff0000) 
        await ctx.reply(embed=cnt)
    else:
        raise error

def setup(client):
  client.add_cog((colc(client)))