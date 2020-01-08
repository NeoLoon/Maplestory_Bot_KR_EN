#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import discord
import requests
from bs4 import BeautifulSoup

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


def information_main(msg):
    if len(msg) is 2:
        url = 'https://maple.gg/u/%s' % msg[1]
        url = requests.get(url)
        html = url.content
        soup = BeautifulSoup(html, 'html.parser')
        finder = soup.select(".bg-light")
        if finder[0].select('h3')[0].text == '검색결과가 없습니다.':
            output = discord.Embed(title="Warning!!!", description='No result.', color=0xff0000)
            output.set_footer(text="Please check your character name, It's case-sensitive. Data is based on Maple.gg.")
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
