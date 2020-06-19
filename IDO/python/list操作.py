#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/19 16:20
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : list操作.py
@Software: PyCharm
@description: 列表基本操作
"""

data_list = [21, "day", "python"]

# 索引
print(data_list[0], "\n", data_list[-1])

# 切片
print(data_list[:-1])
print(data_list[::-1])
print(data_list[1:2])

# 连接
data_list.append("hello world")
print(data_list)

# 赋值
print(data_list*2)
data_list[1:2] = "may"
print(data_list)
data_list[1:2] = ["may"]
print(data_list)

data_list[1:] = "may3"
print(data_list)