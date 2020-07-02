#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/2 16:42
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 传参练习.py
@Software: PyCharm
@description: 
"""


def func(a, b):
    print(a+b)


func(1, 2)


# 设置参数默认值
def func2(a, b=2):
    print(a+b)


func2(1)
func2(1, 4)
