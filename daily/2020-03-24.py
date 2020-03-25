#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/25 16:47
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 2020-03-24.py
@Software: PyCharm
@description: 
"""


import re
import requests


seed_url = "https://www.bilibili.com/v/dance"

regex = r"\<a href=\"\/\/www\.bilibili\.com\/video\/[a-zA-Z0-9]+\""

def fetch_seed_context():
    r = requests.get(seed_url)
    with open("index.html", "w", encoding="utf-8") as index_obj:
        index_obj.write(r.text)

def extract_herf():
    with open("index.html", "r", encoding="utf-8") as index_obj:
        content = index_obj.read()
        matches = re.finditer(regex, content, re.MULTILINE)

        for matchNum, match in enumerate(matches, start=1):
            target_url = "https:{0}".format(match.group()[9:-1])
            print(target_url)

            next_r = requests.get(target_url)
            print(next_r)



if __name__ == '__main__':
    fetch_seed_context()
    extract_herf()

"""
1.#!/usr/bin/env python 将文件自动识别为python脚本
2.requests库入门：https://requests.readthedocs.io/zh_CN/latest/index.html
    - 发送请求：requests.get(seed_url, params=payload)
    - 一些基本属性：
        - r.text
        - r.encoding
        - r.content
3.with open的使用
    - 在with open语句中自动调用了close()方法，因此不需要单独关闭文件
    - open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
    - read(size)：一次性读取size字节的内容
    - readline()：每次读取一行，返回一个字符串对象
    - readlines():读取所有行，返回以每行为值的列表，可以搭配for ... in f.readlines()
    - write()：将内容写入文件
4.match()
    - 参考2.4.md
5.format格式化函数
"""