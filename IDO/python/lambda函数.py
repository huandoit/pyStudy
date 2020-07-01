#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/1 16:46
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : lambda函数.py
@Software: PyCharm
@description: 匿名函数的基本使用
"""

'''
匿名函数：
    - 语法："lambda arguments : expression"
    - 可以接受任意数量的参数，但只能有一个表达式
题目：使用lambda函数将列表[1.2.3.4.5]中的每个元素都平方
'''

x = lambda n: n ** 2

# 笨方法
for i in [1, 2, 3, 4, 5]:
    print(x(i))

# map
print(list(map(x, [1, 2, 3, 4, 5])))
