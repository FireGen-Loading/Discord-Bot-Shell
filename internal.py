import discord
import os
import json

channel_id : int
token : str

logged_in = False

working_path = []

intents = discord.Intents.all()
bot = discord.Client(intents=intents)



def LoadProfile(name) -> bool:
    global working_path
    global channel_id
    global token

    path = os.getcwd()

    Profile = f"{path}/Profiles/{name}.json"
    if os.path.exists(Profile):
        working_path = path.split('\\')
        file = open(Profile, 'r')
        settings = json.load(file)
        file.close()

        channel_id = settings['Channel id']
        token = settings['Token']
        
        
        return True
    else:
        return False
        
async def Message(content : str,path : str):
    channel : discord.TextChannel
    channel = bot.get_channel(channel_id)

    if path != "":
        file = open("\\".join(working_path) + '\\' + path, 'rb')
        filedisc = discord.File(file)
        await channel.send(content, file=filedisc)
        filedisc.close()
        file.close()
        return

    else:
        await channel.send(content)


async def Reply_Message(content : str,path : str ,id : int):
    channel : discord.TextChannel
    channel = bot.get_channel(channel_id)
    message : discord.Message
    message = await channel.fetch_message(id)
    if path != "": 
        file = open("\\".join(working_path) + '\\' + path, 'rb')
        filedisc = discord.File(file)
        await message.reply(content, file=filedisc)
        filedisc.close()
        file.close()
        return
    else:
        await message.reply(content)


async def DirectMessage(content : str,path : str ,id : int):
    user : discord.User = await bot.fetch_user(id)
    if path != "": 
        file = open("\\".join(working_path) + '\\' + path, 'rb')
        filedisc = discord.File(file)
        await user.send(content=content, file=filedisc)
        filedisc.close()
        file.close()
    else:
        await user.send(content)

async def Get_User_DM_Channel(id : int) -> tuple:

    user : discord.User = await bot.fetch_user(id)
    if user.dm_channel == None:
        return await user.create_dm(), user
    else:
        return user.dm_channel,user 

async def Get_logs(channel : (discord.TextChannel | discord.DMChannel), limit) -> list[discord.Message]:
    history =await channel.history(limit=limit).flatten()

    history.reverse()
    return history
        
