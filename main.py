import discord
import os
import asyncio
import aiohttp
import requests
import string
import random
#from dislash import SlashClient, ActionRow, Button, check, ButtonStyle
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from datetime import timedelta, datetime
from PIL import Image
from io import BytesIO
from discord.ext import commands
from typing import List


client = commands.Bot(command_prefix=(","),help_command=None,activity=discord.Activity(type=discord.ActivityType.listening,name=" to ,help | Ping Me"))


#SlashClient(client)
bclient= DiscordComponents(client)

client.load_extension('cog')


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
   

@client.group()
async def fun(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(name=ctx.author.display_name,title=' :video_game: type :arrow_down::arrow_down: cmds for more info', description="\n \n`,fun ttt` how to play tictactoe!\n \n `,fun 8ball` how to use 8ball cmd! \n \n `,fun rnum` how to use random number generator. \n \n `,fun rolldice` how to use the roll dice cmd. \n \n `,fun memes` how to get memes! \n \n `,fun memez` more funnier memes. \n \n `,fun yjokes` yo mama jokes! \n \n `,fun googleit` to search google! \n \n `,fun youtube` to search youtube! \n \n `,fun insta` to search instagram!", color=0x00ff33)
        await ctx.reply(embed=embed)


@client.group()
async def gen(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(name=ctx.author.display_name,title="General Cmds" , description="`,gen avatar` how to get a users pfp. \n \n `,gen serverinfo` how to get server info. \n \n `,gen poll` how to make a poll. \n \n `,gen embedinfo` for how to create a embed.",color=0xbb00ff)
        await ctx.reply(embed=embed)


@client.group()
async def math(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(name=ctx.author.display_name,title="math cmds!", description="`,math add` for how to use addition cmd \n \n `,math sub` for how to use the subtraction cmd \n \n`,math mult` for how to use the multiplication cmd \n \n `,math div` for how to use the division cmd",color=0xff7b00)
        await ctx.reply(embed=embed)


@client.group()
async def mod(ctx):
    if ctx.invoked_subcommand is None:
        embed=discord.Embed(name=ctx.author.display_name,title='Moderation cmds  :man_mage: ', description="`,mod purge` for more info on how to purge messages.\n \n `,mod kick` for more info on how to kick members. \n \n `,mod ban` for more info on how to ban members. \n \n `,createrole`for more info on how to create a role. ",color=0xff0000)
        await ctx.reply(embed=embed)


@fun.command()
async def runum(ctx):
    embed=discord.Embed(description=",rnum then your get a random number!",color=0x00ff33)
    await ctx.reply(embed=embed)
    

@fun.command()
async def yjokes(ctx):
    embed=discord.Embed(description="`,ymjokes` then your mom will get roasted!",color=0x00ff33)
    await ctx.reply(embed=embed)


@fun.command()
async def rolldice(ctx):
    embed=discord.Embed(description="`,rdice` then your dice is rolled!",color=0x00ff33)
    await ctx.reply(embed=embed)


@fun.command()
async def memes(ctx):
    embed=discord.Embed(description="`,meme`for memes!",color=0x00ff33)
    await ctx.reply(embed=embed)


@fun.command()
async def memez(ctx):
    embed=discord.Embed(description="`,ogmemes` all the og memes!",color=0x00ff33)
    await ctx.reply(embed=embed)


@fun.command()
async def googleit(ctx):
    embed=discord.Embed(description="`,google` type what you wanna search",color=0x00ff33)
    await ctx.reply(embed=embed)


@fun.command()
async def youtube(ctx):
    embed=discord.Embed(description="`,yt` type what you wanna search",color=0x00ff33)
    await ctx.reply(embed=embed)


@fun.command()
async def insta(ctx):
    embed=discord.Embed(description="`,ig` what you wanna search",color=0x00ff33)
    await ctx.reply(embed=embed)


@gen.command()
async def avatar(ctx):
    embed=discord.Embed(description="`,pfp @user` then your set!",color=0xbb00ff)
    await ctx.reply(embed=embed)


@gen.command()
async def serverinfo(ctx):
    embed=discord.Embed(description="`,server` then your set!",color=0xbb00ff)
    await ctx.reply(embed=embed)


@gen.command()
async def poll(ctx):
    embed=discord.Embed(description="`,poll` + your keywords",color=0xbb00ff)
    await ctx.reply(embed=embed)


@gen.command()
async def embedinfo(ctx):
    embed=discord.Embed(description="`,embed` title description .",color = 0xbb00ff)
    await ctx.reply(embed=embed)


@fun.command()
async def ttt(ctx):
    embed=discord.Embed(title='tictactoe!', description="`,ttt`= tictactoe" , color=0x00ff33)
    embed.add_field(name="`,pe` Places an X or O in square, 1 starts at top left to 9 at bottom right ", value="The board goes \n 1 2 3 \n 4 5 6 \n 7 8 9 ex `,pe #`")
    await ctx.reply(embed=embed)


@fun.command(aliases=['8ball'])
async def fun_8ball(ctx):
    embed=discord.Embed(title='8ball cmd! :8ball: ', description="`,8ball` + your question" , color=0x00ff33)
    embed.add_field(name="`,8ball your question here?`", value="done!")
    await ctx.reply(embed=embed)


@mod.command()
async def kick(ctx):
    embed=discord.Embed(description = "`,kick` @user or id",color=0xff0000)
    await ctx.reply(embed=embed)


@mod.command()
async def ban(ctx):
    embed=discord.Embed(description = "`,ban` @user or id",color=0xff0000)
    await ctx.reply(embed=embed)


@math.command()
async def add(ctx):
    embed=discord.Embed(description="`,add`then type 2 numbers \n EX :arrow_down: \n `,add 5 6` ",color=0xff7b00)
    await ctx.reply(embed=embed)


@math.command()
async def sub(ctx):
    embed=discord.Embed(description="`,sub` then type 2 numbers \n EX :arrow_down: \n `,sub 6 2` this cmd also outputs results for negative numbers. ",color=0xff7b00)
    await ctx.reply(embed=embed)


@math.command()
async def mult(ctx):
    embed=discord.Embed(description="`,mult` then type 2 numbers \n EX :arrow_down: \n `,mult 6 6` this cmd also outputs results for negative numbers. ",color=0xff7b00)
    await ctx.reply(embed=embed)


@math.command()
async def div(ctx):
    embed=discord.Embed(description="`,div` then type 2 numbers \n EX :arrow_down: \n `,div 6 3` this cmd also outputs results for negative numbers.", color=0xff7b00)
    await ctx.reply(embed=embed)


@mod.command()
async def purge(ctx):
    embed=discord.Embed(description="`,clear [number]` then your set!",color=0xff0000)
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


@client.command()
async def server(ctx):
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

@client.command()
async def pfp(ctx, *, member: discord.Member = None):
    if not member:
        member = ctx.message.author
    userAvatar = member.avatar_url
    await ctx.reply(userAvatar)


player1 = ""
player2 = ""
turn = ""
gameOver = True

board = []

winningConditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

@client.command()
async def ttt(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:",
                 ":white_large_square:", ":white_large_square:", ":white_large_square:"]
        turn = ""
        gameOver = False
        count = 0

        player1 = p1
        player2 = p2


        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]


        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn. use `,pe` numbers 1-9 to make a move!")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn. use `,pe` numbers 1-9 to make a move!")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")

@client.command()
async def pe(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:" :
                board[pos - 1] = mark
                count += 1


                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(mark + " wins!")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("It's a tie!")


                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send("Be sure to choose an integer between 1 and 9 make sure its a unmarked tile.")
        else:
            await ctx.send("It is not your turn.")
    else:
        await ctx.send("Please start a new game using the ,ttt command. Make sure to ping 2 people after using ,ttt !")


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True

@ttt.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please @ping 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")

@pe.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


@client.command(aliases=['8ball'])
async def d8ball(ctx, *, question):
    responses = ['As I see it, yes.',
             'Yes.',
             'Positive',
             'From my point of view, yes',
             'ehh.',  
             'Most Likley.',
             'Without a doubt.',
             'Chances High',
             'idk',
             'u must be stupid for asking that',
             'No.',
             'NOOOOOOOO.',
             'only on thursdays.',
             'Perhaps.',
             'Not Sure',
             'Maybye',
             'I cannot predict now.',
             'Im to lazy to predict.',
             'I am tired. *proceeds with sleeping*']
    response = random.choice(responses)
    embed=discord.Embed(name=ctx.author.display_name,title="The Magic 8 Ball has Spoken!", color=(0x060505))
    embed.add_field(name='Question: ', value=f'{question}', inline=True)
    embed.add_field(name='Answer: ', value=f'{response}', inline=False)
    await ctx.reply(embed=embed)


@client.listen()
async def on_message(message):
    context = await client.get_context(message)
    if client.user.mentioned_in(message) and not context.valid:
        embed=discord.Embed(title= 'Help page/Click me for updates <:rdannythinking:759935024123871283> ' ,url='https://discord.gg/VnWBqX3Pjs ' ,description="Bot prefix = [`,`] \n \n `,invite` invite my bot to your server.\n \n `,fun` for games.\n \n `,gen` general commands.\n \n `,math` for math cmds. \n \n `,mod` for moderation cmds.", color=0x00d6e6)
        await message.reply(embed=embed)


@client.command()
async def ymjokes(ctx):
    jokes= ["Yo mama is so old that that when she was in school there was no history class.",
    "Yo mama is so old that I told her to act her own age, and she died.",
    "Yo mama is so old that she knew Burger King while he was still a prince.",
    "Yo mama is so old that her social security number is 1.",
    "Yo mama is so old that her birth certificate is written in Roman numerals.",
    "Yo mama is so old that she has Adam & Eve's autographs.",
    "Yo mama is so old that she co-wrote the Ten Commandments.",
    "Yo mama is so old that she has an autographed bible.",
    "Yo mama is so old she remembers when the Mayans published their calendar.",
    "Yo mama is so old that the candles cost more than the birthday cake.",
    "Yo mama is so old that when she farts, dust comes out.",
    "Yo mama is so old that she owes Fred Flintstone a food stamp.",
    "Yo mama is so old that she drove a chariot to high school.",
    "Yo mama is so old that she took her drivers test on a dinosaur.",
    "Yo mama is so old that she DJ'd at the Boston Tea Party.",
    "Yo mama is so old that she walked into an antique store and they kept her.",
    "Yo mama is so old that she baby-sat for Jesus.",
    "Yo mama is so old that she knew Mr. Clean when he had an afro.",
    "Yo mama is so old that she knew the Beetles when they were the New Kids on the Block.",
    "Yo mama is so old that when God said \"Let there be light\" she was there to flick the switch.",
    "Yo mama is so old that she needed a walker when Jesus was still in diapers.",
    "Yo mama is so old that when Moses split the red sea, she was on the other side fishing.",
    "Yo mama is so old that she learned to write on cave walls.",
    "Yo mama is so old that her memory is in black and white.",
    "Yo mama is so old that she's mentioned in the shout out at the end of the bible.",
    "Yo mama is so old that she planted the first tree at Central Park.",
    "Yo mama is so old that she sat next to Jesus in third grade.",
    "Yo mama is so old that she has a picture of Moses in her yearbook.",
    "Yo mama is so old that she knew Cap'n Crunch while he was still a private.",
    "Yo mama is so old that she called the cops when David and Goliath started to fight.",
    "Yo mama is so old that when she was born, the Dead Sea was just getting sick.",
    "Yo mama is so old, when she breast feeds, people mistake her for a fog machine.",
    "Yo mama is so old that when she was young rainbows were black and white.",
    "Yo mama is so old that she was a waitress at the Last Supper.",
    "Yo mama is so old that she owes Jesus a dollar.",
    "Yo mama is so old that she ran track with dinosaurs."
    "Yo mama so fat that when she went to Wendy's they had to call burger king for help"]
    embed = discord.Embed(title = "Yo Mama Roasted <:PepePoint:759934591590203423>",
    description=random.choice(jokes), color = (0x00ff33))
    await ctx.send(embed=embed)

@client.command()
@commands.cooldown(1,30, commands.cooldowns.BucketType.user)
async def tts(ctx, *, args):
    await ctx.send(args, tts=True)


@client.command()
async def google(ctx, a):
    await ctx.reply(f'https://google.com/?q={a}')
 

@client.command()
async def animesearch(ctx, args):
    await ctx.reply(f'https://www.crunchyroll.com/search?from=&q={args}')


@client.command()
async def yt(ctx, args):
    await ctx.reply(f'https://www.youtube.com/results?search_query={args}')


@client.command()
async def ig(ctx, args):
    await ctx.reply(f'https://www.instagram.com/{args}/')

@client.command()
async def amazon(ctx, args):
    await ctx.reply(f'https://www.amazon.com/s?k={args}')

@client.command()
async def urban(ctx, args):
    await ctx.reply(f'https://www.urbandictionary.com/define.php?term={args}')


@client.command()
async def rnum(ctx):
    embed = discord.Embed(title = "Random Number", description = (random.randint(1, 101)), color = (0x00ff33))
    await ctx.send(embed = embed)


@client.command()
async def rdice(ctx):
    embed = discord.Embed(title = "You Rolled Your Dice", description = (random.randint(1, 6)), color = (0x00ff33))
    await ctx.send(embed = embed)



#@client.command()
#async def roast(ctx):

    #api_url = 'https://api.snowflakedev.xyz/roast'


#@client.listen
#async def on_message(message):
    #if not message.author.bot:
        #if message.content == 'roast':
            #data = requests.get(api_url).content.decode()
            #roast = json.loads(data)['roast']
            #await message.channel.send(roast)


@client.command()
async def meme(ctx):
    
    embed = discord.Embed(title="Memes", color = (0x00ff33))

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed=discord.Embed(title= 'Heres your meme', color=0x00ff33)
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.reply(embed=embed)


@client.command()
async def ogmeme(ctx):
    embed = discord.Embed(title="More Memes", color = (0x00ff33))
 
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.reply(embed=embed)


@client.command()
async def planes(ctx):
    embed = discord.Embed(title="Planes", color = (0x00ff33))
 
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.airport-data.com/api/ac_thumb.json?m=400A0B&n=2') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.reply(embed=embed)


@client.command()
async def cat(ctx):
    embed = discord.Embed(title="Cats", color = (0x00ff33))

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://aws.random.cat/meow') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


buttons = [
    [
        Button(style=ButtonStyle.grey, label='1'),
        Button(style=ButtonStyle.grey, label='2'),
        Button(style=ButtonStyle.grey, label='3'),
        Button(style=ButtonStyle.blue, label='×'),
        Button(style=ButtonStyle.red, label='Exit')
    ],
    [
        Button(style=ButtonStyle.grey, label='4'),
        Button(style=ButtonStyle.grey, label='5'),
        Button(style=ButtonStyle.grey, label='6'),
        Button(style=ButtonStyle.blue, label='÷'),
        Button(style=ButtonStyle.red, label='←')
    ],
    [
        Button(style=ButtonStyle.grey, label='7'),
        Button(style=ButtonStyle.grey, label='8'),
        Button(style=ButtonStyle.grey, label='9'),
        Button(style=ButtonStyle.blue, label='+'),
        Button(style=ButtonStyle.red, label='Clear')
    ],
    [
        Button(style=ButtonStyle.grey, label='00'),
        Button(style=ButtonStyle.grey, label='0'),
        Button(style=ButtonStyle.grey, label='.'),
        Button(style=ButtonStyle.blue, label='-'),
        Button(style=ButtonStyle.green, label='=')
    ],
]
 
 
def calculate(exp):
    o = exp.replace('×', '*')
    o = o.replace('÷', '/')
    result = ''
    try:
        result = str(eval(o))
    except:
        result = 'An error occurred.'
    return result
 
#@client.command()
# async def calc(ctx):
#     m = await ctx.send(content='Loading Calculators...')
#     expression = 'None'
#     delta = datetime.utcnow() + timedelta(minutes=5)
#     e = discord.Embed(title=f'{ctx.author.name}\'s calculator | {ctx.author.id}', description=expression,
#                         timestamp=delta)
#     await m.edit(components=buttons, embed=e)
#     while m.created_at < delta:
#         res = await client.wait_for('button_click')
#         if res.author.id == int(res.message.embeds[0].title.split('|')[1]) and res.message.embeds[
#             0].timestamp < delta:
#             expression = res.message.embeds[0].description
#             if expression == 'None' or expression == 'An error occurred.':
#                 expression = ''
#             if res.component.label == 'Exit':
#                 await res.respond(content='Calculator Closed', type=7)
#                 break
#             elif res.component.label == '←':
#                 expression = expression[:-1]
#             elif res.component.label == 'Clear':
#                 expression = 'None'
#             elif res.component.label == '=':
#                 expression = calculate(expression)
#             else:
#                 expression += res.component.label
#             f = discord.Embed(title=f'{res.author.name}\'s calculator|{res.author.id}', description=expression,
#                                 timestamp=delta)
#             await res.respond(content='', embed=f, components=buttons, type=7)

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
#    num1= float(input("Enter the 1st input:"))
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


@client.command(name="poll")
async def suggestions(ctx, *, suggestion: str):
    """Make a `/suggestion"""
    await ctx.message.delete()
    em = discord.Embed(description=suggestion,color=0xbb00ff)
    em.set_author(name=f"Poll by {ctx.author.display_name}", icon_url=ctx.author.avatar_url)   
    msg = await ctx.send(embed=em)
    await msg.add_reaction('⬆️')
    await msg.add_reaction('⬇️')


@client.command()
async def embed(ctx,a ,b ,c):
    embed=discord.Embed(title = f"{a}" ,description = f"{b}",value = f"{c}",color=0xbb00ff)
    await ctx.reply(embed=embed)


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



@client.listen()
async def CommandNotFound(ctx):
    await ctx.send("error")


client.run(os.getenv('TOKEN'))
