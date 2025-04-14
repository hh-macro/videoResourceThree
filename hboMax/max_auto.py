# -- coding: utf-8 --
# @Author: 胡H
# @File: max_auto.py
# @Created: 2025/4/12 18:03
# @LastModified: 
# Copyright (c) 2025 by 胡H, All Rights Reserved.
# @desc:
import random

import pandas as pd
from DrissionPage import ChromiumPage
import time

page = ChromiumPage()

page.get('https://play.max.com/series?tab=series-page-tab-apac-adult-animation')
input(':')
animation_grid = page.ele('css:[data-testid="series-page-rail-apac-adult-animation-a-z_grid"]')
StyledTileWrapper = animation_grid.ele('css:.StyledTileWrapper-Fuse-Web-Play__sc-1ramr47-31.nsONH.StyledTile-Fuse-Web-Play__sc-29yzoe-3.kARcCj')
kXgdems = StyledTileWrapper.eles('css:.StyledTileLinkNormal-Fuse-Web-Play__sc-1ramr47-33.kXgdem')
data_content_list = []
for kXgdem in kXgdems:
    full_url = kXgdem.attr('href')
    aria_label = kXgdem.attr('aria-label')
    index = aria_label.find("。第")
    if index != -1:
        aria_label = aria_label[:index]
    else:
        aria_label = aria_label

    video_info = {
        'aria_label': aria_label,
        'href': full_url
    }
    data_content_list.append(video_info)  # 将当前视频信息添加到行数据中

print('data_content_list:\t', data_content_list)
df = pd.DataFrame(data_content_list)

df.to_excel(f"./compilations/hboMaxList-{int(time.time())}.xlsx", index=False)

print(f"hboMaxList-{int(time.time())}.xlsx")
