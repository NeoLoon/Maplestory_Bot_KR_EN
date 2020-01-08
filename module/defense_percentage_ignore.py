#!/usr/bin/env python3

import discord


def defense_percentage_ignore1(defense_percentage_ignore, percentage):
    monster_damage_percentage = 1 - (percentage * (1 - defense_percentage_ignore))
    if monster_damage_percentage < 0:
        monster_damage_percentage = 0
    return monster_damage_percentage


def defense_percentage_ignore_main(msg):
    if len(msg) is 1:
        output = discord.Embed(title="#ied",
                               description='You can input #ied (ied 1) (ied 2)... (ied n), and check the damage % you do to a mob.',
                               color=0x00ff00)
        output.set_footer(text="Ex. #ied 85 40 20")
    num = 2
    for i in msg:
        if not i.isdecimal():
            num = num - 1
    if num is 1:
        defense_percentage_ignore = 1
        defense_percentage_ignore_options = list(range(1, len(msg), 1))
        for i in defense_percentage_ignore_options:
            defense_percentage_ignore = defense_percentage_ignore * (1 - float(msg[i]) / 100)
        defense_percentage_ignore = 1 - defense_percentage_ignore

        if defense_percentage_ignore > 1:
            output = discord.Embed(title="Warning!!!", description='ied cannot be higher than 100%.', color=0xff0000)
            output.set_footer(text="#ied (ied 1) (ied 2)... (ied n)")
        else:
            output = discord.Embed(title="ied %3.2f %% damage to a mob" % (defense_percentage_ignore * 100),
                                   description="Damage to 100%% def. : %3.2f %%\n"
                                               "Damage to 150%% def. : %3.2f %%\n"
                                               "Damage to 200%% def. : %3.2f %%\n"
                                               "Damage to 250%% def. : %3.2f %%\n"
                                               "Damage to 300%% def. : %3.2f %%\n"
                                               % (defense_percentage_ignore1(defense_percentage_ignore, 1) * 100,
                                                  defense_percentage_ignore1(defense_percentage_ignore, 1.5) * 100,
                                                  defense_percentage_ignore1(defense_percentage_ignore, 2) * 100,
                                                  defense_percentage_ignore1(defense_percentage_ignore, 2.5) * 100,
                                                  defense_percentage_ignore1(defense_percentage_ignore, 3) * 100),
                                   color=0x0000ff)
    else:
        output = discord.Embed(title="Warning!!!", description='You can only use number in #ied.', color=0xff0000)
        output.set_footer(text="#ied 85 40 20")

    return output
