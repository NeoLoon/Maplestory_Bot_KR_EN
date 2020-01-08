#!/usr/bin/env python3

import discord
import csv
import requests
from bs4 import BeautifulSoup
from module.timeout import *


@timeout(3)
def level1(url):
    url = requests.get(url)
    html = url.content
    soup = BeautifulSoup(html, 'html.parser')
    ranking = soup.select(".rank_table_wrap table > tbody > tr")

    result = [[], [], [], [], [], [], []]

    for i in range(0, len(ranking)):
        if ranking[i].select('td')[0].text.strip():
            result[0].append(ranking[i].select('td')[0].text.strip())  # 순위
            result[1].append(ranking[i].select('a')[0].text.strip())  # 닉네임
            result[2].append(ranking[i].select('dd')[0].text.strip())  # 직업 / 직업
            result[3].append(ranking[i].select('td')[2].text.strip())  # 레벨
            result[4].append(ranking[i].select('td')[3].text.strip())  # 경험치량
            result[5].append(ranking[i].select('td')[4].text.strip())  # 인기도
            result[6].append(ranking[i].select('td')[5].text.strip())  # 길드

    return result


def level2(result, msg1):
    optlist = [[], [], [], [], [], [], []]
    data = ''
    file = "module/database/level/level.csv"
    if not result:
        output = discord.Embed(title="Warning!!!", description='No response from the server.', color=0xff0000)
        output.set_footer(text="Please try again later.")
    else:
        for i in range(0, len(result[0])):
            if result[1][i] == msg1:
                for j in range(0, 6):
                    optlist[j] = result[j][i]

        title = optlist[1]

        if not title:
            output = discord.Embed(title="Warning!!!", description='Cannot find the character in the ranking!', color=0xff0000)
            output.set_footer(text="IGNs are case-sensitive.")
        else:
            now_level = optlist[3]
            now_level = now_level[3:]
            level_250 = str(250)
            level_275 = str(275)

            with open(file, newline='', encoding="utf-8") as database:
                freader = csv.reader(database)
                for row_list in freader:
                    station_name = row_list[0]
                    if station_name.startswith(now_level):
                        experience_temp = int(row_list[1])
                        accumulate_experience_temp = int(row_list[2])
                    elif station_name.startswith(level_250):
                        accumulate_experience_250 = int(row_list[2])
                    elif station_name.startswith(level_275):
                        accumulate_experience_275 = int(row_list[2])

            temp = optlist[4]
            temp = temp.replace(",", "")
            now_experience = int(temp)
            now_level = int(now_level)

            data += 'Job : %s\n' % optlist[2]
            data += 'Level : %s\n' % optlist[3]
            if now_level < 275:
                data += 'Current Level : %s (%3.2f%%)\n\n' % (
                    format(now_experience, ','), now_experience / experience_temp * 100)
                if now_level < 250:
                    data += "EXP left until 250: %s\n" % format(
                        accumulate_experience_250 - accumulate_experience_temp - now_experience, ',')
                data += "EXP left until 275: %s\n" % format(
                    accumulate_experience_275 - accumulate_experience_temp - now_experience, ',')

            if not title:
                output = discord.Embed(title="Warning!!!", description='Cannot find the character in the ranking!', color=0xff0000)
                output.set_footer(text="IGNs are case-sensitive.")
            output = discord.Embed(title=title, description=data, color=0x0000ff)

    return output


def level_main(msg):
    if len(msg) is 2:
        empty_result = [[], [], [], [], [], [], []]

        main_url = 'https://maplestory.nexon.com/Ranking/World/Total?c=%s' % msg[1]
        reboot_url = 'https://maplestory.nexon.com/Ranking/World/Total?c=%s&w=254' % msg[1]
        main_result = level1(main_url)

        if main_result == empty_result:
            reboot_result = level1(reboot_url)
            if reboot_result == empty_result:
                output = discord.Embed(title="Warning!!!", description='Cannot find the character in the ranking!', color=0xff0000)
            else:
                output = level2(main_result, msg[1])
        else:
            output = level2(main_result, msg[1])
    else:
        output = discord.Embed(title="#level", description='You can use #level (ign) to figure out how much EXP you need to reach 250 and 275.\nThis uses official MapleStory site to grab information.', color=0x00ff00)
        output.set_footer(text="Ex. #level RIRINTO")

    return output
