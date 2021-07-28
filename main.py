import discord
import os
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
from datetime import timedelta, datetime
from discord.ext import commands
from dotenv import load_dotenv


client = commands.Bot(command_prefix=(","),help_command=None,activity=discord.Activity(type=discord.ActivityType.listening,name=" to ,help | Ping Me"),intents=discord.Intents.all())


exs = ('cogs.errors', 'cogs.help cmds', 'cogs.calc', 'cogs.gen cmds','cogs.fun cmds','cogs.image cmds','cogs.mod cmds','cogs.ttt')
if __name__ == '__main__':
  for ex in exs:
    client.load_extension(ex)


DiscordComponents(client)
load_dotenv('.env')
@client.event
async def on_ready():
    global up_time
    up_time= datetime.now()
    print(f'It works {client.user}')


@client.command()
async def uptime(ctx):
    delta_uptime = datetime.now() - up_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    embed = discord.Embed(title=f"I've been up for {days}d, {hours}h, {minutes}m, {seconds}s,", color=0xff0000)
    await ctx.reply(embed=embed)

client.run(os.getenv('TOKEN'))
