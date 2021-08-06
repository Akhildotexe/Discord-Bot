import discord
from discord.ext import commands
import asyncio
import sqlite3

class Ticket(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.test = {}
  global conn
  conn = sqlite3.connect('./data/Database.db', check_same_thread=False)

  @commands.Cog.listener()
  @commands.guild_only()
  async def on_raw_reaction_add(self, get:discord.RawReactionActionEvent):
    emoji = get.emoji
    if not str(emoji) in ('📩', '🔒', '✅', '❎', '📛', '🔓'):
      return
    c = conn.cursor()
    member:discord.Member =get.member
    if member.bot:
      return
    c.execute(f'SELECT msg FROM Guild_ticket WHERE id=?', (member.guild.id,))
    if c.fetchone() == None and str(emoji) != '📩':
      return
    msg=get.message_id
    channel: discord.TextChannel = commands.Bot.get_channel(self.bot, get.channel_id)
    rmsg: discord.Message= await channel.fetch_message(get.message_id)
    admin=False
    Enter = False
    num = self.ticket_num(channel, member, c)
    admin= self.mng(member)
    _id = f'{member.guild.id}_{num}'
    is_have = self.is_have(member, c)
    if not member.bot:
      if str(emoji) != '📩':
        c.execute("SELECT msg, lmsg FROM Tickets WHERE id=?", (_id,))
        if msg in c.fetchone():
          c.execute('SELECT closed FROM Tickets WHERE id=?', (_id,))
          is_closed = bool(c.fetchone()[0])
          c.execute('SELECT lmsg FROM Tickets WHERE id=?', (_id,))
          is_lmsg = bool(c.fetchone()[0] == msg)
          c.execute('SELECT author FROM Tickets WHERE id=?', (_id,))
          author = c.fetchone()[0]
          Enter = True
    
    # =================================================================================================
    if Enter or str(emoji) == '📩':
      if str(emoji) == '📩':
        await rmsg.remove_reaction('📩', member)
        await self.ctk(member, member.guild.id, c)
      elif str(emoji) == '🔒' and admin:
        await rmsg.remove_reaction('🔒', member)
        await rmsg.add_reaction('❎')
        await rmsg.add_reaction('✅')
      elif str(emoji) == '❎' and admin:
        await rmsg.clear_reaction('✅')
        await rmsg.clear_reaction('❎')

      elif str(emoji) == '✅' and admin:
        c.execute('SELECT msg FROM Tickets WHERE id=?', (_id,))
        if msg != c.fetchone()[0]:
          return
        await rmsg.clear_reaction('✅')
        await rmsg.clear_reaction('❎')
        await channel.send(f'***Ticket has been closed by {member.mention}***')
        await self.ltk(_id, channel, author, c)
      elif str(emoji) == '📛':
        if not is_closed or not is_lmsg:
          return
        del_count = 5
        embed=discord.Embed(title=f'Ticket will be deleted in {del_count} sec', color=0xe74c3c)
        del_msg = await channel.send(embed=embed)
        while del_count != 0:
          del_count -= 1
          await asyncio.sleep(1)
          await del_msg.edit(embed=discord.Embed(title=f'Ticket will be deleted in {del_count} sec', color=0xe74c3c))
        c.execute(f'DELETE FROM Tickets WHERE id=?', (_id,))
        conn.commit()
        await channel.delete()
      elif str(emoji) == '🔓':
        if not is_closed or not is_lmsg:
          return
        elif is_have:
          author_mem= channel.guild.get_member(author)
          await channel.send(embed=discord.Embed(description=f'{author_mem.mention} is already opened one.', color = 0xffcc00))
          await rmsg.remove_reaction('🔓',member)
          return
        await self.reopen(channel, author, _id, c)
        await channel.send(f'***Ticket has been reopened by {member.mention}***')
        await rmsg.delete()


  async def reopen(self, channel: discord.TextChannel, author_id, _id, c: sqlite3.Cursor):
    author = channel.guild.get_member(author_id)
    await channel.set_permissions(author, view_channel=True)
    c.execute(f'UPDATE Tickets SET closed=0, lmsg=null WHERE id=?', (_id,))
    conn.commit()

  def ticket_num(self, channel, member, c: sqlite3.Cursor):
    c.execute(f'SELECT id FROM Tickets WHERE channel={channel.id}')
    _id: str = c.fetchone()
    if _id != None:
      return _id[0].split('_')[1]

  def mng(self, member: discord.Member):
    if member == member.guild.owner:
      return member == member.guild.owner
    for role in member.roles:
      if role.permissions.administrator:
        return role.permissions.administrator
    return False
    
  def is_have(self, member: discord.Member, c: sqlite3.Cursor):
    c.execute(f'SELECT closed FROM Tickets WHERE author={member.id}')
    closed = c.fetchall()
    if (0,) in closed:
      return True
    return False

  async def ltk(self, _id, channel, author_id, c: sqlite3.Cursor):
    author = channel.guild.get_member(author_id)
    overwrites={channel.guild.default_role : discord.PermissionOverwrite(view_channel=False), author : discord.PermissionOverwrite(view_channel=None)}
    await channel.edit(overwrites=overwrites)
    embed=discord.Embed(description='📛 to delete the ticket.\n🔓 to reopen the ticket.', color=0xe74c3c)
    lmsg = await channel.send(embed=embed)
    c.execute('UPDATE Tickets SET lmsg=?, closed=1 WHERE id=?', (lmsg.id, _id))
    conn.commit()
    await lmsg.add_reaction('📛')
    await lmsg.add_reaction('🔓')

  async def ctk(self, user, guild_id, c: sqlite3.Cursor):
    overwrites={user.guild.default_role : discord.PermissionOverwrite(view_channel=False), user : discord.PermissionOverwrite(view_channel=True)}
    c.execute(f'SELECT num FROM Guild_ticket WHERE id={guild_id}')
    tkc=  c.fetchone()[0] + 1
    c.execute(f'SELECT category FROM Guild_ticket WHERE id={guild_id}')
    cat = discord.utils.get(user.guild.categories, id=c.fetchone()[0])
    c.execute(f'UPDATE Guild_ticket SET num={tkc} WHERE id={guild_id}')
    channel = await user.guild.create_text_channel(f'ticket-{tkc}', overwrites=overwrites, category=cat)
    lock = await channel.send(embed=discord.Embed(title='Support will be with you shortly.\n To close this ticket react with :lock:'))
    await lock.add_reaction('🔒')
    c.execute('INSERT INTO Tickets VALUES (?, ?, ?, ?, ?, ?)', (f'{guild_id}_{tkc}', lock.id, channel.id, None,  user.id, 0))
    conn.commit()

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def tk(self, ctx):
    embed = discord.Embed(title='react to open a ticket 📩')
    await ctx.message.delete()
    msg= await ctx.send(embed=embed)
    await msg.add_reaction('📩')
    c=conn.cursor()
    c.execute('SELECT id FROM Guild_ticket WHERE id=?', (ctx.guild.id,))
    if c.fetchone() != None:
      c.execute('DELETE FROM Guild_ticket WHERE id=?', (ctx.guild.id,))
    c.execute(f'INSERT INTO Guild_ticket VALUES (?, ?, ?, ?)', (ctx.guild.id, msg.id, 0, None))
    conn.commit();c.close()

  @commands.command()
  @commands.guild_only()
  @commands.has_permissions(administrator=True)
  async def category(self, ctx, _id: int):
    c=conn.cursor()
    c.execute('UPDATE Guild_ticket SET category=? WHERE id=?', (_id, ctx.guild.id))
    conn.commit();c.close()
    cat = discord.utils.get(ctx.guild.categories, id=_id)
    await ctx.send('Ticket ct is now '+cat.name)

  
  # @commands.command()
  # @commands.guild_only()
  # @commands.has_permissions(administrator=True)
  # async def tk_role(self, ctx, role:discord.Role):
  #   with open('Desktop/Discord_Bot/data/ticket.json', 'r') as f:
  #     tk = json.load(f)
  #   if any('tk_msg' == k for k,v in tk[str(ctx.guild.id)].items()):
  #     admin_roles = tk[str(ctx.guild.id)]['admin_roles']
  #     if admin_roles != []:
  #       if not role.id in admin_roles:
  #         admin_roles.append(role.id)
  #         await ctx.send(f'Role **{role.name}** added.')
  #       else:
  #         await ctx.send('You already added the role.')
  #     else:
  #       admin_roles.append(role.id)
  #       await ctx.send(f'Role **{role.name}** added.')
  #   else:
  #     await ctx.send('You must have ticket to use this command.')
  #   with open('Desktop/Discord_Bot/data/ticket.json', 'w') as f:
  #     json.dump(tk, f, indent=2)
  

  # @commands.command()
  # @commands.guild_only()
  # @commands.has_permissions(administrator=True)
  # async def del_tk_role(self, ctx):
  #   with open('Desktop/Discord_Bot/data/ticket.json', 'r') as f:
  #     tk = json.load(f)
  #   roles = tk[str(ctx.guild.id)]['admin_roles']
  #   for mem_role in ctx.author.roles:
  #     var = 0
  #     if mem_role.id in roles or await self.mng(ctx.author):
  #       var += 1
  #   if var == 0:
  #     return await ctx.send('You do not have Permission.')
  #   if len(roles) == 0:
  #     return await ctx.send('There is no admin to delete.')
  #   for role_id in roles:
  #     role = ctx.guild.get_role(role_id)
  #     await ctx.send('{0} - {1}'.format(roles.index(role_id) + 1, role.mention))
  #   await ctx.send('To delete role Enter role number, to ignr Enter anything')
  #   self.test[f'{ctx.guild.id}'] = {}
  #   self.test[f'{ctx.guild.id}']['channel'] = ctx.channel
  #   self.test[f'{ctx.guild.id}']['roles'] = tk[str(ctx.guild.id)]['admin_roles']

def setup(bot):
  bot.add_cog((Ticket(bot)))