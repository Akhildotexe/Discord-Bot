import discord
import random
import string
import aiohttp
from discord import embeds
from discord import client
from discord.client import Client
from discord.ext import commands
from discord_components import Button, ButtonStyle, DiscordComponents
from datetime import datetime, timedelta

class colc(commands.Cog):
  def __init__(self, client):
    self.client = client


#  @commands.group()
#  async def fun(self,ctx):
#    if ctx.invoked_subcommand is None:
#      embed=discord.Embed(name=ctx.author.display_name,title=' :video_game: type :arrow_down::arrow_down: cmds for more info', description="\n \n`,fun ttt` how to play tictactoe!\n \n `,fun 8ball` how to use 8ball cmd! \n \n `,fun rnum` how to use random number generator. \n \n `,fun rolldice` how to use the roll dice cmd. \n \n `,fun memes` how to get memes! \n \n `,fun memez` more funnier memes. \n \n `,fun yjokes` yo mama jokes! \n \n `,fun googleit` to search google! \n \n `,fun youtube` to search youtube! \n \n `,fun insta` to search instagram!", color=0x00ff33)
#      await ctx.reply(embed=embed)
#
#  @fun.command() 
#  async def test(self, ctx):
#    embed=discord.Embed(title="fun command works kid stop bonking ur head now")
#    await ctx.send(embed=embed)
#
#
#  @fun.command()
#  async def yjokes(self,ctx):
#    embed=discord.Embed(description="`,ymjokes` then your mom will get roasted!",color=0x00ff33)
#    await ctx.reply(embed=embed)
#
#
#  @fun.command()
#  async def rolldice(self,ctx):
#    embed=discord.Embed(description="`,rdice` then your dice is rolled!",color=0x00ff33)
#    await ctx.reply(embed=embed)
#
#
#  @fun.command()
#  async def memes(self,ctx):
#    embed=discord.Embed(description="`,meme`for memes!",color=0x00ff33)
#    await ctx.reply(embed=embed)
#
#
#  @fun.command()
#  async def memez(self,ctx):
#    embed=discord.Embed(description="`,ogmemes` all the og memes!",color=0x00ff33)
#    await ctx.reply(embed=embed)
#
#
#  @fun.command()
#  async def googleit(self,ctx):
#    embed=discord.Embed(description="`,google` type what you wanna search",color=0x00ff33)
#    await ctx.reply(embed=embed)
#
#
#  @fun.command()
#  async def youtube(self,ctx):
#    embed=discord.Embed(description="`,yt` type what you wanna search",color=0x00ff33)
#    await ctx.reply(embed=embed)
#
#
#  @fun.command()
#  async def insta(self,ctx):
#    embed=discord.Embed(description="`,ig` what you wanna search",color=0x00ff33)
#    await ctx.reply(embed=embed)
#    
#
#  @fun.command()
#  async def ttt(self, ctx):
#    embed=discord.Embed(title='tictactoe!', description="`,ttt`= tictactoe" , color=0x00ff33)
#    embed.add_field(name="`,pe` Places an X or O in square, 1 starts at top left to 9 at bottom right ", value="The board goes \n 1 2 3 \n 4 5 6 \n 7 8 9 ex `,pe #`")
#    await ctx.reply(embed=embed)
#
#
#  @fun.command(aliases=['8ball'])
#  async def fun_8ball(self,ctx):
#    embed=discord.Embed(title='8ball cmd! :8ball: ', description="`,8ball` + your question" , color=0x00ff33)
#    embed.add_field(name="`,8ball your question here?`", value="done!")
#    await ctx.reply(embed=embed)


####################################################################################
  global count
  global player1
  global player2
  global turn
  global gameOver
  global count
  global player1
  global player2
  global turn
  global gameOver
  
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
    
  @commands.command()
  async def ttt(self,ctx, p1: discord.Member, p2: discord.Member):
    
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
            
  def checkWinner(winningConditions, mark):
        global gameOver
        for condition in winningConditions:
            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                gameOver = True
    

  @commands.command()
  async def pe(self,ctx, pos: int):
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
    
                    self.checkWinner(winningConditions, mark)
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
    
    
#  def checkWinner(winningConditions, mark):
#        global gameOver
#        for condition in winningConditions:
#            if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
#                gameOver = True
    
  @ttt.error
  async def tictactoe_error(self, ctx, error):
        print(error)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please @ping 2 players for this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to mention/ping players (ie. <@688534433879556134>).")
    
  @pe.error
  async def place_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please enter a position you would like to mark.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please make sure to enter an integer.")
    
    
    ####################################################################################
    
    
  @commands.command(aliases=['8ball'])
  async def d8ball(self,ctx, *, question):
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
        await ctx.send(embed=embed)
    
    
    
    ####################################################################################
    
    
    
  @commands.command()
  async def ymjokes(self,ctx):
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
    
    
    
    ####################################################################################
    
    
    
  @commands.command()
  @commands.cooldown(1,30, commands.cooldowns.BucketType.user)
  async def tts(self, ctx, *, args):
        await ctx.send(args, tts=True)
    
    
  @commands.command()
  async def google(ctx, a):
        await ctx.reply(f'https://google.com/?q={a}')
    
    
  @commands.command()
  async def animesearch(ctx, args):
        await ctx.reply(f'https://www.crunchyroll.com/search?from=&q={args}')
    
    
  @commands.command()
  async def yt(ctx, args):
        await ctx.reply(f'https://www.youtube.com/results?search_query={args}')
    
    
  @commands.command()
  async def ig(ctx, args):
        await ctx.reply(f'https://www.instagram.com/{args}/')
    
  @commands.command()
  async def amazon(ctx, args):
        await ctx.reply(f'https://www.amazon.com/s?k={args}')
    
  @commands.command()
  async def urban(ctx, args):
        await ctx.reply(f'https://www.urbandictionary.com/define.php?term={args}')
    
  @commands.command()
  async def downloadyt(self,ctx,args):
        await ctx.send("https://www.y2mate.com/youtube/{args}")
    
    
    
    ####################################################################################
    
    
    
  @commands.command()
  async def rnum(self,ctx):
        embed = discord.Embed(title = "Random Number", description = (random.randint(1, 101)), color = (0x00ff33))
        await ctx.send(embed = embed)
    
    
  @commands.command()
  async def rdice(self,ctx):
        embed = discord.Embed(title = "You Rolled Your Dice", description = (random.randint(1, 6)), color = (0x00ff33))
        await ctx.send(embed = embed)
    
    
  @commands.command()
  async def meme(self,ctx):
        
        embed = discord.Embed(title="Memes", color = (0x00ff33))
    
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                res = await r.json()
                embed=discord.Embed(title= 'Heres your meme', color=0x00ff33)
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.reply(embed=embed)
    
    
  @commands.command()
  async def ogmeme(ctx):
        embed = discord.Embed(title="More Memes", color = (0x00ff33))
    
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.reply(embed=embed)
    
    
  @commands.command()
  async def planes(ctx):
        embed = discord.Embed(title="Planes", color = (0x00ff33))
     
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.airport-data.com/api/ac_thumb.json?m=400A0B&n=2') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.reply(embed=embed)
    
    
  @commands.command()
  async def cat(ctx):
        embed = discord.Embed(title="Cats", color = (0x00ff33))#
    
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://aws.random.cat/meow') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)



def setup(client):
  client.add_cog((colc(client)))