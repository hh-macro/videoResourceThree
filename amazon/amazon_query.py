# -- coding: utf-8 --
# @Author: 胡H
# @File: amazon_query.py
# @Created: 2025/4/12 14:03
# @LastModified: 
# Copyright (c) 2025 by 胡H, All Rights Reserved.
# @desc:
import re

import requests

cookies = {
    'session-id': '130-4385434-5066934',
    'ubid-main': '135-1025297-2749812',
    'av-timezone': 'Asia/Shanghai',
    'i18n-prefs': 'USD',
    'sst-main': 'Sst1|PQFhZzrtrRSmBDE3nE_r6BYpDF1l5pzJzUhJm1Kv6URZb2rlMne1eKfNbn5zB_DVpyyB1MnOF7Eu0Mkn7PSXPEYc-85WBknp6-MDRog2I6Ohv4xX79DEItG8jhLTbhT7sHYtqXhuwLePgsmj7byuxo3DIPmUJ5BtwmbZx0tZpU58-1ArWnPaBIIGidnEquqNY3u4RM1Q-mTDOv48HgRMwBB5_lSmQ8NI6rZOvZt8VZb0cRHJYZDyH5cW5VXBWImo0cQwQ5ujMz4wmrjrJhmCLYyVqiyyY_tUaJdtXE5Xee9Q6Y00SwZQGjjAG0GE8DX9HlJkrXyjRYBZ3tXH5LHRje0xvFW9NPLi3KKMaFRbPfCGUAk',
    'session-id-time': '2082787201l',
    'sp-cdn': '"L5Z9:NL"',
    'sess-at-main': 'KGM7i6dGzUyHYuerJNwnrkhPCVE+H7DDLezZAov74js=',
    'at-main': 'Atza|IwEBIE6tiX9dqLwocC3eqWD408f4tVR2hzVBpOeHY4HuleQ3XM3wULNsaJxGobnt3atFVtLNW_pRnyEmLPYR1ELOncqFRN5Ff8hkHksughbuLxvbxvCAd8MbQnttVzyQ6VCslONepXI_GqlIdSfYGswzbwkVP7ltmZDzP1I5erWuOj4ANJ-SDV8IpPbxFufvCq4yKNyrKvTanNoqOT7nMTMYwqjjd0h-zk59IzpTHnMSOFKfkBCkOk7Tnl1KCCq-_QcoMd0pUB4jfy-r_PJkfadLKGn2Fnh8mX0BBgCm9YHE3WFJOQSStmj8fpCaH2AdjUz045A8OEiIWgE3anGy5MIFn7eE',
    'av-profile': 'cGlkPWFtem4xLmFjdG9yLnBlcnNvbi5vaWQuQTVLQ09VSjNUSUQ4MyZ0aW1lc3RhbXA9MTc0NDQzNzQyMTQ2MiZ2ZXJzaW9uPXYx.g2sn75klkIabG0TBt9ftXiYDBv3tsewiyNziDOz9hPStAAAAAQAAAABn-gCtcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ',
    'lc-main': 'zh_CN',
    'session-token': '"+pki0Yn2FdK2lk35wTkbHIs37nDnZGmw0HpP65/3ryTNoEfXHjPtqjsJRojIiKKMEMiJd3pvxd3fZEd+fNLvAwSPhTOdVnXUzgLOORR0mR6HPTt5ubhKmp6sLZqm0o3BJVUVWqRH7nHQVDPqNVpRm/LY7P/18bJ1QG8CWPIBvy35BTapROOvSc3CGe+DCeBJ3LF729j+rmiXad+zngqs776WlwMc99E5FzivVTtPzBJOood2rdvymxrMC3l4FCmbnxzscs7i0OREOoumUnhcPAVaYPFTq6X1ZI/Nnig0ruwwiYbS/jpcbMyABmA31q8byRRUwwFRsr8sGFTrWiDv6u9MT78HSfURLD1L/QMU/3z/q1IVDy/dqZ6oJz6Dd9mJHBXbarqzMY/8eqyOXnwhwzJwg5sqV0mzTuDc6Ic72aZGxoS90eDZNg=="',
    'x-main': '"Tx42ckDSbXW2M7e7ipa0ipuMyFaHBeEipXDOVTW50radblwBw1y1x1qIb0?KTflU"',
    'csm-hit': 'tb:ETDY6R1C03BNPWA3YY2C+sa-QB5W06BE94R0E5RMJ5AS-JN7YKBGA0Q4ZRDV9RAF4|1744437738191&t:1744437738191&adb:adblk_no',
}

