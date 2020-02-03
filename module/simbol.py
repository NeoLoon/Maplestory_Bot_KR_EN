#!/usr/bin/env python3

import discord


def simbol1(a, b):
    result1 = 0
    result2 = 0
    for i in range(1, a):
        result1 += (i * i) + 11
    for i in range(1, b):
        result2 += (i * i) + 11
    result = result2 - result1
    return format(result, ',')


def simbol2(a, b):
    result1 = 0
    result2 = 0
    for i in range(1, a):
        result1 += 2370000 + (7130000 * i)
    for i in range(1, b):
        result2 += 2370000 + (7130000 * i)
    result = result2 - result1
    return format(result, ',')


def simbol3(a, b):
    result1 = 0
    result2 = 0
    for i in range(1, a):
        result1 += 12440000 + (6600000 * i)
    for i in range(1, b):
        result2 += 12440000 + (6600000 * i)
    result = result2 - result1
    return format(result, ',')


def simbol_main(msg):
    if len(msg) == 3:
        if msg[1].isdecimal() and msg[2].isdecimal():
            msg1 = float(msg[1])
            msg2 = float(msg[2])
            if msg1 == int(msg1) and msg2 == int(msg2):
                msg1 = int(msg1)
                msg2 = int(msg2)
                if 0 < msg1 < 21 and 0 < msg2 < 21:
                    if msg1 > msg2:
                        output = discord.Embed(title="Warning!!!", description='Option 1 cannot exceed Option 2!',
                                               color=0xff0000)
                        return output
                    else:
                        output = discord.Embed(title="Symbol Level %d → %d" % (msg1, msg2),
                                               description='Total amount of symbols needed : %s \n Vanishing Journey Symbol Upgrade fee : %s \n Chuchu/Lach/Arcana/Morass/Esfera Symbol Upgrade fee : %s'
                                                           % (simbol1(msg1, msg2), simbol2(msg1, msg2),
                                                              simbol3(msg1, msg2)), color=0x0000ff)
                        return output
                else:
                    output = discord.Embed(title="Warning!!!", description='Number out of bound!', color=0xff0000)
                    output.set_footer(text="Input must be higher than 1 and lower than 21!")
                    return output
            else:
                output = discord.Embed(title="Warning!!!", description='Input must be an integer!', color=0xff0000)
        else:
            output = discord.Embed(title="Warning!!!", description='You must input two integers!', color=0xff0000)
            output.set_footer(text="#symbol (Start level) (Target level)")
    else:
        output = discord.Embed(title="#symbol", description='Type #symbol (Start level) (Target level) to see how much mesos and symbols are needed to upgrade the symbols.', color=0x00ff00)
        output.set_footer(text="#symbol 7 12")

    return output
