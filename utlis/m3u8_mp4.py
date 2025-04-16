# -- coding: utf-8 --
# @Author: 胡H
# @File: m3u8_mp4.py
# @Created: 2025/4/15 15:38
# @LastModified: 
# Copyright (c) 2025 by 胡H, All Rights Reserved.
# @desc:  将m3u8内容提取ts并转换为mp4

import os
import requests
import subprocess
from urllib.parse import urljoin


def parse_m3u8(m3u8_content):
    """解析M3U8内容，返回TS文件路径列表"""
    return [line.strip() for line in m3u8_content.split('\n')
            if line.strip() and not line.startswith('#')]


def download_ts(ts_paths, base_url, output_dir="ts_files"):
    """下载所有TS文件到指定目录"""
    os.makedirs(output_dir, exist_ok=True)
    downloaded_files = []

    for path in ts_paths:
        ts_url = urljoin(base_url, path)
        filename = os.path.join(output_dir, os.path.basename(path))

        # 下载TS文件
        try:
            with requests.get(ts_url, stream=True) as r:
                r.raise_for_status()
                with open(filename, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
            downloaded_files.append(filename)
            print(f"已下载: {filename}")
        except Exception as e:
            print(f"下载失败 {ts_url}: {str(e)}")

    return downloaded_files


def merge_files(file_list, output_file):
    """使用FFmpeg合并文件"""
    list_file = "file_list.txt"

    # 生成文件列表
    with open(list_file, 'w') as f:
        for file in file_list:
            f.write(f"file '{file}'\n")

    # 执行合并命令
    subprocess.run([
        'ffmpeg',
        '-f', 'concat',
        '-safe', '0',
        '-i', list_file,
        '-c', 'copy',
        output_file
    ], check=True)

    # 清理临时文件
    os.remove(list_file)


if __name__ == "__main__":
    M3U8_FILE = "index.m3u8"  # 本地路径
    BASE_URL = "https://c1.rrcdnbf6.com/video/lianqishiwannian/%E7%AC%AC01%E9%9B%86/"  # TS文件的基础URL
    OUTPUT_MP4 = "lianqishiwannian.mp4"

    with open(M3U8_FILE, 'r') as f:
        m3u8_content = f.read()

    # 解析并下载TS文件
    ts_paths = parse_m3u8(m3u8_content)
    downloaded_files = download_ts(ts_paths, BASE_URL)

    # 合并文件
    if downloaded_files:
        merge_files(downloaded_files, OUTPUT_MP4)
        print(f"合并完成，输出文件: {OUTPUT_MP4}")
    else:
        print("没有文件需要合并")
