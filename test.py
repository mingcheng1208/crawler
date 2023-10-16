#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2023/09/30 20:03:13
@Author  :   xxx 
@Version :   1.0
@Site    :   https://github.com/xxx
@Desc    :   None
'''
# import random
# time_all = ['0930', '1000', '1200', '1230', '1430', '1500', '1530', '1600']
# time_p = []
# for i in range(len(time_all)):
#     if i+2 <= len(time_all):
#         time_p.append(time_all[i:i+3])
#     else:
#         pass
# # 提取3个时间段全部空缺
# timealbe = [i for i in time_p if len(i)==3 and i[0][-2:]==i[-1][-2:] and int(i[0][1])+1==int(i[-1][1])]

# a = random.choice(timealbe)
# print(a)

# 引入函数库
import datetime as dt
# 获取当前时间
now_time = dt.datetime.now()+ dt.timedelta(days=7)
now_time =now_time.strftime('%m/'+"%d")
a = [str(int(x)) for x in now_time.split('/')]
b = '/'.join(a)
# 格式化输出年份的后两位+月份2位+日期2位数字
print(b)

