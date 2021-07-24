import discord
import random
import string
import aiohttp
from discord.ext import commands
from discord_components import Button, ButtonStyle, DiscordComponents
import datetime

class colc(commands.Cog):
  def __init__(self, client):
    self.client = client


#  @commands.group()
#  async def gen(self,ctx):
#    if ctx.invoked_subcommand is None:
#        embed=discord.Embed(name=ctx.author.display_name,title="General Cmds" , description=" `,gen user` to get info abt users join date, etc. \n \n`,gen avatar` how to get a users pfp. \n \n `,gen serverinfo` how to get server info. \n \n `,gen poll` how to make a poll. \n \n `,gen embedinfo` for how to create a embed.",color=0xbb00ff)
#        await ctx.reply(embed=embed)
#
#
#
#  @gen.command()
#  async def user(self,ctx):
#    embed=discord.Embed(description="`whois @user` to get a users info.",color=0xbb00ff)
#    await ctx.send(embed=embed)
#
#
#  @gen.command()
#  async def avatar(self,ctx):
#    embed=discord.Embed(description="`,pfp @user` then your set!",color=0xbb00ff)
#    await ctx.reply(embed=embed)
#
#
#  @gen.command()
#  async def serverinfo(self,ctx):
#    embed=discord.Embed(description="`,server` then your set!",color=0xbb00ff)
#    await ctx.reply(embed=embed)
#
#
#  @gen.command()
#  async def poll(self,ctx):
#    embed=discord.Embed(description="`,poll` + your keywords",color=0xbb00ff)
#    await ctx.reply(embed=embed)
#
#
#  @gen.command()
#  async def embedinfo(self,ctx):
#    embed=discord.Embed(description="`,embed` title description .",color = 0xbb00ff)
#    await ctx.reply(embed=embed)



####################################################################################
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
      embed.add_field(name='Owner', value=owner,inline=True)
      embed.add_field(name='ServerID', value=id, inline=True)
      embed.add_field(name='Member Count', value=memberCount,
    inline=True)
      await ctx.reply(embed=embed)


  @commands.command()
  async def embed(self,ctx,a ,b ,c):
      embed=discord.Embed(title = f"{a}" ,description = f"{b}",value = f"{c}",color=0xbb00ff)
      await ctx.reply(embed=embed)



def setup(client):
  client.add_cog((colc(client)))