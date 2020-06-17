#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/17 16:33
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : string操作.py
@Software: PyCharm
@description: 字符串基本操作
"""

data_string = "21 day python"

# 切割
print(data_string[:])
print(data_string[1:9])
print(data_string[:-1])

# 拼接
print(data_string + "hello world")

# 复制
print(data_string * 2)

# 占位引用
print("%s" % data_string)
