#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
import csv
import requests
from bs4 import BeautifulSoup
from module.timeout import *

def achievement(msg, data, i):  # 업적
    output = "";
    temp = [[], [], [], []]
    result = [[], [], [], []]
    temp[0].append(data[i].select('div')[2].text.strip())  # 등급
    temp[1].append(data[i].select('span')[0].text.strip())  # 점수
    temp[2].append(data[i].select('span')[1].text.replace("\n", "").replace(" ", "").replace("/", " / ").strip())  # 레벨 / 직업
    temp[3].append(data[i].select('span')[4].text.strip())  # 기준일

    rank = temp[0]

    if "브론즈" in rank:
        rank = "bronze"
    elif "실버" in rank:
        rank = "silver"
    elif "골드" in rank:
        rank = "gold"
    elif "플래티넘" in rank:
        rank = "platinum"
    elif "다이아몬드" in rank:
        rank = "diamond"
    elif "마스터" in rank:
        rank = "master"

    for k in range(0, 4, 1):
        result[k] = temp[k][0]
    output = discord.Embed(title=msg[1],
                           description='%s\n%s\n%s\n%s' % (result[0], result[1], result[2], result[3]),
                           color=0x0000ff)
    output.set_thumbnail(url="http://ec2-52-79-205-251.ap-northeast-2.compute.amazonaws.com/image/achievement/%s.png" % rank)

    return output


def union(msg, data, i):  # 유니온
    temp = [[], [], [], []]
    result = [[], [], [], []]
    temp[0].append(data[i].select('div')[2].text.strip())  # 등급
    temp[1].append(data[i].select('span')[0].text.strip())  # 레벨
    temp[2].append(data[i].select('span')[1].text.lstrip('전투력 ').replace(",", "").strip())  # 전투력
    temp[3].append(data[i].select('span')[4].text.strip())  # 기준일

    num = int(temp[2][0]) * 0.000000864
    num = int(num)
    rank = temp[0][0]

    if "그랜드" in rank:
        rank1 = "grandmaster"
        rank2 = rank.lstrip('그랜드마스터 ')
    elif "마스터" in rank:
        rank1 = "master"
        rank2 = rank.lstrip('마스터 ')
    elif "베테랑" in rank:
        rank1 = "veteran"
        rank2 = rank.lstrip('베테랑 ')
    elif "노비스" in rank:
        rank1 = "novice"
        rank2 = rank.lstrip('노비스 ')

    for k in range(0, 4, 1):
        result[k] = temp[k][0]
    output = discord.Embed(title=msg[1],
                           description='%s\nRank : %s\nLegion Raid Power : %s\n%s\nTotal coin per day : %d' % (
                               result[1], result[0], format(int(result[2]),','), result[3], num),
                           color=0x0000ff)
    output.set_thumbnail(url="http://ec2-52-79-205-251.ap-northeast-2.compute.amazonaws.com/image/union/%s/%s.png" % (rank1, rank2))

    return output


def information(msg, data, i):  # 무릉, 더시드
    temp = [[], [], [], []]
    result = [[], [], [], []]
    temp[0].append(data[i].select('h1')[0].text.replace(" ", "").replace("\n", " "))  # 최고층
    temp[1].append(data[i].select('small')[0].text.strip())  # 시간
    temp[2].append(
        data[i].select('span')[1 - i].text.replace("\n", "").replace(" ", "").replace("/", " / ").strip())  # 레벨 / 직업
    temp[3].append(data[i].select('span')[4 - i].text.lstrip('기준일: ').strip())  # 날짜

    for k in range(0, 4, 1):
        result[k] = temp[k][0]
    output = discord.Embed(title=msg[1],
                           description='%s\nFloor : %s\nTime : %s\nDate : %s' % (result[2], result[0], result[1], result[3]),
                           color=0x0000ff)
    return output

