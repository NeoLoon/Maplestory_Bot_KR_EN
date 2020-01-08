#!/usr/bin/env python3

import discord
import csv
import random


def gambling2(times, title, target):
    file = "module/database/gambling/%s.csv" % target
    maxnumber = float(0)
    with open(file, newline='', encoding='UTF-8') as database:  # 확률 총합 확인
        freader = csv.reader(database)
        next(freader)
        for row_list in freader:
            if maxnumber < float(row_list[3]):
                maxnumber = float(row_list[3])
    resultlist = []
    for i in range(0, times):  # 결과 누적
        randomnumber = random.randrange(0, int(maxnumber*10000000))
        file = "module/database/gambling/%s.csv" % target
        with open(file, newline='', encoding='UTF-8') as database:
            freader = csv.reader(database)
            next(freader)
            for row_list in freader:
                if float(row_list[2]) <= randomnumber/10000000 < float(row_list[3]):
                    resultlist.append(row_list[0])
    result = ""
    with open(file, newline='', encoding='UTF-8') as database:  # 정렬
        freader = csv.reader(database)
        next(freader)
        for row_list in freader:
            for i in range(0, len(resultlist)):
                if resultlist[i] in row_list[0]:
                    if resultlist[i] not in result:
                        result += "%s : %d\n" % (resultlist[i], resultlist.count(resultlist[i]))
    output = discord.Embed(title="%s %d회 결과" % (title, times), description='%s' % result, color=0x0000ff)
    return output


def gambling1(display_name, title, target):
    file = "module/database/gambling/%s.csv" % target
    maxnumber = float(0)
    with open(file, newline='', encoding='UTF-8') as database:  # 확률 총합 확인
        freader = csv.reader(database)
        next(freader)
        for row_list in freader:
            if maxnumber < float(row_list[3]):
                maxnumber = float(row_list[3])
    randomnumber = random.randrange(0, int(maxnumber*10000000))
    file = "module/database/gambling/%s.csv" % target
    with open(file, newline='', encoding='UTF-8') as database:  # 랜덤 결과 확인
        freader = csv.reader(database)
        next(freader)
        for row_list in freader:
            if float(row_list[2]) <= randomnumber/10000000 < float(row_list[3]):
                getitem = row_list[0]
    if "hair" in title:
        output = discord.Embed(title="로얄 헤어 쿠폰", description='%s님의 헤어가 %s 로 변경되었습니다.' % (display_name, getitem),
                               color=0x0000ff)
    elif "face" in title:
        output = discord.Embed(title="로얄 성형 쿠폰", description='%s님의 얼굴이 %s 로 변경되었습니다.' % (display_name, getitem),
                               color=0x0000ff)
    else:
        output = discord.Embed(title="%s" % title, description='%s님이 %s 을(를) 획득하였습니다.' % (display_name, getitem),
                               color=0x0000ff)
    return output


def gambling_main(msg, display_name):
    if len(msg) is 1:
        if 'gold' in msg[0] or 'apple' in msg[0]:
            output = gambling1(display_name, "GoldApple", "GoldApple")
        elif 'royal' in msg[0]:
            output = gambling1(display_name, "RoyalStyle", "RoyalStyle")
        elif 'wonder' in msg[0]:
            output = gambling1(display_name, "WispsWonderBerry", "WispsWonderBerry")
        elif 'luna' in msg[0]:
            output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
            output.set_footer(text="Ex. #luna sweet/dream")
        elif 'male' in msg[0] or 'female' in msg[0]:
            output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
            output.set_footer(text="Ex. #male/female hair/face")
    elif len(msg) is 2:
        if 'luna' in msg[0]:
            if 'sweet' in msg[1]:
                output = gambling1(display_name, "루나 크리스탈 스윗", "LunaCrystalSweet")
            elif 'dream' in msg[1]:
                output = gambling1(display_name, "루나 크리스탈 드림", "LunaCrystalDream")
            else:
                output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
                output.set_footer(text="Ex. #luna sweet/dream")
        elif 'male' in msg[0]:
            if 'hair' in msg[1]:
                output = gambling1(display_name, "헤어", "RoyalHairCouponMan")
            elif 'face' in msg[1]:
                output = gambling1(display_name, "성형", "RoyalPlasticSurgeryCouponMan")
            else:
                output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
                output.set_footer(text="Ex. #male hair/face")
        elif 'female' in msg[0]:
            if 'hair' in msg[1]:
                output = gambling1(display_name, "헤어", "RoyalHairCouponWoman")
            elif 'face' in msg[1]:
                output = gambling1(display_name, "성형", "RoyalPlasticSurgeryCouponWoman")
            else:
                output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
                output.set_footer(text="Ex. #female hair/face")
        else:
            if msg[1].isdecimal():
                times = int(float(msg[1]))
                if 'royal' in msg[0] and msg[1].isdecimal():
                    if 0 < times <= 1000:
                        output = gambling2(times, "RoyalStyle", "RoyalStyle")
                    else:
                        output = discord.Embed(title="Warning!!!", description='1 ~ 1000 의 횟수를 지정해주세요.', color=0xff0000)
                elif ('wonder' in msg[0] and msg[1].isdecimal()):
                    if 0 < times <= 1000:
                        output = gambling2(times, "WispsWonderBerry", "WispsWonderBerry")
                    else:
                        output = discord.Embed(title="Warning!!!", description='1 ~ 1000 의 횟수를 지정해주세요.', color=0xff0000)
                elif ('gold' in msg[0] or 'apple' in msg[0]) and msg[1].isdecimal():
                    if 0 < times <= 100:
                        output = gambling2(times, "GoldApple", "GoldApple")
                    else:
                        output = discord.Embed(title="Warning!!!", description='1 ~ 100 의 횟수를 지정해주세요.', color=0xff0000)
            else:
                output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
                output.set_footer(
                    text="#gold (int), 골드애플과 로얄스타일, 원더베리를 시뮬레이션 할 수 있으며, 횟수 옵션이 없으면 1회 시행합니다. #루나 스윗/드림은 횟수를 지정할 수 없습니다.")
    else:
        output = discord.Embed(title="Warning!!!", description='올바른 옵션을 입력하세요.', color=0xff0000)
        output.set_footer(
            text="#gold (int), 골드애플과 로얄스타일, 원더베리를 시뮬레이션 할 수 있으며, 횟수 옵션이 없으면 1회 시행합니다. #루나 스윗/드림, #남자/여자 헤어/성형 은 횟수를 지정할 수 없습니다.")

    return output
