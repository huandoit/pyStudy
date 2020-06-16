#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/16 14:39
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : data_type.py
@Software: PyCharm
@description: python基本数据类型介绍
"""

'''
Python六大基本数据类型
1. 数字 Number
    - int 整型
    - float 浮点型
    - bool 布尔型
    - complex 复数
2. 字符串 String
    - 'str'
    - "str"
3. 列表 List
    - []
4. 元组 Tuple
    - ()
5. 集合 Set
    - {a, b}
6. 字典 Dict
    - {key1: value1, key2: value2}
'''

# 数字
a = 1
b = 1.0
c = True
d = 3.14j

# 字符串
str1 = 'wanghuan'
str2 = "wanghuan"

# 列表
list = ['wang', 'huan']

# 元组
tuple = ('hello', 'world')

# 集合
set = {'python', 'good'}

# 字典
dict = {
    'name': 'wanghuan',
    'age': 18
}
print(f'{a}的类型为：', type(a))
print(f'{b}的类型为：', type(b))
print(f'{c}的类型为：', type(c))
print(f'{d}的类型为：', type(d))


print(f'{str1}的类型为：', type(str1))
print(f'{str2}的类型为：', type(str2))


print(f'{list}的类型为：', type(list))


print(f'{tuple}的类型为：', type(tuple))


print(f'{set}的类型为：', type(set))


print(f'{dict}的类型为：', type(dict))