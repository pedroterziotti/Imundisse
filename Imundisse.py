import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix= "!")

for Cogs in os.listdir('./cogs'):
    if Cogs.endswith('.py'):
        client.load_extension(f'Cogs.{Cogs[:-3]}')



client.run('NjM0MDQ5NzIxMjU3ODIwMTcz.Xac20Q.DrRSeOdlxxtoKOdyJVIUbVvTpt4')