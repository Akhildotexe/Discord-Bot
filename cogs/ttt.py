import discord
import random
from discord.ext import commands

class ttt(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    global gameOver
    global count
    global player1
    global player2
    global turn
    global winningConditions
    global nums
    
    player1 = ""
    player2 = ""
    turn = ""
    turn = ""
    gameOver = False
    count = 0
    
    board = []
    nums={'1':":one:", '2':":two:", '3':":three:",'4':":four:", '5':":five:", '6':":six:", '7':":seven:", '8':":eight:", '9':":nine:"}
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
    
        if not gameOver:
            global board, turn, player1, player2
            board = [":one:", ":two:", ":three:",
                    ":four:", ":five:", ":six:",
                    ":seven:", ":eight:", ":nine:"]
    
            player1 = p1
            player2 = p2
    
    
            line = ""
            for x in range(len(board)):
                if x == 3 or x == 6 or x == 9:
                    line += '\n'
                    line += board[x]
                else:
                    line += ' '+board[x]
            await ctx.send(line)
    
    
            num = random.randint(1, 2)
            if num == 1:
                turn = player1
                await ctx.send("It is <@" + str(player1.id) + ">'s turn. use `,pe` numbers 1-9 to make a move!")
            elif num == 2:
                turn = player2
                await ctx.send("It is <@" + str(player2.id) + ">'s turn. use `,pe` numbers 1-9 to make a move!")
        else:
            await ctx.send("A game is already in progress! Finish it before starting a new one.")
            
    def checkWinner(self, winningConditions, mark):
            global gameOver
            for condition in winningConditions:
                if board[condition[0]] == mark and board[condition[1]] == mark and board[condition[2]] == mark:
                    gameOver = True
    
    @commands.command()
    async def pe(self,ctx, pos: int):
        global gameOver
        global count
        global player1
        global player2
        global turn
    
        if not gameOver:
            mark = ""
            if turn == ctx.author:
                if turn == player1:
                    mark = ":x:"
                elif turn == player2:
                    mark = ":o:"
                if 0 < pos < 10 and board[pos - 1] == nums[str(pos)] :
                    board[pos - 1] = mark
                    count += 1
    
                    self.checkWinner(winningConditions, mark)

                    line = ""
                    for x in range(len(board)):
                        if x == 3 or x == 6 or x == 9:
                            line += '\n'
                            line += board[x]
                        else:
                            line += ' '+board[x]
                    await ctx.send(line)
                    print(count)
                    if gameOver:
                        await ctx.send(mark + " wins!")
                    elif count >= 9:
                        gameOver = True
                        await ctx.send("It's a tie!")
    
    
                    if turn == player1:
                        turn = player2
                    elif turn == player2:
                        turn = player1
                    if not gameOver:
                        await ctx.send(f"It is {turn.mention}'s turn. use `,pe` numbers 1-9 to make a move!")
                else:
                    await ctx.send("Be sure to choose an integer between 1 and 9 make sure its a unmarked tile.")
            else:
                await ctx.send("It is not your turn.")
        else:
            await ctx.send("Please start a new game using the ,ttt command. Make sure to ping 2 people after using ,ttt !")

    @ttt.error
    async def tictactoe_error(self, ctx, error):
            print(error)
            if isinstance(error, commands.MissingRequiredArgument):
                await ctx.send("Please @ping 2 players for this command.")
            elif isinstance(error, commands.BadArgument):
                await ctx.send("Please make sure to mention/ping players (ie. <@!688534433879556134>).")


def setup(client):
    client.add_cog((ttt(client)))