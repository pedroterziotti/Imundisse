import discord
import asyncio
import json
import time

intents = discord.Intents.all()
intents.members = True
#
with open('./variables.json') as file:
    variables = json.load(file)

#client = commands.Bot(command_prefix= "!", intents=intents)
client = discord.Client(intents=intents)
message='ola'

@client.event
async def on_ready():
    """
    guild =client.get_guild(830505972451639296)
    member = guild.get_member_named("scorpiontaken")
    print(member.id)
    await client.close()
    #await channel.send(f'Estou onliner com Grandes "Roubos Automobilisticos". Aassista em: https://www.twitch.tv/nsgordon   <@&{836346543228452944}>')
    """ 
    user = client.get_user(178144275358285825)
    await user.send('oi')
    await asyncio.sleep(10)
    await user.send(message)
    await client.close()


@client.event
async def on_message(ctx):
    global message
    message = ctx.content

async def send(user):
    await user.send(message)


"""async def login(client): 
    await client.login('NjM0MDQ5NzIxMjU3ODIwMTcz.Xac20Q.pzdt3QGc7lUb7RYxqkDtwJITsw8',bot=True)
    await client.send()"""


if __name__== "__main__":
    client.run('NjM0MDQ5NzIxMjU3ODIwMTcz.Xac20Q.pzdt3QGc7lUb7RYxqkDtwJITsw8',bot=True)






