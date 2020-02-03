#!/usr/bin/env python3

import discord

b = 'List of commands\n#help, #unity, #symbol, #flame, #ied, #level, #dojo, #oz, #union, #achievement, #apple, #royal, #wonder, #luna sweet/dream, #male/female hair/face\n\n'

def help_main():
    output = discord.Embed(title = "help", description = '%s' % (b), color = 0x00ff00)
    return output
