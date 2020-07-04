#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
关键字参数：
    - 以“key=value”的形式传入函数
    - 在函数内部所有关键字参数组成一个字典dict
在定义函数时指定可变数量的关键字参数：
    - def func(x, **kwargs)
"""


def func(x, **kwargs):
    print(x)
    print(kwargs)
    print('总共有 %d 个参数' % len(kwargs))
    print('这些参数分别为：', kwargs)


func(20, name='rose', age=18)
