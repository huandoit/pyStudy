#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/29 10:05
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : map函数.py
@Software: PyCharm
@description: map()基本使用
"""


'''
map(function, iterable, ...)：
    - function 函数
    - iterable 可迭代对象
    - 返回结果：一个迭代器
题目：使用map()返回元素的平方
'''


def f(x):
    return x ** 2


l = []
for i in map(f, [1, 2, 3, 4, 5]):
    l.append(i)
print(l)

# 匿名函数
for i in map(lambda x: x ** 2, [1, 2, 3, 4, 5]):
    print(i)
