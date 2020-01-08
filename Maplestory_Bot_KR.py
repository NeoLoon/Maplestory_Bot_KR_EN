#!/usr/bin/env python3

from module.help import *
from module.simbol import *
from module.additional_options import *
from module.defense_percentage_ignore import *
from module.level import *
from module.information import *
from module.gambling import *

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('hello')
    activity = discord.Game(name="#help for help")
    await client.change_presence(status=discord.Status.idle, activity=activity)

@client.event
async def on_message(message):
    if message.content.startswith("#help"):
        output = help_main()
        await message.channel.send(embed=output)

    if message.content.startswith("#symbol"):
        msg = message.content.split(" ")
        output = simbol_main(msg)
        await message.channel.send(embed=output)

    if message.content.startswith("#flame"):
        msg = message.content.split(" ")
        output = additional_options_main(msg)
        await message.channel.send(embed=output)

    if message.content.startswith("#ied"):
        msg = message.content.split(" ")
        output = defense_percentage_ignore_main(msg)
        await message.channel.send(embed=output)

    if message.content.startswith("#level"):
        msg = message.content.split(" ")
        output = level_main(msg)
        await message.channel.send(embed=output)

    if message.content.startswith("#info")\
            or message.content.startswith("#dojo")\
            or message.content.startswith("#seed")\
            or message.content.startswith("#oz")\
            or message.content.startswith("#union")\
            or message.content.startswith("achievement"):
        msg = message.content.split(" ")
        output = information_main(msg)
        await message.channel.send(embed=output)

    if message.content.startswith("#golden")\
            or message.content.startswith("#apple")\
            or message.content.startswith("#royal")\
            or message.content.startswith("#wonder") \
            or message.content.startswith("#wongki")\
            or message.content.startswith("#luna")\
            or message.content.startswith("#male")\
            or message.content.startswith("#female"):
        msg = message.content.split(" ")
        display_name = message.author.display_name
        output = gambling_main(msg, display_name)
        await message.channel.send(embed=output)

client.run('token')
