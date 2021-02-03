import discord
from discord.ext import commands,tasks
import requests
import json

API_Key ='RGAPI-cec1f861-f9f7-4d89-8068-67ee8c0302ea'

sujera ={'PoO_oc8nvK1XpRMq3C1xuqLsY4g-GvYSvFGY6nfeeKRlIg':'João',
        'Ojf9TSrs1JKzmdEHRaPWplMWxXJ-QYmHULi_k0YaP94HjA':'Czar',
        'S46jcYKvdnr8-gEPhIpbmEdbuZ6cOzPi6N9mBXfpMU7QaD4': 'Brono',
        'BzlfXfF2dvIIfZubEU9Ol2ym6dNIb64Ts1XxzheWr2AM28w': 'Juan',
        "T_J8paFvYmMEYXMdd4lGxZi54QiMeLa0MTSU-qR1QYYEW1w":'Alê',
        'CYRyF8WsN5KKhaIy2gdZF9aA7NgaBvqHIOA9-1Uh-P0dSw': 'Pedro',}
        #"XRVRcUJ7GBvKKtoz6XNy2EhYNBtTBJJt3euighRtqoKk8Uc": 'FMS'}

class EmJogo(commands.Cog):
    ''' Verifica quando alguém entra na Fila'''
    def  __init__(self,client):
        self.client = client
        latest_patch = requests.get('https://ddragon.leagueoflegends.com/api/versions.json').json()[0]
        champions = requests.get(f'http://ddragon.leagueoflegends.com/cdn/{latest_patch}/data/en_US/champion.json').json().get('data')
        arquivo = open('./Dados/champions.json','w')
        json.dump(champions, arquivo)
        arquivo.close()
        self.verificar.start()


    @tasks.loop(seconds = 120)
    async def verificar(self):
        nomes = []; bonecos =[]
        for id in sujera.keys():
            r = requests.get(f'https://br1.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{id}?api_key={API_Key}')
            if r.status_code == 200:
                match= r.json()
                for participant in match.get('participants'):
                    if participant.get('summonerId') == id:
                        nomes.append(sujera.get(id))
                        arquivo = open('./Dados/champions.json')
                        champions = json.load(arquivo)
                        for champion in champions.values():
                            '''print(champion.get('key'))
                            print(participant.get('championId'))'''
                            if str(champion.get('key')) == str(participant.get('championId')):
                                bonecos.append(champion.get('id'))
                        arquivo.close()
            '''print(nomes)
            print(bonecos)'''
        self.nomes = nomes; self.bonecos = bonecos

    @commands.command()
    async def ingame(self,ctx):
        mensagem=''
        if len(self.nomes) ==0:
            await ctx.send('Ninguém está jogando arrombado')
        else:
            for a in range(len(self.nomes)):
                mensagem += f'{self.nomes[a]} está jogando de {self.bonecos[a]} \n'
            await ctx.send(mensagem)


                        



def setup(client):
    client.add_cog(EmJogo(client))