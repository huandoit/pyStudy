#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/22 11:36
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : string和int转换.py
@Software: PyCharm
@description: string和int类型转换
"""

a = "21"

# 10进制string转换成int
print(int(a))

# 16进制string转换成int
print(int(a, 16))

a = 21

# int转换成10进制string
print(str(a))

# int转换成16进制string
print(hex(a))