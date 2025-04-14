# -- coding: utf-8 --
# @Author: 胡H
# @File: 草稿二.py
# @Created: 2025/4/12 16:33
# @LastModified: 
# Copyright (c) 2025 by 胡H, All Rights Reserved.
# @desc:
# 读取Excel文件
import pandas as pd
import random

from DrissionPage import ChromiumPage
import time

page = ChromiumPage()
df = pd.read_excel('compilations/amazon_动漫电影.xlsx')
# 将数据转换为字典列表
data_list = df.to_dict(orient='records')
ji_list = []
print(data_list)
for data_li in data_list:
    href = data_li['href']
    page.get(href)
    ji = page.ele('css:[data-automation-id="runtime-badge"]').text
    print(ji)
    ji_list.append(ji)
    time.sleep(1)
print(ji_list)

"""

amazon_动画电视.xlsx 21  268集 6700
amazon_动漫电视.xlsx 40  828集 20700
amazon_动漫电影.xlsx 555 555集 49395


hboMax_动画剧集.xlsx  23  1057集   25368
hboMax_动画电影.xlsx  50  50集     5000
"""