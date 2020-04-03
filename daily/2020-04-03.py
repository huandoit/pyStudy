# -*- coding: utf-8 -*-
"""
@Time    : 2020/4/3 14:16
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 2020-04-03.py
@Software: PyCharm
@description: webdriver实现页面加载新数据后抓取信息并保存
"""

import os
import re
import time
import urllib.request
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


def down_pearvideo():
    storage = 'videos'
    if storage not in os.listdir():
        os.mkdir(storage)

    seed_url = "https://www.pearvideo.com/category_8"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    driver = webdriver.Chrome()
    driver.get(seed_url)
    driver.implicitly_wait(10)
    # print(driver.page_source)

    # 点击“加载更多”
    for i in range(1, 5):
        driver.find_element(By.ID, "listLoadMore").click()
        print(f'点击“加载更多” {i} 次')
        driver.implicitly_wait(10)
        # time.sleep(5)

    # 获取页面加载内容，下载视频
    content = driver.page_source
    vids_regex = r'<a href="(.*?)" class="vervideo-lilink actplay" target="_blank">'
    print(content)
    vids = re.findall(vids_regex, content)
    prefix_url = 'https://www.pearvideo.com/'
    videos = []
    for _ in vids:
        _url = prefix_url + _
        print(_url)
        videos.append(_url)

    for _ in videos:
        print(_)
        content = requests.get(_, headers=headers).text
        mp4_regex = r'ldUrl="",srcUrl="(.*?)",vdoUrl='
        video_url = re.findall(mp4_regex, content)
        title_regex = r'<h1 class="video-tt">(.*?)</h1>'
        video_title = re.findall(title_regex, content)
        print(f'正在下载视频：{video_title[0]}')
        urllib.request.urlretrieve(video_url[0], os.path.join(storage, f"{video_title[0]}.mp4"))


if __name__ == '__main__':
    down_pearvideo()