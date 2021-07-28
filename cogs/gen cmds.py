import discord
import random
import string
from discord import client
from discord.ext import commands
from discord import Embed
import datetime

class colc(commands.Cog):
  def __init__(self, client):
    self.client = client


  async def colc(self, colc_type):
    now = datetime.datetime.utcnow()    
    ago = now - colc_type
    print(ago)
    y = datetime.timedelta(365)
    m = datetime.timedelta(30.4)
    if ago < y:
      if ago < m:
        return '%d days' % ago.days
      else:  
        months = round( ago.days / 30 )
        return f'{months} months'
    else:
      years = round(ago.days / 365)
      return f'{int(years)} years'




  @commands.command()
  async def whois(self, ctx, *, mention: discord.Member=None):
    if mention == None:
      mention = ctx.author
    ageA = mention.created_at
    ageJ = mention.joined_at
    tp = await self.colc(ageA)
    tp2 = await self.colc(ageJ)
    embed=discord.Embed(color=0xbb00ff)
    embed.set_thumbnail(url=mention.avatar_url)
    embed.add_field(name='Username:', value=f'{mention.name}#{mention.discriminator}')
    embed.add_field(name='Mention:', value=mention.mention)
    embed.add_field(name='Account Age: ', value=ageA.strftime('`%m/%d/%Y |  %I:%M %p`')+ f'\n {tp}', inline=False)
    embed.add_field(name='Server Joined :', value=ageJ.strftime('`%m/%d/%Y |  %I:%M %p`')+ f'\n {tp2} ago')
    embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


  @commands.command()
  async def pfp(self, ctx, *,  mention: discord.Member=None):
    user=ctx.author
    if mention==None:
      mention=user
      avatar=mention.avatar_url
      embed=discord.Embed(title='Avatar Link', url=f'{mention.avatar_url}',color=0xbb00ff)
      embed.set_footer(text=f'Requested by {user.name}#{user.discriminator}', icon_url=user.avatar_url)
      embed.set_image(url=avatar)
      embed.set_author(name=f'{mention.name}', icon_url=mention.avatar_url)
      await ctx.send(embed=embed)


  @commands.command(name="poll")
  async def suggestions(ctx, *, suggestion: str):
      """Make a `/suggestion"""
      await ctx.message.delete()
      em = discord.Embed(description=suggestion,color=0xbb00ff)
      em.set_author(name=f"Poll by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)   
      msg = await ctx.send(embed=em)
      await msg.add_reaction('⬆️')
      await msg.add_reaction('⬇️')


  @commands.command()
  async def server(self,ctx):
      name = str(ctx.guild.name)
      description = str(ctx.guild.description)

      owner = str(ctx.guild.owner)
      id = str(ctx.guild.id)
      memberCount = str(ctx.guild.member_count)

      icon = str(ctx.guild.icon_url)

      embed = discord.Embed(
        title=name +'Server information',
        description=description,
       color=0xbb00ff)
      embed.set_thumbnail(url=icon)
      embed.add_field(name='<:pikawhat:597589872198549515> Owner',  value=owner,inline=True)
      embed.add_field(name='<:thrinking:597590667669274651> ServerID',  value=id, inline=True)
      embed.add_field(name='<:verycool:739613733474795520> Member Count',  value=memberCount,
    inline=True)
      await ctx.reply(embed=embed)

  @commands.command()
  async def botinfo(self, ctx):
    all_users=set([mem for guild in self.client.guilds for mem in guild.members if not mem.bot])
    all_bots=set([mem for guild in self.client.guilds for mem in guild.members if mem.bot])
    all_guilds=[guild for guild in self.client.guilds]
    all_channels=[channel for guild in self.client.guilds for channel in guild.channels]
    all_roles=[role for guild in self.client.guilds for role in guild.roles]
    everything= [f'**<:verycool:739613733474795520> Users:** {len(all_users)}', f'** <:dpy:596577034537402378> Bots:** {len(all_bots)}', 
                f'** <a:Discord:865978943055462440> servers:** {len(all_guilds)}', f'** <:discriminator:866155257242976276> Channels:** {len(all_channels)}',
                f'** <:general:866155253861580811> Roles:** {len(all_roles)}',
                ]
    e= discord.Embed(title=' <:hahayes:739613910180692020> I can see.  <:thrinking:597590667669274651>', description='\n\n'.join([thing for thing in everything]),color=0xbb00ff)
    await ctx.send(embed=e)


  @commands.command()
  async def embed(self,ctx,a ,b ,c):
      embed=discord.Embed(title = f"{a}" ,description = f"{b}",value = f"{c}",color=0xbb00ff)
      await ctx.reply(embed=embed)

  @commands.command()
  async def ping(self,ctx):
    latency = round(self.client.latency * 1000)
    if latency < 1:
        pingg=discord.Embed(description=f" :ping_pong: Pong! 0 MS", color=(0x00fbff))
        await ctx.reply(embed=pingg)
    else:
       ping=discord.Embed(description=f" :ping_pong: Pong! {latency} MS", color=(0x00fbff))
       await ctx.reply(embed=ping)


    
def setup(client):
  client.add_cog((colc(client)))