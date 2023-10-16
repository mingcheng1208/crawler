#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   xmu_book.py
@Time    :   2023/10/06 20:08:42
@Author  :   xxx 
@Version :   1.0
@Site    :   https://github.com/xxx
@Desc    :   None
'''
import time
import random
import requests
import datetime as dt
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class GYM():
    def __init__(self,name,passwd,sign_url):
        self.username, self.password = name, passwd
        self.sign_url = sign_url
        self.browser = None
        self.cookie = None
        self.open_signin()
        self.req_get()
        # 获取当前时间
        # now_time = dt.datetime.now()+ dt.timedelta(days=6)
        # self.now_time =now_time.strftime('%m/'+"%d")
        # self.time_day = '/'.join([str(int(x)) for x in self.now_time.split('/')])

    def open_signin(self,):
        # 获取当前时间
        now_time = dt.datetime.now()+ dt.timedelta(days=6)
        self.now_time =now_time.strftime('%m/'+"%d")
        self.time_day = '/'.join([str(int(x)) for x in self.now_time.split('/')])
        # 打开浏览器
        # service = Service(executable_path='chromedriver-win64\chromedriver.exe')     
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors-spki-list')
        self.options.add_argument('-ignore -ssl-errors')
        # browser = webdriver.Chrome(service=service,options=options)
        self.browser = webdriver.Chrome(options=self.options)            #    打开浏览器
        # 打开登录截面，开始登录
        self.browser.get(self.sign_url)
        print('开始登录')
        self.browser.find_element(By.ID, 'username').send_keys(self.username)
        self.browser.find_element(By.ID, 'password').send_keys(self.password)
        self.browser.find_element(By.ID, 'login_submit').click()
        print('登录成功')
        # 获取cookie信息
        self.cookie = self.browser.get_cookies()
        time.sleep(0.5)
        # partner_name = '23220220156475 白佳兴'
        # tele = '13324209373'
        # self.req_get()
        # self.get_reservable_rooms()
        # self.choose_time(time_start='1200',time_delay = 30)
        # self.get_reservable_url()
        # self.gym_book(partner_name,tele,time_delay=30)


        return 0
    
    def req_get(self,):

        url_room_all = 'https://cgyy.xmu.edu.cn/room_reservations/'+ self.now_time
        # cookies做拼接
        cookies_list = [item["name"] + "=" + item["value"] for item in self.cookie]
        cookies = ';'.join(it for it in cookies_list)
        headers = {
            'Content-Type':'application/json;charset=UTF-8',
            'Cookie':f'{cookies}',
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
        }

        # 创建Session对象
        session = requests.Session()
        result = session.post(url=url_room_all, headers=headers)
        print(f"statusCode = {result.status_code}")
        if result.status_code == 200:
            with open('casho_result.html', "wb") as f:
                f.write(result.content)
        self.html_read = result.content
        return self.html_read

    def get_reservable_rooms(self,):
        # html = 'casho_result.html'
        # with open(html, "rb") as f:
        #     html_read = f.read()
        html_read = self.html_read
        soup = BeautifulSoup(html_read,"lxml")
        able_dir_time = []
        for a in soup.find_all('div',attrs={'id':"1"}):
            for c in a.find_all('div',attrs={'class':"grid-column hours-column"}):
                for d in c.find_all('li',class_=['even reservable','odd reservable']):
                    able_dir_time.append(d.find('a').get('href'))
        dir_name = [x.split('/')[-1] for x in able_dir_time]
        time_value =  [x.split('/')[-2] for x in able_dir_time]

        ini_dir = dir_name[0]
        self.time_dict ={}
        coach = []
        for i in range(len(dir_name)):
            if dir_name[i] != ini_dir:
                self.time_dict[ini_dir] = coach
                ini_dir = dir_name[i]
                coach = []
                coach.append(time_value[i])
            else:
                coach.append(time_value[i])
        self.time_dict[ini_dir] = coach
        print("reservable_rooms:",self.time_dict)
        return self.time_dict
    
    def choose_time(self,time_start='1400',time_delay = 90):
        time_l = int(time_delay/30)
        self.able_dict = {}
        for key,value in self.time_dict.items():
            time_all = value
            time_p = []
            match time_l:
                case 3:
                    for i in range(len(time_all)):
                        if i+2 <= len(time_all):
                            time_p.append(time_all[i:i+3])
                        else:
                            pass
                    # 提取连续时间段
                    timealbe = [i for i in time_p if len(i)==3 and i[0][-2:]==i[-1][-2:] and abs(int(i[0])-int(i[2]))==100 and int(i[0]) >=int(time_start)]
                    if timealbe:
                        self.able_dict[key] = random.choice(timealbe)
                    else:
                        continue
                case 2:
                    for i in range(len(time_all)):
                        if i+1 <= len(time_all):
                            time_p.append(time_all[i:i+time_l])
                        else:
                            pass
                    # 提取连续时间段
                    timealbe = [i for i in time_p if len(i)==2 and i[0][-2:]!=i[-1][-2:] and abs(int(i[0])-int(i[1])) in [30,70] and int(i[0]) >=int(time_start)]
                    if timealbe:
                        self.able_dict[key] = random.choice(timealbe)
                    else:
                        continue
                case  1:
                    time_p = [[i] for i in time_all if i]
                    timealbe = [i for i in time_p if int(i[0]) >=int(time_start)]
                    if timealbe:
                        self.able_dict[key] = random.choice(timealbe)
                    else:
                        continue
        print("choose time:",self.able_dict)
        return self.able_dict

    def get_reservable_url(self,m_day=None,room=None):
        url0 = 'https://cgyy.xmu.edu.cn/node/add/room-reservations-reservation/'
        if m_day is None:
            mday = self.time_day
        else:
            mday = m_day
        if room is None:
            roomlist = list(self.able_dict.keys())
            if '9' in roomlist:
                roomlist.remove('9')
            if '14' in roomlist:
                roomlist.remove('14')
            room01 = random.choice(roomlist)
            room02 = random.choice(roomlist)
        else:
            room = str(room + 4)
        self.url = url0 + mday + '/' + self.able_dict[room01][0] + '/' + room01
        self.url_stb = url0 + mday + '/' + self.able_dict[room02][0] + '/' + room02
        print(self.url)
        return self.url

    def gym_book(self,partner_name,tele,time_delay=90):

        url0i = self.url
        print(self.url)
        try:
            self.browser.get(url0i)

            s1=self.browser.find_element(By.TAG_NAME,'select')
            Select(s1).select_by_value(str(time_delay))
            partnar = partner_name
            tele = tele
            self.browser.find_element(By.ID, 'edit-field-members-und-0-value').send_keys(partnar)
            self.browser.find_element(By.ID, 'edit-field-telephone-und-0-value').send_keys(tele)
            self.browser.find_element(By.ID, 'edit-submit').click()
            time.sleep(300)
        except:
            self.browser.quit()
            room_url01 = self.url_stb
            self.browser.get(room_url01)
            s1=self.browser.find_element(By.TAG_NAME,'select')
            Select(s1).select_by_value(str(time_delay))
            partnar = partner_name
            tele = tele
            self.browser.find_element(By.ID, 'edit-field-members-und-0-value').send_keys(partnar)
            self.browser.find_element(By.ID, 'edit-field-telephone-und-0-value').send_keys(tele)
            self.browser.find_element(By.ID, 'edit-submit').click()
            time.sleep(300)

        return 0
    

if __name__ == '__main__':
    # 用户名和密码
    username = '34720220156442'
    password = '12080517@Mc'
    # login(username,password)
    sign_url = "https://ids.xmu.edu.cn/authserver/login?type=userNameLogin&service=http%3A%2F%2Fcgyy.xmu.edu.cn%2Fidcallback"

    partner_name = '23220220156475 白佳兴'
    tele = '13324209373'
    time_delay = 90
    time_start='1430'

    gym = GYM(username,password,sign_url)
    gym.get_reservable_rooms()
    gym.choose_time(time_start=time_start,time_delay=time_delay)
    gym.get_reservable_url()
    gym.gym_book(partner_name,tele,time_delay=time_delay)




