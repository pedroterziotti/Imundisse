from inspect import indentsize
import discord
from discord.channel import VoiceChannel
from discord.ext import commands

import youtube_dl 
import os


class DJ(commands.Cog):
    '''Separa as funções de DJ'''

    def __init__(self,client):
        self.client = client
        self.musicas = [] 

    @commands.command()
    async def play(self,ctx, *url :str):
        
        self.musicas.append(url)
        print(self.musicas[0])
        voiceChannel = ctx.author.voice.channel
        try:
            await voiceChannel.connect()
        except: pass
        voice =discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        self.tocar(voice)


    def tocar(self,voice):
        if len(self.musicas) !=0:
            musica_existe = os.path.isfile("musica.mp3")
            try:
                if musica_existe:
                    os.remove("musica.mp3")
            except PermissionError:
                return

            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl: 
                try:
                    ydl.download([self.musicas[0]])
                except:
                    pesquisa =''
                    for a in range(len(self.musicas[0])):
                        pesquisa += self.musicas[0][a] + ' '
                    ydl.extract_info(f"ytsearch:{pesquisa}")['entries'][0]
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "musica.mp3")
            self.musicas.pop(0)
            voice.play(discord.FFmpegPCMAudio("musica.mp3"), after= lambda error: self.tocar(voice))

    @commands.command()
    async def leave(self,ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_connected():
            await voice.disconnect()
        else: await ctx.send("Ja sai desgraça!")


    @commands.command()
    async def pause(self,ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_playing():
            voice.pause()
        else: await ctx.send("To parado o caralho")

    @commands.command()
    async def resume(self,ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        if voice.is_paused():
            voice.resume()
        else: await ctx.send("Não da pra voltar porra")

    @commands.command()
    async def stop(self,ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()

    @commands.command()
    async def next(self,ctx):
        voice = discord.utils.get(self.client.voice_clients, guild=ctx.guild)
        voice.stop()
        self.tocar(ctx)

def setup(client):
    client.add_cog(DJ(client))