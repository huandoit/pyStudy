# /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/4/7 10:26
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 2020-04-07.py
@Software: PyCharm
@description: 在梨视频科技排行榜中获取前十名视频的对应作者的全部视频内容
"""

import re
import os
import time
import requests
import hashlib
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By


def down_top10_techvideo():
    storage = 'videos'
    if storage not in os.listdir():
        os.mkdir(storage)

    seed_url = 'https://www.pearvideo.com/popular_8'
    prefix_url = 'https://www.pearvideo.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    # 获取前十名视频的作者
    content = requests.get(seed_url, headers=headers).text
    author_regex = r'<a href="(.*?)" class="column">'
    author_ids = re.findall(author_regex, content)
    author_url = []
    for _ in author_ids:
        _url = prefix_url + _
        author_url.append(_url)

    videos = []
    driver = webdriver.Chrome()

    # 进入作者页面，获取作者页面下“最新”中的所有视频
    for _ in author_url:
        print('-' * 60)
        print(f'作者地址：{_}')

        # 访问作者页面
        driver.get(_)
        driver.implicitly_wait(10)
        temp_pagesource = driver.page_source

        # 匹配视频链接
        vids_regex = r'<a href="(.*?)" class="vervideo-lilink actplay" target="_blank">'
        vids = re.findall(vids_regex, temp_pagesource)
        # 剔除前六个热门视频
        for i in range(0, 6):
            vids.pop(0)
        for _ in vids:
            _url = prefix_url + _
            videos.append(_url)

        i = 1
        # 实现一直点击“加载更多”直到没有加载出新的内容
        while videos:
            # 在作者页面点击“加载更多”，获取更多视频信息
            driver.find_element(By.ID, "listLoadMore").click()
            print(f'点击“加载更多” {i} 次')
            i += 1
            time.sleep(3)
            # 重新获取页面内容
            new_pagesource = driver.page_source
            # 获取新的vids
            new_vids = re.findall(vids_regex, new_pagesource)
            old_vids = re.findall(vids_regex, temp_pagesource)
            vids = (vid for vid in new_vids if vid not in old_vids)

            # 当没有新vids时，跳出循环
            if vids:
                temp_pagesource = new_pagesource
                for v in vids:
                    _url = prefix_url + v
                    videos.append(_url)
            else:
                break

            # 访问videos中的视频地址，保存对应视频文件和相关描述信息，并将已保存过的视频链接从videos中去除
            for video in videos:
                print(video)
                video_content = requests.get(_, headers=headers).text
                mp4_regex = r'ldUrl="",srcUrl="(.*?)",vdoUrl='
                video_url = re.findall(mp4_regex, video_content)
                title_regex = r'<h1 class="video-tt">(.*?)</h1>'
                video_title = re.findall(title_regex, video_content)

                md5 = hashlib.md5()
                md5.update(video_title[0].encode(encoding='utf-8'))
                md5_title = md5.hexdigest()

                print(f'正在下载视频：{video_title[0]}')
                urllib.request.urlretrieve(video_url[0], os.path.join(storage, f"{md5_title}.mp4"))

                sum_regex = r'<div class="summary">(.*?)</div>'
                video_sum = re.findall(sum_regex, content)
                with open(f"videos/{md5_title}.txt", 'w', encoding='utf-8') as f:
                    f.write(video_title[0])
                    f.write(video_sum[0])
                videos.remove(video)


if __name__ == '__main__':
    down_top10_techvideo()