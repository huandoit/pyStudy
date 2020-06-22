#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/22 17:43
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : string与dict转换.py
@Software: PyCharm
@description: string与dict转换
"""

# string -> dict
a = "{'name':'idoxu', 'sex':'male', 'age':30}"
b = eval(a)
print(a)
print(b)
print("a type: ", type(a))
print("b type: ", type(b))

# dict -> string
a = {
    'name': 'idoxu',
    'sex': 'male',
    'age': 30
}
b = str(a)
print(a)
print(b)
print("a type: ", type(a))
print("b type: ", type(b))