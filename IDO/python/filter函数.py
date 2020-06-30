#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/30 14:03
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : filter函数.py
@Software: PyCharm
@description: filter函数基本使用
"""

'''
filter(function, iterable):用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象
    - function 判断函数
    - iterable 可迭代对象
    - 返回：一个迭代器对象
题目：使用filter()找出列表[1,2,3,4,5,6,7,8,9,10]中的奇数
'''


def odd(x):
    """
    判断x是否为奇数，如果是则返回x
    :param x:
    :return:
    """
    if x % 2 == 1:
        return x


print(list(filter(odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
