import discord
import random
import aiohttp
import json
from discord import Embed
from discord.ext import commands
from datetime import datetime, timedelta

class colc(commands.Cog):
  def __init__(self, client):
    self.client = client

#####################################################################################
    
    
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
                "ahh hell nahh",
                'Maybye',
                'I cannot predict now.',
                'Im to lazy to predict.',
                'I am tired. *proceeds with sleeping*']
        response = random.choice(responses)
        embed=discord.Embed(name=ctx.author.display_name,title="The Magic 8 Ball has Spoken!", color=(0x060505))
        embed.add_field(name='Question: ', value=f'{question}', inline=True)
        embed.add_field(name='Answer: ', value=f'{response}', inline=False)
        await ctx.reply(embed=embed)
    
    
    
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
        await ctx.reply(embed=embed)
    
    
    
    ####################################################################################
    
    
    
  @commands.command()
  @commands.cooldown(1,30, commands.cooldowns.BucketType.user)
  async def tts(self, ctx, *, args):
        await ctx.send(args, tts=True)
    
    
  @commands.command()
  async def google(self,ctx, a):
        await ctx.reply(f'https://google.com/?q={a}')
    
    
  @commands.command()
  async def animesearch(self,ctx,args):
        await ctx.reply(f'https://www.crunchyroll.com/search?from=&q={args}')
    
    
  @commands.command()
  async def yt(self,ctx,args):
        await ctx.reply(f'https://www.youtube.com/results?search_query={args}')
    
    
  @commands.command()
  async def ig(self,ctx,args):
        await ctx.reply(f'https://www.instagram.com/{args}/')
    
  @commands.command()
  async def amazon(self,ctx,args):
        await ctx.reply(f'https://www.amazon.com/s?k={args}')
    
  @commands.command()
  async def urban(self,ctx,args):
        await ctx.reply(f'https://www.urbandictionary.com/define.php?term={args}')
    
  @commands.command()
  async def downloadyt(self,ctx,args):
        await ctx.reply("https://www.y2mate.com/youtube/{args}")
    
    
    
    ####################################################################################
    
    
    
  @commands.command()
  async def rnum(self,ctx):
        embed = discord.Embed(title = "Random Number", description = (random.randint(1, 101)), color = (0x00ff33))
        await ctx.reply(embed = embed)
    
    
  @commands.command()
  async def rdice(self,ctx):
        embed = discord.Embed(title = "You Rolled Your Dice", description = (random.randint(1, 6)), color = (0x00ff33))
        await ctx.reply(embed = embed)
    
    
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
  async def ogmeme(self,ctx):
        embed = discord.Embed(title="More Memes", color = (0x00ff33))
    
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.reply(embed=embed)
    
    
  @commands.command()
  async def planes(self,ctx):
        embed = discord.Embed(title="Planes", color = (0x00ff33))
     
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.airport-data.com/api/ac_thumb.json?m=400A0B&n=2') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.reply(embed=embed)
    
    
  @commands.command()
  async def cat(self,ctx):
        embed = discord.Embed(title="Cats", color = (0x00ff33))
    
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://aws.random.cat/meow') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)


  @commands.command()
  async def urbantest(self,ctx,args):
        
        embed = discord.Embed(title="test", color = (0x00ff33))
    
        async with aiohttp.ClientSession()as cs :
              
            async with self.session.get(f'http://www.urbandictionary.com/new.json?define.php?term={args}') as r:              
                res = await r.json()
                data = await r.read()
                r = json.loads(data)
                embed=discord.Embed(title= 'Heres your meme', color=0x00ff33)
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.reply(embed=embed)


  @commands.command()
  async def yt(self, ctx):
        link = await self.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube')
        await ctx.send(f"Click the blue link!\n{link}")

        

def setup(client):
  client.add_cog((colc(client)))
