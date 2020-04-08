#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/4/8 10:12
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 2020-04-08.py
@Software: PyCharm
@description: 对2020-04-07.py中的代码进行包装
"""

import re
import os
import time
import requests
import hashlib
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.by import By


class PearVideoSpider(object):

    def __init__(self, seed_url):
        self.seed_url = seed_url
        self.prefix = "https://www.pearvideo.com/"
        self.finish_video_urls = set()
        self.storage = 'videos'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        }
        self.author_urls = set()

    def _setup_driver(self):
        """ 初始化浏览器 """
        self.driver = webdriver.Chrome()

    def _click_more(self):
        """ 点击“加载更多”按钮 """
        self.driver.find_element(By.ID, "listLoadMore").click()
        time.sleep(3)

    def setup_storage(self):
        """ 创建视频存储路径 """
        if self.storage not in os.listdir():
            os.mkdir(self.storage)

    def get_top10_creator(self, regex):
        """
        获取前十名视频的作者地址
        :param regex: 匹配作者地址的正则表达式
        :return:
        """
        content = requests.get(self.seed_url, headers=self.headers).text
        author_ids = re.findall(regex, content)
        for _ in author_ids:
            _url = self.prefix + _
            self.author_urls.add(_url)

    def get_video_urls(self, pagesource):
        """
        查找页面中视频的链接地址
        :param pagesource: 页面源码
        :return:
        """
        vids_regex = r'<a href="(.*?)" class="vervideo-lilink actplay" target="_blank">'
        vids = re.findall(vids_regex, pagesource)
        videos = []
        for _ in vids:
            _url = self.prefix + _
            videos.append(_url)
        videos.reverse()
        return videos

    def download_video(self, video):
        """
        根据视频地址下载视频，并保存标题和描述
        :param video:访问视频的链接地址
        :return:
        """
        video_content = requests.get(video, headers=self.headers).text
        mp4_regex = r'ldUrl="",srcUrl="(.*?)",vdoUrl='
        video_url = re.findall(mp4_regex, video_content)
        title_regex = r'<h1 class="video-tt">(.*?)</h1>'
        video_title = re.findall(title_regex, video_content)

        md5 = hashlib.md5()
        md5.update(video_title[0].encode(encoding='utf-8'))
        md5_title = md5.hexdigest()

        print(f'正在下载视频：{video_title[0]}')
        urllib.request.urlretrieve(video_url[0], os.path.join(self.storage, f"{md5_title}.mp4"))

        sum_regex = r'<div class="summary">(.*?)</div>'
        video_sum = re.findall(sum_regex, video_content)
        with open(f"videos/{md5_title}.txt", 'w', encoding='utf-8') as f:
            f.write(video_title[0])
            f.write(video_sum[0])

    def run(self):
        # 创建存储目录
        self.setup_storage()

        # 获取前十名视频的作者地址
        self.get_top10_creator(regex=r'<a href="(.*?)" class="column">')

        # 初始化浏览器
        self._setup_driver()

        # 进入作者页面，获取作者页面下“最新”中的所有视频
        for _ in self.author_urls:
            print('-' * 60)
            print(f'作者地址：{_}')

            # 访问作者页面
            self.driver.get(_)
            self.driver.implicitly_wait(10)
            temp_pagesource = self.driver.page_source

            # 获取视频地址
            videos = self.get_video_urls(temp_pagesource)

            # 去掉页面中显示在“最热”模块的视频
            videos = videos[:-6]

            i = 1
            # 实现一直点击“加载更多”直到没有加载出新的内容
            while videos:
                print(f'当前队列里面有视频数量为: {len(videos)}')
                # 下载视频和相关描述信息
                while videos:
                    video = videos.pop()
                    print(f'当前爬取的视频地址: {video}')
                    self.download_video(video)

                # 在作者页面点击“加载更多”，获取更多视频信息
                self._click_more()
                print(f'点击“加载更多” {i} 次')
                i += 1

                # 重新获取页面内容
                new_pagesource = self.driver.page_source
                # 获取新的vids
                new_vids = self.get_video_urls(new_pagesource)
                old_vids = self.get_video_urls(temp_pagesource)
                vids = [vid for vid in new_vids if vid not in old_vids]

                # 当没有新vids时，跳出循环
                if vids:
                    temp_pagesource = new_pagesource
                    videos = vids
                else:
                    break


if __name__ == '__main__':
    pearVideoSpider = PearVideoSpider("https://www.pearvideo.com/popular_8")
    pearVideoSpider.run()