headers = {
    'accept': 'text/html,image/webp,*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/json',
    'device-memory': '8',
    'downlink': '10',
    'dpr': '1.25',
    'ect': '4g',
    'origin': 'https://us.amazon.com',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://us.amazon.com/-/zh/s?k=%E7%94%B5%E5%BD%B1&i=movies-tv&rh=n%3A2625373011%2Cp_n_theme_browse-bin%3A30245692011&dc=&page=3&language=zh&__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=1M0I5GT3NA1QK&qid=1744437675&rnid=2650362011&sprefix=dia%2Cinstant-video%2C721&xpid=sMIyM_t9umILJ',
    'rtt': '300',
    'sec-ch-device-memory': '8',
    'sec-ch-dpr': '1.25',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"19.0.0"',
    'sec-ch-viewport-width': '1536',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    'viewport-width': '1536',
    'x-amazon-rush-fingerprints': 'AmazonRushAssetLoader:1202F8AA9B9E3A62A246BF3FA42812770110C222|AmazonRushFramework:9F05006E3CFD098B85DF9F821E78C67A14F2BEB7|AmazonRushRouter:9F42D6FB9D4ADCF73074D70FD0BCDD689982ADFB',
    'x-amazon-s-fallback-url': '',
    'x-amazon-s-mismatch-behavior': 'ABANDON',
    'x-amazon-s-swrs-version': '7C97F228F318C199A34841900461394B,D41D8CD98F00B204E9800998ECF8427E',
    'x-requested-with': 'XMLHttpRequest',
    # 'cookie': 'session-id=130-4385434-5066934; ubid-main=135-1025297-2749812; av-timezone=Asia/Shanghai; i18n-prefs=USD; sst-main=Sst1|PQFhZzrtrRSmBDE3nE_r6BYpDF1l5pzJzUhJm1Kv6URZb2rlMne1eKfNbn5zB_DVpyyB1MnOF7Eu0Mkn7PSXPEYc-85WBknp6-MDRog2I6Ohv4xX79DEItG8jhLTbhT7sHYtqXhuwLePgsmj7byuxo3DIPmUJ5BtwmbZx0tZpU58-1ArWnPaBIIGidnEquqNY3u4RM1Q-mTDOv48HgRMwBB5_lSmQ8NI6rZOvZt8VZb0cRHJYZDyH5cW5VXBWImo0cQwQ5ujMz4wmrjrJhmCLYyVqiyyY_tUaJdtXE5Xee9Q6Y00SwZQGjjAG0GE8DX9HlJkrXyjRYBZ3tXH5LHRje0xvFW9NPLi3KKMaFRbPfCGUAk; session-id-time=2082787201l; sp-cdn="L5Z9:NL"; sess-at-main=KGM7i6dGzUyHYuerJNwnrkhPCVE+H7DDLezZAov74js=; at-main=Atza|IwEBIE6tiX9dqLwocC3eqWD408f4tVR2hzVBpOeHY4HuleQ3XM3wULNsaJxGobnt3atFVtLNW_pRnyEmLPYR1ELOncqFRN5Ff8hkHksughbuLxvbxvCAd8MbQnttVzyQ6VCslONepXI_GqlIdSfYGswzbwkVP7ltmZDzP1I5erWuOj4ANJ-SDV8IpPbxFufvCq4yKNyrKvTanNoqOT7nMTMYwqjjd0h-zk59IzpTHnMSOFKfkBCkOk7Tnl1KCCq-_QcoMd0pUB4jfy-r_PJkfadLKGn2Fnh8mX0BBgCm9YHE3WFJOQSStmj8fpCaH2AdjUz045A8OEiIWgE3anGy5MIFn7eE; av-profile=cGlkPWFtem4xLmFjdG9yLnBlcnNvbi5vaWQuQTVLQ09VSjNUSUQ4MyZ0aW1lc3RhbXA9MTc0NDQzNzQyMTQ2MiZ2ZXJzaW9uPXYx.g2sn75klkIabG0TBt9ftXiYDBv3tsewiyNziDOz9hPStAAAAAQAAAABn-gCtcmF3AAAAAPgWC9WfHH8iB-olH_E9xQ; lc-main=zh_CN; session-token="+pki0Yn2FdK2lk35wTkbHIs37nDnZGmw0HpP65/3ryTNoEfXHjPtqjsJRojIiKKMEMiJd3pvxd3fZEd+fNLvAwSPhTOdVnXUzgLOORR0mR6HPTt5ubhKmp6sLZqm0o3BJVUVWqRH7nHQVDPqNVpRm/LY7P/18bJ1QG8CWPIBvy35BTapROOvSc3CGe+DCeBJ3LF729j+rmiXad+zngqs776WlwMc99E5FzivVTtPzBJOood2rdvymxrMC3l4FCmbnxzscs7i0OREOoumUnhcPAVaYPFTq6X1ZI/Nnig0ruwwiYbS/jpcbMyABmA31q8byRRUwwFRsr8sGFTrWiDv6u9MT78HSfURLD1L/QMU/3z/q1IVDy/dqZ6oJz6Dd9mJHBXbarqzMY/8eqyOXnwhwzJwg5sqV0mzTuDc6Ic72aZGxoS90eDZNg=="; x-main="Tx42ckDSbXW2M7e7ipa0ipuMyFaHBeEipXDOVTW50radblwBw1y1x1qIb0?KTflU"; csm-hit=tb:ETDY6R1C03BNPWA3YY2C+sa-QB5W06BE94R0E5RMJ5AS-JN7YKBGA0Q4ZRDV9RAF4|1744437738191&t:1744437738191&adb:adblk_no',
}

json_data = {
    'page-content-type': 'atf',
    'prefetch-type': 'rq',
    'customer-action': 'pagination',
}

response = requests.post(
    'https://us.amazon.com/s/query?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&crid=1M0I5GT3NA1QK&dc&i=movies-tv&k=%E7%94%B5%E5%BD%B1&language=zh&page=1&qid=1744437694&ref=sr_pg_3&rh=n%3A2625373011%2Cp_n_theme_browse-bin%3A30245692011&rnid=2650362011&sprefix=dia%2Cinstant-video%2C721&xpid=sMIyM_t9umILJ',
    cookies=cookies,
    headers=headers,
    json=json_data,
)

list_pattern = r'\[.*?\]'
lists = re.findall(list_pattern, response.text, re.DOTALL)
filtered_lists = []
for lst in lists:
    if 'data-main-slot:search-result' in lst:
        filtered_lists.append(lst)

# 打印筛选后的列表
for i, lst in enumerate(filtered_lists):
    print(f"Filtered List {i+1}: {lst}")