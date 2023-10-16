#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   crawler.py
@Time    :   2023/09/28 16:48:20
@Author  :   xxx 
@Version :   1.0
@Site    :   https://github.com/xxx
@Desc    :   None
'''

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

service = Service(executable_path='chromedriver-win64\chromedriver.exe')
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('-ignore -ssl-errors')
browser = webdriver.Chrome(service=service, options=options)

# 用户名和密码
username = '34720220156442'
password = '12080517@Mc'
changdi_url0 = "https://ids.xmu.edu.cn/authserver/login?type=userNameLogin&service=http%3A%2F%2Fcgyy.xmu.edu.cn%2Fidcallback"


browser.get(changdi_url0)

time.sleep(0.5)

print('开始登录')
browser.find_element(By.ID, 'username').send_keys(username)
browser.find_element(By.ID, 'password').send_keys(password)
browser.find_element(By.ID, 'login_submit').click()
print('登录成功')

cookie = browser.get_cookies()

# browser.quit()

# room_url = 'https://cgyy.xmu.edu.cn/room_reservations/10/5/1500/5'
# room_url = 'https://cgyy.xmu.edu.cn/node/add/room-reservations-reservation/10/7/1930/13'
room_url0 = 'https://cgyy.xmu.edu.cn/node/add/room-reservations-reservation/10/7/1930/'
room_list = ['05','06','07','08','10','11','12','13']

url0i = room_url0 + '13'
try:
    browser.get(url0i)

    s1=browser.find_element(By.TAG_NAME,'select')
    Select(s1).select_by_value("90")
    partnar = '23220220156475 白佳兴'
    tele = '13324209373'
    browser.find_element(By.ID, 'edit-field-members-und-0-value').send_keys(partnar)
    browser.find_element(By.ID, 'edit-field-telephone-und-0-value').send_keys(tele)
    browser.find_element(By.ID, 'edit-submit').click()
    time.sleep(600)
except:
    browser.quit()
    room_url01 = room_url0 + '12'
    browser.get(room_url01)
    s1=browser.find_element(By.TAG_NAME,'select')
    Select(s1).select_by_value("90")
    partnar = '23220220156475 白佳兴'
    tele = '13324209373'
    browser.find_element(By.ID, 'edit-field-members-und-0-value').send_keys(partnar)
    browser.find_element(By.ID, 'edit-field-telephone-und-0-value').send_keys(tele)
    browser.find_element(By.ID, 'edit-submit').click()
    time.sleep(600)
# time.sleep(600)










