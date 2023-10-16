#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   crt.py
@Time    :   2023/09/29 19:53:22
@Author  :   xxx 
@Version :   1.0
@Site    :   https://github.com/xxx
@Desc    :   None
'''

import random
import datetime as dt
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

html = 'casho_t.html'
with open(html, "rb") as f:
    html_read = f.read()

soup = BeautifulSoup(html_read,"lxml")
# print(soup.prettify())
badminton = soup.find_all('div',attrs={'id':"1"})

badminton_session = []
badminton_time_dir = []
able_dir_time = []
for a in soup.find_all('div',attrs={'id':"1"}):
    # for b in a.find_all('div',attrs={'class':"grid-column hours-column"}):
    #     badminton_session.append(b.find('li').text)
    for c in a.find_all('div',attrs={'class':"grid-column hours-column"}):
        for d in c.find_all('li',class_=['even reservable','odd reservable'])[1:-1]:
            able_dir_time.append(d.find('a').get('href'))

# def fun_able_dir(abdt):

dir_str = '/node/add/room-reservations-reservation/10/5/'

dir_name = [x.split('/')[-1] for x in able_dir_time]
time_value =  [x.split('/')[-2] for x in able_dir_time]

ini_dir = dir_name[0]
dir_time_dict ={}
coach = []
for i in range(len(dir_name)):
    if dir_name[i] != ini_dir:
        dir_time_dict[ini_dir] = coach
        ini_dir = dir_name[i]
        coach = []
        coach.append(time_value[i])
    else:
        coach.append(time_value[i])
dir_time_dict[ini_dir] = coach

# dir_time_dict.pop(9, None)
# dir_time_dict.pop(14, None)
def choose_time(time_dict,time_start='1400'):
    able_dict = {}
    for key,value in time_dict.items():
        time_all = value
        time_p = []
        for i in range(len(time_all)):
            if i+2 <= len(time_all):
                time_p.append(time_all[i:i+3])
            else:
                pass
        # 提取3个时间段全部空缺
        timealbe = [i for i in time_p if len(i)==3 and i[0][-2:]==i[-1][-2:] and int(i[0][1])+1==int(i[-1][1]) and int(i[0]) >=int(time_start)]
        if timealbe:
            able_dict[key] = random.choice(timealbe)
        else:
            continue
    return able_dict

a = choose_time(dir_time_dict,time_start='1400')
print(a)


# 获取当前时间
now_time = dt.datetime.now()+ dt.timedelta(days=7)
now_time =now_time.strftime('%m/'+"%d")
time_day = '/'.join([str(int(x)) for x in now_time.split('/')])

url_room_all = 'https://cgyy.xmu.edu.cn/room_reservations/'+ now_time

def get_url(hour_room_dict,m_day=None,room=None):
    url0 = 'https://cgyy.xmu.edu.cn/node/add/room-reservations-reservation/'
    if m_day is None:
        mday = time_day
    else:
        mday = m_day
    if room is None:
        room = random.choice(list(hour_room_dict.keys()))
    else:
        room = str(room + 4)
    url = url0 + mday + '/' + hour_room_dict[room][0] + '/' + room
    return url
# time_day = '10/7'
b = get_url(a,time_day,10)
print(b)









