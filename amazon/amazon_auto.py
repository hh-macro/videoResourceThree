# -- coding: utf-8 --
# @Author: 胡H
# @File: amazon_auto.py
# @Created: 2025/4/12 13:38
# @LastModified: 
# Copyright (c) 2025 by 胡H, All Rights Reserved.
# @desc:

import random

import pandas as pd
from DrissionPage import ChromiumPage
import time

page = ChromiumPage()

page.get(
    'https://www.amazon.com/ap/signin?clientContext=135-2939824-8502515&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fus.amazon.com%2Fgp%2Fvideo%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_t%3D1sg7MOyO7HcO2AaUnWu_BV34hTajwE_IximIOoiJZIY541AAAAAQAAAABn-gjQcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ%26location%3D%2Fgp%2Fvideo%2Fsignup%3Fref_%253Ddvah&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&accountStatusPolicy=P1&openid.assoc_handle=usflex&openid.mode=checkid_setup&countryCode=US&language=en_US&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')
time.sleep(5)
try:

    page.ele('css:#ap_password').input('123aaa123')
    page.ele('css:#signInSubmit').click()
except:
    print('已登陆')
time.sleep(5)

page.get(
    'https://us.amazon.com/s?k=%E7%94%B5%E8%A7%86&i=movies-tv-intl-ship&rh=n%3A2625373011%2Cn%3A2649513011%2Cp_n_theme_browse-bin%3A30245692011&dc&language=zh&ds=v1%3AJvDoPffA9moOsmEYFV7JHvkQxdKXSpwAIubkKPYAU3M&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&qid=1744445122&rnid=2625373011&ref=sr_nr_n_3')
time.sleep(3)
page.refresh()
input('请回车:')
# 数据抓取逻辑（带重试机制）
data_content_list = []
retry_count = 3  # 最大重试次数
current_page = 1


def retry_click_next_page():
    """重试点击下一页按钮"""
    for _ in range(retry_count):
        try:
            # 等待页面加载完成
            time.sleep(random.uniform(1, 3))
            # 尝试点击下一页
            page.ele('css:.s-pagination-item.s-pagination-next').click()
            time.sleep(random.uniform(1, 3))
            print(f"成功跳转到第 {current_page} 页")
            return True
        except Exception as e:
            print(f"点击下一页失败，重试中... 错误: {e}")
            # 刷新页面后重试
            page.refresh()
            time.sleep(random.uniform(2, 4))
    return False


try:
    while current_page <= 336:  # 总页数
        print(f"正在抓取第 {current_page} 页...")

        # 抓取当前页数据
        try:
            section_pages = page.eles('css:.a-section.a-spacing-small.a-spacing-top-small')
            for section_page in section_pages:
                try:
                    section_name = section_page.ele(
                        'css:.a-size-medium.a-color-base.a-text-normal').text
                    full_url = section_page.ele(
                        'css:.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal').attr(
                        'href')
                    data_content_list.append({
                        'aria_label': section_name,
                        'href': full_url
                    })
                except Exception as e:
                    print(f"抓取单个元素失败: {e}")
        except Exception as e:
            print(f"抓取页面元素失败: {e}")
            break


        if not retry_click_next_page():
            print("无法继续翻页，退出抓取")
            break

        current_page += 1
except Exception as e:
    print(f"抓取过程中发生异常: {e}")

# 保存数据
finally:
    if data_content_list:
        df = pd.DataFrame(data_content_list)
        timestamp = int(time.time())
        excel_name = f"./compilations/amazonList-{timestamp}.xlsx"
        df.to_excel(excel_name, index=False)
        print(f"数据已保存到: {excel_name}")
    else:
        print("未抓取到任何数据")

"""

"""
