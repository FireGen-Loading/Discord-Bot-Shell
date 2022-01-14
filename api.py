from ntpath import join
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
    contents = " ".join(stuff)

    if contents.startswith('.\\'):
        contents = contents.removeprefix('.\\')

    Path = contents.split('\\')

    

    if contents != "":

        if contents == "\\":
            internal.working_path = ["C:"]

        elif 1 < len(contents):
            if contents == "..":
                internal.working_path.pop()

            elif contents[1] == ':' and contents[2] == '\\':
                if os.path.exists("\\".join(Path)):

                    if os.path.isdir("\\".join(Path)):

                        internal.working_path = Path
                    else:
                        print("Not a directory")

                else:
                    print("Invalid Path")


            else:
                tmp = "\\".join(internal.working_path + Path) 
                if os.path.exists(tmp):

                    if os.path.isdir(tmp):
                        internal.working_path += Path

                    else:
                        print("Not a directory")
                else:
                    print("Invalid Path")

