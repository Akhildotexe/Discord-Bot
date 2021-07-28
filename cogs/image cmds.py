import discord
from discord.ext import commands
from datetime import datetime, timedelta
from discord import Embed
from PIL import Image
from io import BytesIO


class colc(commands.Cog):
  def __init__(self, client):
    self.client = client


  @commands.command()
  async def delete(self,ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    delete = Image.open("delete.png")
    delete = delete.convert('RGB')
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    
    pfp = Image.open(data)
    pfp = pfp.resize((121,121))

    delete.paste(pfp, (56,64))

    delete.save("oof.jpeg")

    await ctx.send(file= discord.File("oof.jpeg"))
    return




  @commands.command()
  async def wanted(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    wanted = Image.open("wanted.jpeg")
    asset = user.avatar_url_as(size = 128)    
    data = BytesIO(await asset.read())
    
    pfp = Image.open(data)
    pfp = pfp.resize((566,582))

    wanted.paste(pfp, (313,605))

    wanted.save("profile.jpeg")

    await ctx.send(file= discord.File("profile.jpeg"))
    return


  @commands.command()
  async def wasted(self,ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author

    wasted = Image.open("wasted.jpeg")
    wasted = wasted.convert('RGB')
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    
    pfp = Image.open(data)
    pfp = pfp.resize((515,515))

    wasted.paste(pfp, (1,1))

    wasted.save("rip.jpeg")

    await ctx.send(file= discord.File("rip.jpeg"))
    return


def setup(client):
  client.add_cog((colc(client)))