from discord.ext import commands, tasks
import os
import discord


intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix= "!", intents=intents)

@client.event
async def on_ready():
    activity= discord.Game('O Jogo')
    await client.change_presence(status=discord.Status.online,activity=activity)
    print(f'Entramos como {client.user}')



for Cogs in os.listdir('./Cogs'):
    if Cogs.endswith('.py'):
        client.load_extension(f'Cogs.{Cogs[:-3]}')

'''@tasks.loop(minutes=20) 
async def refresh():
    urllib.request.urlopen('https://imundiss.herokuapp.com/')'''

if __name__ == '__main__':
    #refresh.start()
    client.run('NjM0MDQ5NzIxMjU3ODIwMTcz.Xac20Q.pzdt3QGc7lUb7RYxqkDtwJITsw8')
