import asyncio
from aiohttp import web
import discord
import os
import json
import time
from aiohttp import ClientSession

with open('./variables.json') as file:
    variables = json.load(file)


routes = web.RouteTableDef()

async def online_discord_dm(*args,**kwargs):

    headers = { "Authorization":"Bot {}".format(variables["BOT_KEY"]),
            "User-Agent":"myBotThing (http://some.url, v0.1)",
            "Content-Type":"application/json", }

    async with ClientSession(headers=headers) as session:
        
        ### tirar isso no deploy ###
        #variables["GUILD_OWNER_DISCORD_USER_ID_test"] = str(178144275358285825)
        ### --------------------- ###

        if "GUILD_OWNER_DM_CHANNEL" not in variables:
            async with session.post(variables["DISCORD_API_BASE_URL"]+'/users/@me/channels',json={'recipient_id':variables["GUILD_OWNER_DISCORD_USER_ID"] }) as channel:
                print(channel)
                channel= await channel.json()
                variables["GUILD_OWNER_DM_CHANNEL"] = channel['id']
                with open('./variables.json','w') as file:
                    json.dump(variables,file,ensure_ascii=True)

        message = f'BUNDINHA SEU ARROMBADO! \nJá que o senhor está em live, em 5 minutos vou mandar pros cornos que você chama de discord o seguinte: \n\n\t"{variables["TWITCH_ONLINE_MESSAGE"]} {variables["GUILD_OWNER_STREAM_URL"]}"\n\n Se o sabichão quiser que eu fale outra coisa, manda aqui pro pai que ele da conta taokey?'
        nm = f'/channels/{variables["GUILD_OWNER_DM_CHANNEL"]}/messages'
        await session.post(variables["DISCORD_API_BASE_URL"]+nm,json={'content':message})

        await asyncio.sleep(300)
        await session.post(f"https://discordapp.com/api/channels/{variables['CHANNEL_ANNOUNCMENT_ID']}/messages",json={"content": f'<@&{variables["ROLE_STREAM_PING_ID"]}>  ' +variables["MESSAGE"] +" " +variables["GUILD_OWNER_STREAM_URL"]})


@routes.post('/twitch')
async def twitch_handler(request):
    parsed = await request.json()
    if "challenge" in parsed.keys():
        return web.Response(text=parsed["challenge"])
    
    else:
        await online_discord_dm()
    return(web.Response(text='imundisse'))

@routes.get('/twitch')
async def send_dm(request):
    await online_discord_dm()
    return(web.Response(text='imundisse'))

@routes.get('/')    
async def disse(request):
    return web.Response(text="Imundisse disse")


app = web.Application()
app.add_routes(routes)

'''def run():
    web.run_app(app,port=os.environ.get('PORT'))'''

