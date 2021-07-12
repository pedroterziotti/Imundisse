from discord.ext import commands
import discord
from discord.embeds import Embed
from discord import Colour
import json
from discord.enums import ActivityType

'''
GUILD_ID = 830505972451639296
ROLE_MESSAGE_ID = 836602516740898866
ROLE_MESSAGE_CHANNEL_ID=836347232843726919
ROLE_STREAM_PING_ID=836346543228452944
ROLE_SUB_ID = 836314888477343805
ROLE_CUSTOM_SUB_ID =830508298649993278
STREAMER_ROLE = 836345815656038420
ID_CHANNEL_OWNER =178307072633470978
CHANNEL_ANNOUNCMENT_ID= 836331956068155402
CHANNEL_PARTNER_STREAMER_ID= 836332807499546694
'''
with open('./variables.json') as file:
    variables = json.load(file)

EMOJI_ROLE_DICT = { '🥂' :variables['ROLE_STREAM_PING_ID'] }

def _default_pre_handler(event):
    pass 

class Server_Gabriel(commands.Cog):
    ''' Classe que cuida do servidor do gabriel'''

    def __init__(self,client):
        '''Construtor da Classe '''
        self.client = client
        self._emoji_to_role_config()

    def _emoji_to_role_config(self, ):
        ''' Método que Inicializa o dicionário das emoji-roles'''
        self.role_message_id = variables['ROLE_MESSAGE_ID'] # ID of the message that can be reacted to to add/remove a role.
        self.emoji_to_role={}
        for key in EMOJI_ROLE_DICT:
            self.emoji_to_role[discord.PartialEmoji(name=key)] = EMOJI_ROLE_DICT[key]
         
    @commands.Cog.listener('on_raw_reaction_add')
    async def roles_emoji_give(self, payload: discord.RawReactionActionEvent):
        ''' Distribui os cargos baseado em reação '''
        
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.client.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        try:
            # Finally, add the role.
            await payload.member.add_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass

    @commands.Cog.listener('on_raw_reaction_remove')
    async def role_emoji_take(self, payload: discord.RawReactionActionEvent):
        ''' Remove cargos baseado em reações'''
        """Removes a role based on a reaction emoji."""
        # Make sure that the message the user is reacting to is the one we care about.
        if payload.message_id != self.role_message_id:
            return

        guild = self.client.get_guild(payload.guild_id)
        if guild is None:
            # Check if we're still in the guild and it's cached.
            return

        try:
            role_id = self.emoji_to_role[payload.emoji]
        except KeyError:
            # If the emoji isn't the one we care about then exit as well.
            return

        role = guild.get_role(role_id)
        if role is None:
            # Make sure the role still exists and is valid.
            return

        # The payload for `on_raw_reaction_remove` does not provide `.member`
        # so we must get the member ourselves from the payload's `.user_id`.
        member = guild.get_member(payload.user_id)
        if member is None:
            # Make sure the member still exists and is valid.
            return

        try:
            # Finally, remove the role.
            await member.remove_roles(role)
        except discord.HTTPException:
            # If we want to do something in case of errors we'd do it here.
            pass

    @commands.Cog.listener('on_member_update')
    async def partner_start_streaming(self,before, after):
        '''Atribui cargos pra Streamers'''
        if after.guild.id != variables['GUILD_ID']:
            return
        try:
            if after.activity == None or after.id == variables['ID_CHANNEL_OWNER']:
                return
            else:
                if before.activity == None and after.activity.type == ActivityType.streaming:
                    role = after.guild.get_role(variables['STREAMER_ROLE'])
                    await after.add_roles(role)
                    channel = self.client.get_channel(variables['CHANNEL_PARTNER_STREAMER_ID'])
                    EMBED={
                        'title':f'{after.display_name}',
                        'type': 'rich',
                        'url':f'{after.activity.url}',
                        'colour': Colour.dark_purple().value,
                    }
                    embed = Embed.from_dict(EMBED)
                    #embed.set_image(url = 'https://www.twitch.tv/enterth64')
                    embed.set_author(name=f'{after.activity.name}')

                    #await channel.send(f'{after.nick} está transmitindo "{after.activity.name}"')
                    await channel.send(f'{after.display_name} está transmitindo {after.activity.name}! Confira em: {after.activity.url}')
                elif before.activity.type != ActivityType.streaming and after.activity.type == ActivityType.streaming:
                    role = after.guild.get_role(variables['STREAMER_ROLE'])
                    await after.add_roles(role)
                    channel = self.client.get_channel(variables['CHANNEL_PARTNER_STREAMER_ID'])
                    EMBED={
                        'title':f'{after.display_name}',
                        'type': 'rich',
                        'url':f'{after.activity.url}',
                        'colour': Colour.dark_purple().value,
                    }
                    embed = Embed.from_dict(EMBED)
                    #embed.set_image(url = 'https://www.twitch.tv/enterth64')
                    embed.set_author(name=f'{after.activity.name}')

                    #await channel.send(f'{after.nick} está transmitindo "{after.activity.name}"')
                    await channel.send(f'{after.display_name} está transmitindo {after.activity.name}! Confira em: {after.activity.url}')

                    #await channel.send(f'{after.nick} está transmitindo "{after.activity.name}"')
                else: return 

        except AttributeError:
            pass

    @commands.Cog.listener('on_member_update')
    async def partner_stop_streaming(self,before, after):
        '''Retira cargos pra Streamers'''
        if after.guild.id != variables['GUILD_ID']:
            return
        try:
            if before.activity == None:
                return
            elif before.activity.type == ActivityType.streaming and after.activity ==None:
                role = after.guild.get_role(variables['STREAMER_ROLE'])
                await after.remove_roles(role)
            elif before.activity.type == ActivityType.streaming and after.activity.type != ActivityType.streaming:
                role = after.guild.get_role(variables['STREAMER_ROLE'])
                await after.remove_roles(role)
            else: return

        except AttributeError:
            pass
                        
    @commands.Cog.listener('on_member_update')
    async def sub_role(self,before,after):
        '''Dá e tirar os cargos de sub'''
        guild= before.guild
        if guild.id == variables['GUILD_ID']:
            sub = guild.get_role(variables['ROLE_SUB_ID'])
            subrole = guild.get_role(variables['ROLE_CUSTOM_SUB_ID']) 
            if sub in after.roles:
                if subrole not in after.roles:
                    await after.add_roles(subrole)
            if sub not in after.roles:
                if subrole in after.roles:
                    await after.remove_roles(subrole)

    @commands.Cog.listener('on_message')
    async def twitch_online_message(self,ctx: discord.Message):
        if ctx.channel == variables["GUILD_OWNER_DM_CHANNEL"]:
            if ctx.author != self.client.user:
                variables['MESSAGE'] = ctx.content
                with open('./variables.json','w') as file:    
                    json.dump(variables,file,ensure_ascii=True)

        return

def setup(client):
    
    client.add_cog(Server_Gabriel(client))


