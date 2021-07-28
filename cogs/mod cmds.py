import discord
from discord import role
from discord.embeds import Embed
from discord.ext import commands
from datetime import datetime, timedelta

class colc(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command()
  async def clear(self,ctx, amount=5):
      await ctx.channel.purge(limit=amount)


  @commands.command()
  async def unban(self,ctx, *,member):
      banned_users = await ctx.guild.bans()
      member_name, member_discriminator = member.split('#')

      for ban_entry in banned_users:
          user = ban_entry.user

          if(user.name,user.discriminator) == (member_name, member_discriminator):
              await ctx.guild.unban(user)
              await ctx.send(f'Unbanned {user.mention}')
              return


  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self,ctx, member: discord.Member,*, reason=None):
      if member==None:
        await ctx.send("asdkflj")
      await member.kick(reason=reason)
      await ctx.send(f'Kicked {member.mention} for {reason}')


  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self,ctx, member : discord.Member,*, reason=None):
      await member.ban(reason=reason)
      await ctx.send(f'Banned {member.mention}')


  @commands.command()
  async def makerole(self,ctx,*, args):
      embed=discord.Embed(title=f"Succesfully created role `{args}` !",color=0xff0000)
      guild = ctx.guild
      await guild.create_role(name=f"{args}")
      await ctx.reply(embed=embed)


  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_channels=True)
  async def lock(self, ctx, *, channel:discord.TextChannel=None):
    channel = channel if channel else ctx.channel
    if channel.overwrites_for(ctx.guild.default_role) == discord.PermissionOverwrite(send_messages=False):
      text = f'{channel.mention}  is already locked.'
      color = 0xFFA500
    else:
      await channel.set_permissions(ctx.guild.default_role, send_messages=False)
      color = 0xFF0000
      text = f':lock: {channel.mention}  has been locked.'
    embed = discord.Embed(description = text, color = color)
    await ctx.send(embed=embed)


  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(manage_channels=True)
  async def unlock(self, ctx, channel:discord.TextChannel=None):
    channel = channel if channel else ctx.channel
    if channel.overwrites_for(ctx.guild.default_role) == discord.PermissionOverwrite(send_messages=None):
      text = f'{channel.mention}  is already unlocked.'
      color = 0xFFA500
    else:
      await channel.set_permissions(ctx.guild.default_role, send_messages=None)
      color = 0x00FF00
      text = f':unlock: {channel.mention}  has been unlocked.'
    embed = discord.Embed(description = text, color = color)
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog((colc(client)))