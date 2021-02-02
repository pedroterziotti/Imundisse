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

    @commands.command()
    async def play(self,ctx, url :str):
        musica_existe = os.path.isfile("musica.mp3")
        try:
            if musica_existe:
                os.remove("musica.mp3")
        except PermissionError:
            return

        voiceChannel = ctx.author.voice.channel
        await voiceChannel.connect()
        voice =discord.utils.get(self.client.voice_clients, guild=ctx.guild)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "musica.mp3")
        voice.play(discord.FFmpegPCMAudio("musica.mp3"))

    @commands.command()
    async def sair(self,ctx):
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

def setup(client):
    client.add_cog(DJ(client))