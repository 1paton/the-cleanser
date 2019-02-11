import discord
from discord.ext import commands
import discord.ext
import asyncio
import time

Client=discord.Client()
client= commands.Bot(command_prefix='!')

#Banned Words
chat_filter=["FUCK", "F U C K", "FUCKING", "FUC", "F U C K I N G", "SHIT", "SHITING","BITCH", "BITCHING" "SHAT", "ASS", "ASSHOLE", "PUSSY", "BASTARD", "ARSE", "CUNT", "GAY", "NIBBA", "FUC", "GEY","B1CH","TITS","VAGINA","DICK","PENIS","THOT"]
bypass_list= []
msg1= "Do not use the following words:F*ck ,sh*t ,b*tch ,shat ,a$$ ,a$$hole ,pu$$y ,b@st@rd ,@rse ,c*nt ,gay ,t*ts ,v*gina ,etc "

ban_filter=["RAID"]

@client.event
async def on_ready() :
    await client.change_presence(game=discord.Game(name="Watching Chat"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter :
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "__**Message Removed.**__")
                    msg = (msg1)
                    await client.send_message(message.author, msg)
                except discord.errors.NotFound:
                    return



client.run("NTQ0MjQ4NjkyODMyNjAwMDc0.D0IZUg.D1AojRM6sEnIj4W5SDK5aPED0RM")
