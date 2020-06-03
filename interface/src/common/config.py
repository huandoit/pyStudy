#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/2 15:38
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : config.py
@Software: PyCharm
@description: 读取conf/default.conf中的配置信息
"""

import os
import configparser

# 获取src的路径
src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config(object):
    def __init__(self, filename="default.conf"):
        self.cf = configparser.ConfigParser()
        self.cf.read(os.path.join(src_path, "conf", filename))

    def get_runtime(self, option):
        return self.cf.get("runtime", option)


if __name__ == '__main__':
    c = Config()
    print(c.get_runtime("log_level"))


'''
1.os.path.abspath(path)
    - 返回path的绝对路径
    - E:\github\pyStudy\interface\src\common\config.py
2.os.path.dirname(path)
    - 返回路径最后一个/之前的内容
    - os.path.dirname('E:/github/pyStudy/interface/src/common') -> E:/github/pyStudy/interface/src
    - os.path.dirname('E:/github/pyStudy/interface/src/common/') -> E:/github/pyStudy/interface/src/common/
3.os.path.join(path, *paths)
    - 将path与*paths进行拼接
    - os.path.join(src_path, "conf", "file.md") -> E:\github\pyStudy\interface\src\conf\file.md
'''