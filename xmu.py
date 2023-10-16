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
import requests
import sys
import time
import json
from requests_oauthlib import OAuth1


changdi_url = "https://cgyy.xmu.edu.cn/"
changdi_url0 = "https://ids.xmu.edu.cn/authserver/login?type=userNameLogin&service=http%3A%2F%2Fcgyy.xmu.edu.cn%2Fidcallback"

cookies = {
    'route':'b80189b417779b45643a0490774fd142', 
    'JSESSIONID':'738A810E25EDF113B790B97971E6A76C', 
    'org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE':'zh_CN',
    '_ga':'GA1.1.2116277080.1681721499', 
    '_ga_K5ZS1FQ11K':'GS1.1.1682321408.7.0.1682321408.0.0.0', 
    'UM_distinctid':'18a8463ee4dc4b-0e6d6c2ed4cf31-57b1a33-1fa400-18a8463ee4e191c'
 }
headers = {
        # "Content-Type" : 'text/html; charset=utf-8',
        # 'cookie':cookies,
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
}

# 登录系统，获取cookies
def login(user_name, user_pwd):
    url = changdi_url0
    login_params = {
        '_eventId': 'submit',
        'cllt': 'userNameLogin',
        'dllt': 'generalLogin',
        "username":user_name,
        "passwordText":user_pwd
    }
    param = {
        'type': 'userNameLogin',
        'service': 'http://cgyy.xmu.edu.cn/idcallback',
    }

    # 创建Session对象
    session = requests.Session()
    result = session.post(url=url, data=login_params,headers=headers,)

    # print('提交登录：',result.text)
    print(f"statusCode = {result.status_code}")
    # print(f"text = {result.text}")
    if result.status_code == 200:
        br = session.get(changdi_url)
        with open('casho_t.html', "wb") as f:
            f.write(br.content)
    print(result.cookies.items())

    return ""


if __name__ == '__main__':
    # 用户名和密码
    username = '34720220156442'
    password = '1208@Mc'
    login(username,password)
