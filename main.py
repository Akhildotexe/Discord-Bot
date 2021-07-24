import discord
import os
import asyncio
import aiohttp
from discord.ext.commands.core import command
import requests
import string
import random
#from dislash import SlashClient, ActionRow, Button, check, ButtonStyle
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from datetime import timedelta, datetime
from PIL import Image
from io import BytesIO
from discord.ext import commands
from dotenv import load_dotenv
    


client = commands.Bot(command_prefix=(","),help_command=None,activity=discord.Activity(type=discord.ActivityType.listening,name=" to ,help | Ping Me"))


#SlashClient(client)
bclient= DiscordComponents(client)
load_dotenv('.env')
client.load_extension('calc')
client.load_extension('fun cmds')
client.load_extension('gen cmds')
client.load_extension('help cmds')

@client.event
async def on_ready():
    print(f'It works {client.user}')


@client.command()
async def yo(ctx):
    embed=discord.Embed(description="The Bot Works!", color=0x00ff9d)
    await ctx.send(embed=embed)


@client.command()
async def help(ctx):
    embed=discord.Embed(title= 'Help page/Click me for updates <:rdannythinking:759935024123871283> ' ,url='https://discord.gg/VnWBqX3Pjs ' ,description="Bot prefix = [`,`] \n \n `,invite` invite my bot to your server.\n \n `,fun` for games.\n \n `,gen` general commands.\n \n `,math` for math cmds. \n \n `,mod` for moderation cmds.", color=0x00d6e6,timestamp=ctx.message.created_at)
    #embed.set_footer(name=f"Requested by {ctx.author.display_name}!", icon_url=ctx.author.avatar_url)
    await ctx.reply(embed=embed)

    
@client.command()
async def invite(ctx):
    embed=discord.Embed(description="https://discord.com/oauth2/authorize?client_id=841300946973622303&permissions=0&scope=bot%20applications.commands\n \nhttps://discord.gg/5HktqCkYHY", color=0x00ff7b)
    await ctx.reply(embed=embed)





@client.command()
async def ping(ctx):
    latency = round(client.latency * 1000)
    if latency < 1:
        embed=discord.Embed(description=f" :ping_pong: Pong! 0 MS", color=(0x00fbff))
        await ctx.reply(embed=embed)
    else:
       embed=discord.Embed(description=f" :ping_pong: Pong! {latency} MS", color=(0x00fbff))
       await ctx.reply(embed=embed)



@client.listen()
async def on_message(message):
    context = await client.get_context(message)
    if client.user.mentioned_in(message) and not context.valid:
        embed=discord.Embed(title= 'Help page/Click me for updates <:rdannythinking:759935024123871283> ' ,url='https://discord.gg/VnWBqX3Pjs ' ,description="Bot prefix = [`,`] \n \n `,invite` invite my bot to your server.\n \n `,fun` for games.\n \n `,gen` general commands.\n \n `,math` for math cmds. \n \n `,mod` for moderation cmds.", color=0x00d6e6)
        await message.reply(embed=embed)



@client.command()
async def nitrocmd(ctx):
    def check_yes_no(msg):
        return msg.content.lower
    a = 5
    while a<10:
        msg = await client.wait_for("message", check=check_yes_no)
        if msg.content.lower() == "stop": 
            return 
            
        random_num = str(random.randint(1, 100))
        y = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + random_num) for _ in range(16))
    
    await ctx.send(f"https://discord.gift/{y}")


@client.command()
async def add(ctx, num1, num2):
  num2 = float(num2)
  num1 = float(num1)
  difference = num1 + num2
  embed=discord.Embed(title="Addition",description = f" {num1} + {num2} = {difference}", color = (0xff7b00))
  await ctx.reply(embed=embed)


@client.command()
async def sub(ctx, num1, num2):
  num2 = float(num2)
  num1 = float(num1)
  difference = num1 - num2
  embed=discord.Embed(title="Subtraction",description = f" {num1} - {num2} = {difference}", color = (0xff7b00))
  await ctx.reply(embed=embed)


@client.command()
async def mult(ctx, num1, num2):
  num2 = float(num2)
  num1 = float(num1)
  mult = num1 * num2
  embed=discord.Embed(title="Multiply",description = f" {num1} * {num2} = {mult}", color = (0xff7b00))
  await ctx.reply(embed=embed)


@client.command()
async def div(ctx, num1, num2):
  num2 = float(num2)
  num1 = float(num1)
  div = num1 / num2
  embed=discord.Embed(title="Division",description = f" {num1} / {num2} = {div}", color = (0xff7b00))
  await ctx.reply(embed=embed)


#@client.command()
#async def algebra(ctx, num1, num2):
#    num1= float(input("Enter the 1st input:"))z
#    op = input("Enter the operator: ")
#    num2= float(input("Enter the 3nd input: "))
#    if op == "+":
#        (f'{num1}+x={num2}  x={num2 - num1}')
#    if op == "-":
#        (f'{num1}-x={num2}  x={num2 + num1}')
#embed=discord.Embed(title="Algebra",description = "Here #is you problem solved", #color = 0xff7b00)
#    await ctx.reply(embed=embed)


@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@client.command()
async def unban(ctx, *,member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban.entry.user

        if(user.name,user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return


@client.command()
async def kick(ctx, member : discord.Member,*, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'Kicked {member.mention}')


@client.command()
async def ban(ctx, member : discord.Member,*, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.mention}')


@client.command()
async def makerole(ctx, args):
    embed=discord.Embed(title=f"Succesfully created role `{args}` !",color=0xff0000)
    guild = ctx.guild
    await guild.create_role(name=f"{args}")
    await ctx.reply(embed=embed)

#@client.command()
#async def uptime(ctx):
#    delta_uptime = datetime.utcnow() - ##client.launch_time
#    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
#    minutes, seconds = divmod(remainder, 60)
#    days, hours = divmod(hours, 24)
#    embed = discord.Embed(title=f"I've been up for {days}d, {hours}h, {minutes}m, {seconds}s,", color=0xff0000)
#    await ctx.reply(embed=embed)


@client.command()
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



@client.command()
async def delete(ctx, user: discord.Member = None):
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


@client.command()
async def wasted(ctx, user: discord.Member = None):
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

@client.event
async def on_command_error(ctx,* ,error): 
    if isinstance(error, commands.MissingRequiredArgument): 
        embed = discord.Embed(title=f"Error!!!", description=f" {error},pls enter a valid cmd or `,help`", color=0xff0000) 
        await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx,* , error): 
    if isinstance(error, commands.MissingPermissions): 
        embed = discord.Embed(title=f"Error!!!", description=f" {error},pls enter a valid cmd or `,help`", color=0xff0000)  
        await ctx.send(embed=embed)


@client.event
async def on_command_error(ctx,error): 
    if isinstance(error, commands.CommandNotFound): 
        embed = discord.Embed(title=f":x: Invalid command used", description=f" `{error}`,pls enter a valid cmd or `,help`", color=0xff0000) 
        await ctx.send(embed=embed)


client.run(os.getenv('TOKEN'))