#!/usr/bin/env python3

import discord
import csv

def UnityTrainingCenter1(msg1, msg2):
    file = "module/database/level/UnityTrainingCenter.csv"
    time = float(0)
    need = int(0)

    with open(file, newline='', encoding="utf-8") as database:
        freader = csv.reader(database)
        next(freader)
        for row_list in freader:
            if msg1 <= int(row_list[0]) < msg2:
                time += float(row_list[4])
                need += int(row_list[3])
    hour = int(time / 60)
    day = int(hour / 24)
    title = "Unity Training %d → %d" % (msg1, msg2)
    data = 'EXP needed : %s\n' % format(need, ',')
    data += 'Time required : '
    if day != 0:
        data += "%s Day(s) " % format(day, ',')
    if hour != 0:
        data += "%s Hour(s) " % format((hour - (day * 24)), ',')
    data += "%2.2f minute(s)\n\n" % (time - (hour * 60))
    data += "Unity Training Center Entrance Charm(Diamond) : %d\n" % (int(time / 60 / 18) + 1)
    data += "Unity Training Center Entrance Charm(Gold) : %d\n" % (int(time / 60 / 9) + 1)
    data += "Unity Training Center Entrance Charm(Silver) : %d\n" % (int(time / 60 / 3) + 1)
    data += "Unity Training Center Entrance Charm(Bronze): %d\n" % (int(time / 60) + 1)

    output = discord.Embed(title=title, description=data, color=0x0000ff)

    return output


def UnityTrainingCenter_main(msg):
    if len(msg) == 3:
        if msg[1].isdecimal() and msg[2].isdecimal():
            msg1 = float(msg[1])
            msg2 = float(msg[2])
            if msg1 == int(msg1) and msg2 == int(msg2):
                msg1 = int(msg1)
                msg2 = int(msg2)
                if 105 <= msg1 < 275 and 105 < msg2 <= 275:
                    if msg1 > msg2:
                        output = discord.Embed(title="Warning!!!", description='Start level cannot exceed the Goal level!',
                                               color=0xff0000)
                    else:
                        output = UnityTrainingCenter1(msg1, msg2)
                else:
                    output = discord.Embed(title="Warning!!!", description='Number out of range', color=0xff0000)
                    output.set_footer(text="Input has to be at least 105 and cannot go above 275")
            else:
                output = discord.Embed(title="Warning!!!", description='Input MUST be integer', color=0xff0000)
        else:
            output = discord.Embed(title="Warning!!!", description='You need two inputs', color=0xff0000)
            output.set_footer(text="Ex) #unity 105 150")
    else:
        output = discord.Embed(title="#unity",
                               description='You can use it by typing #unity (Start level) (goal level), It will give you the calculated time that you will need to train to reach the goal level.',
                               color=0x00ff00)
        output.set_footer(text="Ex) #unity 105 150")

    return output
