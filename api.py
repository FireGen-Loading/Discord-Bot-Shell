import os
import discord
import internal
import asyncio
import sys

async def r(message, *stuff ):
    contents = " ".join(stuff)
    x = input('!Image Path :')

    try:
        await internal.Reply_Message(contents,x,int(message))
    except Exception as e:
        print(e)


async def m(*stuff ):
    contents = " ".join(stuff)
    x = input('!Image Path :')
    try:
        await internal.Message(contents, x)
    except Exception as e:
        print(e)

    
async def i(*stuff):
    contents = " ".join(stuff)
    try:
        await internal.Message("", contents)
    except Exception as e:
        print(e)




# internal commands


async def exit(*stuff):
    internal.logged_in = False
    await internal.bot.close()
    loop = asyncio.get_event_loop()
    loop.stop()
    loop.close()

    sys.exit()


async def logout(*stuff):
    await exit()




async def cd(*stuff):
    path_splitter : str = '/'
    index_offset : int = 0
    if os.name == 'nt':
        path_splitter = '\\'
        index_offset = 1
    elif os.name == 'posix':
        path_splitter = '/'
        index_offset = 0

    contents = " ".join(stuff)

    if contents.startswith('.' + path_splitter):
        contents = contents.removeprefix('.' + path_splitter)

    Path = contents.split(path_splitter)

    

    if contents != "":

        if contents == "\\":
            if os.name == 'nt':
                internal.working_path = ["C:"]
            elif os.name == 'posix' :
                internal.working_path = []

        elif 0 + index_offset < len(contents):
            if contents == "..":
                internal.working_path.pop()

            elif contents[1] == ':' and contents[2] == path_splitter:
                if os.path.exists(path_splitter.join(Path)):

                    if os.path.isdir(path_splitter.join(Path)):

                        internal.working_path = Path
                    else:
                        print("Not a directory")

                else:
                    print("Invalid Path")


            else:
                tmp = path_splitter.join(internal.working_path + Path) 
                if os.path.exists(tmp):

                    if os.path.isdir(tmp):
                        internal.working_path += Path

                    else:
                        print("Not a directory")
                else:
                    print("Invalid Path")

async def dm( user , *stuff):
    contents = " ".join(stuff)
    x = input('!Image Path :')
    try:
        await internal.DirectMessage(contents, x, int(user))
    except Exception as e:
        print(e)


async def getuc(id):
    try:
        Return = await internal.Get_User_DM_Channel(id)
        channel : discord.DMChannel = Return[0]
        user : discord.user = Return[1]

        print(f"{user} channel id: {str(channel.id)}")
    except Exception as e:
        print(e)


async def con(id,limit):
    channel : (discord.TextChannel | discord.DMChannel)
    channel = await internal.bot.fetch_channel(id)


    try:
        n = await internal.Get_logs(channel,int(limit))
        for i in n:

            print(f"[{i.created_at.hour}:{i.created_at.minute}] {i.author}\n>>{i.content}")

    except Exception as e:
        print(e)
        print(e.with_traceback())

async def cona(id,limit):
    channel : (discord.TextChannel | discord.DMChannel)
    channel =  await internal.bot.fetch_channel(id)

    try:
        n = await internal.Get_logs(channel, int(limit))
        for i in n:
            print(f"[{i.created_at.hour}:{i.created_at.minute}] {i.author}\n[UID : {i.author.id}] [MID : {i.id}]\n>>{i.content}")

    except Exception as e:
        print(e)