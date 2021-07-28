import discord
import random
import string
from discord.ext import commands
from datetime import datetime, timedelta


class colc(commands.Cog):
  def __init__(self, client):
    self.client = client


@commands.command()
async def add(self,ctx, num1, num2):
  num2 = float(num2)
  num1 = float(num1)
  difference = num1 + num2
  embed=discord.Embed(title="Addition",description = f" {num1} + {num2} = {difference}", color = (0xff7b00))
  await ctx.reply(embed=embed)


@commands.command()
async def sub(self,ctx, num1, num2):
  num2 = float(num2)
  num1 = float(num1)
  difference = num1 - num2
  embed=discord.Embed(title="Subtraction",description = f" {num1} - {num2} = {difference}", color = (0xff7b00))
  await ctx.reply(embed=embed)


@commands.command()
async def mult(self,ctx, num1, num2):
  num2 = float(num2)
  num1 = float(num1)
  mult = num1 * num2
  embed=discord.Embed(title="Multiply",description = f" {num1} * {num2} = {mult}", color = (0xff7b00))
  await ctx.reply(embed=embed)


@commands.command()
async def div(self,ctx, num1, num2):
  num2 = float(num2)
  num1 = float(num1)
  div = num1 / num2
  embed=discord.Embed(title="Division",description = f" {num1} / {num2} = {div}", color = (0xff7b00))
  await ctx.reply(embed=embed)


#@client.command()
#async def algebra(ctx):
#    await ctx.send('send the first number')
#    cnum1=await client.wait_for('message', check=lambda c: c.author == ctx.author)
#    await ctx.send('send the operator')
#    cop = await client.wait_for('message', check=lambda c: c.author == ctx.author)
#    await ctx.send('send the second number')
#    cnum2= await client.wait_for('message', check=lambda c: c.author == ctx.author)
#    num1=cnum1.content
#    op=cop.content
#    num2=cnum2.content
#    if op == "+":
#        (f'{num1}+ x={num2}  x={num2 - num1}')
#    if op == "-":
#        (f'{num1}-x={num2}  x={num2 + num1}')
#    exec(f'{num1} {op} {num2}')
#    embed=discord.Embed(title="Algebra",description = "Here #is you problem solved", color = 0xff7b00)
#    await ctx.reply(embed=embed)

def setup(client):
  client.add_cog((colc(client)))