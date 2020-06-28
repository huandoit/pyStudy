#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/28 16:47
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 阶乘函数.py
@Software: PyCharm
@description: 简单的阶乘函数
"""


def factorial(n):
    """
    阶乘函数n！
    :param n:
    :return:
    """

    if n == 0:
        value = 1
    else:
        value = n * factorial(n-1)
    return value


print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
