#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/3 16:46
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 可变参数.py
@Software: PyCharm
@description: 可变参数
"""

'''
可变参数：允许在调用参数的时候传入多个参数
    - 多个位置参数 def func(*args):
    - 多个关键字参数 def func(**kwargs):
    - 所有的args参数会被合并成一个元组
    - 所有的kwargs参数会被合并成一个字典
位置参数：
    - 调用函数时根据函数定义的参数位置传递参数
    - def func(x, y):
关键字参数：
    - 调用函数时，通过“key=value”的形式加以指定
    - def func(name='wanghuan')
    - 关键字参数必须在位置参数后面
'''


def func(*args):
    print(args)
    print(args[0], '\n')


func('P', 'y', 't', 'h', 'o', 'n')
func('Python', 123, '爬虫')
func(*(1, 2, 3))
func((1, 2, 3))