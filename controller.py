import asyncio
import discord
import types
import api
import sty
default_path = sty.fg(0x55,0xb9,0xc4)
default_end = f"/ →\n{sty.fg(0x63,0xF0,0x8C)}➜{sty.fg.rs}"


def main():
    is_logged = False
    while not is_logged:
        n = input("Enter profile config \nName:")
        result = api.internal.LoadProfile(n)
        if result:
            print("Logged in with local")
            is_logged = True
            api.internal.logged_in = True
            api.internal.bot.run(api.internal.token)
        else: 
            print("No local profile as such exists")


@api.internal.bot.event 
async def on_ready():
    # guild = await client.fetch_guild(0)
    # role = guild.get_role(0)
    # role = await guild.create_role(name="e", permissions=discord.Permissions(0), colour=discord.Colour(0xff0000))
    # print(role.id)
    # member : Member = await guild.fetch_member(0)
    # await member.add_roles(role)
    # print(member)
    
    while api.internal.logged_in:
        x = input(default_path + "/ → /".join(api.internal.working_path)  + default_end)
        n = x.split(' ')
        com = n[0]

        if hasattr(api,com):
            Iobject = getattr(api,com)
            if type(Iobject) == types.FunctionType:
                await Iobject(*n[1:])
            else:
                print("Command does not exist")

        else:
            print("Command does not exist")


if __name__ == "__main__":
    main()