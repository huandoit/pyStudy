#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/4/1 9:48
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 2020-03-31.py
@Software: PyCharm
@description: 爬虫实例操作，下载梨视频中的所有视频
"""
import hashlib
import os
import re
import urllib.request
import requests

# 查看是否存在videos目录，如果没有则创建
storage = 'videos'
if storage not in os.listdir():
    os.mkdir(storage)

seed_url = 'https://www.pearvideo.com/category_8'
prefix_url = 'https://www.pearvideo.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}


# 下载科技页面的视频
def download_pearvideo():
    # 找到页面中的视频地址并保存
    content = requests.get(seed_url, headers=headers).text
    vids_regex = r'<a href="(.*?)" class="vervideo-lilink actplay">'
    vids = re.findall(vids_regex, content)
    videos = []
    for _ in vids:
        _url = prefix_url + _
        videos.append(_url)

    # 访问视频地址，将视频保存为以标题命名的视频文件
    for _ in videos:
        print(_)
        content = requests.get(_, headers=headers).text
        mp4_regex = r'ldUrl="",srcUrl="(.*?)",vdoUrl='
        video_url = re.findall(mp4_regex, content)
        title_regex = r'<h1 class="video-tt">(.*?)</h1>'
        video_title = re.findall(title_regex, content)
        print(f'正在下载视频：{video_title[0]}')
        urllib.request.urlretrieve(video_url[0], os.path.join(storage, f"{video_title[0]}.mp4"))


# 进阶，在科技页面找到所有作者进入作者页面，保存对应视频
def download_authorvideo():
    content = requests.get(seed_url, headers=headers).text
    author_regex = r'<a href="(.*?)" class="column">'
    author_ids = re.findall(author_regex, content)
    author_url = []
    for _ in author_ids:
        _url = prefix_url + _
        if _url not in author_url:
            author_url.append(_url)

    videos = []

    for _ in author_url:
        content = requests.get(_, headers=headers).text
        vids_regex = r'<a href="(.*?)" class="vervideo-lilink actplay">'
        vids = re.findall(vids_regex, content)
        for v in vids:
            _url = prefix_url + v
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

# 进阶，将视频名称保存为md5加密值，并将描述文字保存为相同md5值的txt文件
def md5_video():
    content = requests.get(seed_url, headers=headers).text
    vids_regex = r'<a href="(.*?)" class="vervideo-lilink actplay">'
    vids = re.findall(vids_regex, content)
    videos = []
    for _ in vids:
        _url = prefix_url + _
        videos.append(_url)

    # 访问视频地址，将视频保存为md5加密后的视频文件
    for _ in videos:
        print(_)
        content = requests.get(_, headers=headers).text
        mp4_regex = r'ldUrl="",srcUrl="(.*?)",vdoUrl='
        video_url = re.findall(mp4_regex, content)
        title_regex = r'<h1 class="video-tt">(.*?)</h1>'
        video_title = re.findall(title_regex, content)

        md5 = hashlib.md5()
        md5.update(video_title[0].encode(encoding='utf-8'))
        md5_title = md5.hexdigest()

        print(f'正在下载视频：{video_title[0]}')
        urllib.request.urlretrieve(video_url[0], os.path.join(storage, f"{md5_title}.mp4"))

        sum_regex = r'<div class="summary">(.*?)</div>'
        video_sum = re.findall(sum_regex, content)
        with open(f"videos/{md5_title}.txt", 'w', encoding='utf-8') as f:
            f.write(video_sum[0])


if __name__ == '__main__':
    # download_pearvideo()
    # download_authorvideo()
    md5_video()

"""
1.os
    - 可以进行文件路径相关的操作
    - os.listdir(path)：返回一个列表，该列表包含了path中所有文件与目录的名称
    - os.mkdir(path)：创建一个名为path的目录
2.f-string格式化字符串
    - 使用方法和str.format()类似，但是要更简洁
    - 在字符串中使用{}将变量括起来，如 f"{md5_title}.mp4"
3.python md5加密
    - 使用库hashlib
    - m = hashlib.md5()：创建md5对象
    - m.update(str)：更新hash对象，但是只能接受字节对象，因此对于字符串可以使用encode方法进行编码后传入
    - m.hexdigest()：16进制形式返回加密内容
"""