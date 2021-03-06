
###################
###################
###
###
###  POPIT COMMAND
###
###
###################
###################


import discord
from discord.ext import commands
from decouple import config
from __main__ import bot



class PopItCommand(commands.Cog):
    def __init__(self, client):
        self.client = client


@bot.command()
async def popit(ctx):
            embed = discord.Embed(title="Mini game Pop-It š®", color=discord.Color.blue(), timestamp=ctx.message.created_at)

            embed.add_field(name="`Click on the squares`", value=" ā||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||||:orange_square:||ā\nā||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||||:blue_square:||ā\nā||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||||:yellow_square:||ā\nā||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||||:white_large_square:||ā\nā||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||||:green_square:||ā\nā||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||||:purple_square:||ā")

            embed.set_footer(text=f'Requested by { ctx.message.author.display_name }', icon_url=ctx.message.author.avatar_url)

            await ctx.send(embed=embed)
    

def setup(client):
    client.add_cog(PopItCommand(client))
