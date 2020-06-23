#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/23 16:50
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : string与bytes转换.py
@Software: PyCharm
@description: 
"""

# 将string转换为utf-8格式的bytes
a = "21 python"
b = a.encode()
print("b type: ", type(b))
print(b)

# 将utf-8格式的bytes转换为string
a = b'21 python'
b = a.decode()
print("b type: ", type(b))
print(b)