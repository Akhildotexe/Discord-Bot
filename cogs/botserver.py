import discord
from discord.ext import commands
from datetime import datetime, timedelta

class colc(commands.Cog):
    def __init__(self, client):
      self.client = client
    
    
    
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        channel= guild.get_channel(871990088014372894)
        if not channel:
            channel= await self.client.fetch_channel(871990088014372894)
        e=discord.Embed(title='Guild join', description=f'Bot has been added to {guild.name} .', color=discord.Color.green())
        e.set_thumbnail(url=guild.icon_url)
        e.set_footer(text=f'{guild.name} • {len(self.client.guilds)} servers')
        await channel.send(embed=e)
        
    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        try:
            channel_id= 872268371272564766
            channel= guild.get_channel(channel_id)
            if not channel:
                channel= await self.client.fetch_channel(channel_id)
            e=discord.Embed(title='Guild remove', description=f'Bot has been removed from {guild.name} .', color=discord.Colour.red())
            e.set_thumbnail(url=guild.icon_url)
            e.set_footer(text=f'{guild.name} • {len(self.client.guilds)} servers')
            await channel.send(embed=e)
        except Exception as e:
            print(e)

    
def setup(client):
  client.add_cog((colc(client)))
    
