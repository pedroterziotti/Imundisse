import discord
from discord import activity
from discord import emoji
from discord import guild
from discord.ext import commands, tasks
from discord.embeds import Embed
from discord import Colour
import asyncio
import json

intents = discord.Intents.all()
intents.members = True
#
with open('./variables.json') as file:
    variables = json.load(file)

#client = commands.Bot(command_prefix= "!", intents=intents)
client = discord.Client(intents=intents)


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

"""async def login(client): 
    await client.login('NjM0MDQ5NzIxMjU3ODIwMTcz.Xac20Q.pzdt3QGc7lUb7RYxqkDtwJITsw8',bot=True)
    await client.send()"""


if __name__== "__main__":
    client.run('NjM0MDQ5NzIxMjU3ODIwMTcz.Xac20Q.pzdt3QGc7lUb7RYxqkDtwJITsw8',bot=True)






