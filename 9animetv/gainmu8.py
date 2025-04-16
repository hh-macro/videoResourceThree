# -- coding: utf-8 --
# @Author: 胡H
# @File: gainmu8.py
# @Created: 2025/4/16 11:15
# @LastModified: 
# Copyright (c) 2025 by 胡H, All Rights Reserved.
# @desc:
from concurrent.futures import ThreadPoolExecutor

import os
import requests
import subprocess
import shutil


def parse_m3u8(file_path):
    urls = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('http'):
                urls.append(line)
    return urls


class Download_segments():
    def __init__(self, urls, max_workers):
        self.urls = urls
        self.folder = 'ts_segments'
        self.max_workers = max_workers
        self.headers = {
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
            'cache-control': 'no-cache',
            'origin': 'https://rapid-cloud.co',
            'pragma': 'no-cache',
            'priority': 'u=1, i',
            'referer': 'https://rapid-cloud.co/',
            'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
        }

    def download_task(self, args):
        """单个下载任务"""
        idx, url = args
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            filename = os.path.join(self.folder, f'segment_{idx + 1:03d}.ts')
            with open(filename, 'wb') as f:
                f.write(response.content)
            return f'成功：{filename}'
        except Exception as e:
            return f'失败：{url} [{str(e)[:30]}]'  # 截短错误信息

    def main_mu(self):
        """多线程下载实现"""
        os.makedirs(self.folder, exist_ok=True)

        tasks = [(idx, url) for idx, url in enumerate(urls)]

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = executor.map(self.download_task, tasks)
            # 打印实时进度
            for result in results:
                print(result)


def merge_to_mp4(output, folder='ts_segments', ):
    # 生成文件列表（带文件夹路径）
    file_list = []
    for f in sorted(os.listdir(folder)):
        if f.endswith('.ts'):
            file_list.append(f"file '{os.path.join(folder, f)}'")

    with open('file_list.txt', 'w') as f:
        f.write('\n'.join(file_list))

    # 执行合并命令
    subprocess.run([
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', 'file_list.txt',
        '-c', 'copy',
        f'{output}.mp4'
    ], check=True)

    # 清理临时文件
    if os.path.exists(folder):
        shutil.rmtree(folder)
    if os.path.exists('file_list.txt'):
        os.remove('file_list.txt')

    print('合并完成！TS文件已自动删除，输出文件：output.mp4')


if __name__ == '__main__':
    m3u8_file = 'playlist.m3u8'  # M3U8文件路径
    urls = parse_m3u8(m3u8_file)

    download_segments = Download_segments(urls, max_workers=12)
    download_segments.main_mu()

    merge_to_mp4(output='海贼王1124')  # ffmpeg 合并并清理
