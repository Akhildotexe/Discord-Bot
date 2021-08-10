import discord
import os
from discord_components import DiscordComponents
from datetime import timedelta, datetime
from discord.ext import commands
from dotenv import load_dotenv
import sqlite3


client = commands.Bot(command_prefix=(","),help_command=None,activity=discord.Activity(type=discord.ActivityType.listening,name=" ,help | Ping Me"),intents=discord.Intents.all())


cogs = ('cogs.errors', 'cogs.help cmds', 'cogs.calc', 'cogs.gen cmds','cogs.fun cmds','cogs.image cmds','cogs.mod cmds','cogs.ttt','cogs.ticket','cogs.botserver')
if __name__ == '__main__':
  for ex in cogs:
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


conn= sqlite3.connect('./data/Database.db')
c= conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Tickets(id TEXT PRIMARY KEY, msg INTEGER, channel INTEGER, lmsg INTEGER, author INTEGER, closed INTEGER)''')
c.execute('''CREATE TABLE IF NOT EXISTS Guild_ticket(id INTEGER PRIMARY KEY, msg INTEGER, num INTEGER, category INTEGER)''')
conn.commit()

client.run(os.getenv('TOKEN'))
