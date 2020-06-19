#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/19 16:49
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : tuple操作.py
@Software: PyCharm
@description: 元组基本操作
"""

data_tuple = (21, "day", "python")
print("data_tuple: ", data_tuple)

# 索引
print("data_tuple[0]: ", data_tuple[0])
print("data_tuple[-1]: ", data_tuple[-1])

# 切片
print("data_tuple[:-1]: ", data_tuple[:-1])
print("data_tuple[::-1]: ", data_tuple[::-1])

# 拆包
data_1, data_2, data_3 = data_tuple
print(data_1, "/", data_2, "/", data_3)
