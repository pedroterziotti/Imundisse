import discord
from discord.ext import commands
import random

class UGA(commands.Cog):
    '''Seção do bot separada para ugar'''

    def __init__(self,client):
        self.client = client
        self.sujera = {"Kilfrox#7389": "Julin", "ChoroVendoAnime#4438": "Alê", "Brono#7259": "Brono",
          "scorpiontaken#5498":"Pedro", "Jott4#2505":"João","Morfeu#6627": "Rods", "Pato#9781": "Juan",
          "Terziotti#0546": "Gabriel", "homio#3764": "Czar"}
        self.n_mensagens=0
        self.mensagem_de_uga=10
    
    @commands.Cog.listener()
    async def on_message(self, message):
        
        if message.author == self.client.user: return
        if message.content.startswith("Ping"):
            await message.channel.send("Pong")

        self.n_mensagens+=1
        if self.n_mensagens == self.mensagem_de_uga :
            self.n_mensagens =0
            try:
                final,self.mensagem_de_uga = uga(message.content)
                await message.channel.send(final)

            except: return

        if message.content.startswith('uga uga'):
            await message.channel.send(f'uga uga {self.sujera[str(message.author)]}')

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

def setup(client):
    client.add_cog(UGA(client))