def info(msg, reboot):
    file = "module/database/level/level.csv"
    data = 0.0
    if reboot == 0:
        url = 'https://maplestory.nexon.com/Ranking/World/Total?c=%s' % msg[1]
    else:
        url = 'https://maplestory.nexon.com/Ranking/World/Total?c=%s&w=254' % msg[1]
        print(msg[1])
    url = requests.get(url)
    html = url.content
    soup = BeautifulSoup(html, 'html.parser')
    try:
        finder = soup.find('tr', {'class':'search_com_chk'})
        inside = finder.find_all('td')
        allrank = int(inside[0].find('p').get_text()) # space doesn't get removed with rstrip()
        image = inside[1].find('span').find('img').get('src').replace('/180','')
        world = inside[1].find('dl').find('dt').find('a').find('img').get('src').split('world_icon/', 1)[1]

        worldlist = {'icon_2.png': 'Reboot 2', 'icon_3.png': 'Reboot', 'icon_4.png': 'Aurora',
                    'icon_5.png': 'Red', 'icon_6.png': 'Enosis', 'icon_7.png': 'Union',
                    'icon_8.png': 'Scania', 'icon_9.png': 'Luna', 'icon_10.png': 'Zenith',
                    'icon_11.png': 'Croa', 'icon_12.png': 'Bera', 'icon_13.png':'Elysium',
                    'icon_14.png': 'Arcane', 'icon_15.png': 'Nova', 'icon_16.png': 'Burning',
                    'icon_17.png': 'Burning 2'}

        for i in worldlist:
            if world in worldlist:
                world = worldlist[world]
                break
            else:
                world = "unknown"
                i = i + 1

        job = inside[1].find("dd").get_text().rsplit('/', 1)[1]
        level = inside[2].get_text()
        exp = inside[3].get_text()
        pop = inside[4].get_text()
        guild = inside[5].get_text()

        now_level = level
        now_level = now_level[3:]

        with open(file, newline='', encoding="utf-8") as database:
            freader = csv.reader(database)
            for row_list in freader:
                station_name = row_list[0]
                if station_name.startswith(now_level):
                    experience_temp = int(row_list[1])

            temp = exp
            temp = temp.replace(",", "")
            now_experience = int(temp)
            now_level = int(now_level)

            if now_level < 275:
                perc = now_experience / experience_temp * 100
                data = '(%3.2f%%)' % (perc)

        output = discord.Embed(title="KMS Profile lookup", description='Profile data for %s' % (msg[1]))
        output.add_field(name ="Name", value = '%s' % (msg[1]), inline = True)
        output.add_field(name ="Level", value = "%s" % (level), inline = True)
        if guild != "":
            output.add_field(name ="Guild", value = "%s" % (guild), inline = True)
        else:
            output.add_field(name ="Guild", value = "None", inline = True)
        if now_level > 235:
            output.add_field(name ="EXP", value = "%s%s" % (exp, data), inline = True)
        else:
            output.add_field(name ="EXP", value = "%s" % (exp), inline = True)
        output.add_field(name ="Overall Rank", value = "%s" % (allrank), inline = True)
        output.add_field(name ="Server", value = "%s" % (world), inline = True)
        output.add_field(name ="Class", value = "%s" % (job), inline = True)
        output.set_thumbnail(url=image)
        return output
    except Exception as e:
        print(e)
        if reboot == 0:
            return info(msg, 1)
        else:
            output = discord.Embed(title="Warning!!!", description='No result.', color=0xff0000)
            output.set_footer(text="Please check your character name, It's case-sensitive. Data is based on Offical KMS rank.")
            return output

def information_main(msg):
    if len(msg) is 2:
        if 'info' in msg[0]:
            output = info(msg, 0)
        else:
            url = 'https://maple.gg/u/%s' % msg[1]
            url = requests.get(url)
            html = url.content
            soup = BeautifulSoup(html, 'html.parser')
            finder = soup.select(".bg-light")
            if finder[0].select('h3')[0].text == '검색결과가 없습니다.':
                output = discord.Embed(title="Warning!!!", description='No result.', color=0xff0000)
                output.set_footer(text="Please check your character name, It's case-sensitive. Data is based on Maple.gg.")
            else:
                if 'info_gg' in msg[0]:
                    output = information1(msg)
                else:
                    data = soup.select("div.bg-light > section > div > div")
                    if 'dojo' in msg[0]:
                        if data[0].select('div')[2].text == '기록이 없습니다.':
                            output = discord.Embed(title="Warning!!!", description='Cannot find the result.', color=0xff0000)
                        else:
                            output = information(msg, data, 0)
                    elif 'oz' in msg[0]:
                        if data[1].select('div')[2].text == '기록이 없습니다.':
                            output = discord.Embed(title="Warning!!!", description='Cannot find the result.', color=0xff0000)
                        else:
                            output = information(msg, data, 1)
                    elif 'union' in msg[0]:
                        if data[2].select('div')[2].text == '기록이 없습니다.':
                            output = discord.Embed(title="Warning!!!", description='Cannot find the result.', color=0xff0000)
                        else:
                            output = union(msg, data, 2)
                    elif 'achievement' in msg[0]:
                        if data[3].select('div')[2].text == '기록이 없습니다.':
                            output = discord.Embed(title="Warning!!!", description='Cannot find the result.', color=0xff0000)
                        else:
                            output = achievement(msg, data, 3)
    else:
        output = discord.Embed(title="#dojo", description='You can use #dojo (ign) to find out your dojo floor.\nFor other information please use #oz, #union or #achievement.', color=0x00ff00)
        output.set_footer(text="Ex. #dojo RIRINT")

    return output
