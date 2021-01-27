import discord
import random


client = discord.Client()

contador = 0
numero = 10

sujera = {"Kilfrox#7389": "Julin", "ChoroVendoAnime#4438": "Alê", "Brono#7259": "Brono",
          "scorpiontaken#5498":"Pedro", "Jott4#2505":"João","Morfeu#6627": "Rods", "Pato#9781": "Juan",
          "Terziotti#0546": "Gabriel", "homio#3764": "Czar"}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    
    global contador
    global numero
    contador+= 1
    if contador == numero:
        contador =0
        try:
            final,numero = uga(message.content)
            await message.channel.send(final)
        except:
            return

    if message.content.startswith('uga uga'):
        await message.channel.send(f"uga uga {sujera[str(message.author)]}")

def uga(mensagem):
    mensagem = mensagem.split(' ')
    quantidade = random.randint(1,len(mensagem))
    
    palavras = []
    for a in range(quantidade):
        novo= random.randint(1,len(mensagem))
        while novo in palavras:
            novo= random.randint(1,len(mensagem))
        palavras.append(novo)

    
    for a in range(quantidade):
        if len(mensagem[palavras[a]-1]) <5:
            mensagem[palavras[a]-1] = 'uga'
        elif len(mensagem[palavras[a]-1]) >4:
            if random.choice(['começo','fim']) == 'fim':
                mensagem[palavras[a]-1] = mensagem[palavras[a]-1][0:-3]+ 'uga'
        
            else:
                mensagem[palavras[a]-1] = 'uga'+mensagem[palavras[a]-1][3:]
    final = ''
    for a in range(len(mensagem)):
        final+= mensagem[a] + ' '
    numero =random.randint(1,8)
    return(final,numero)


client.run('Token')