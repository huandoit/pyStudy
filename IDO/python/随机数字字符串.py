#!/usr/bin/env python
# -*- coding: utf-8 -*-


import random
import string

'''
题目1：写出6位的包含大小写在内的随机字符串
题目2：写出8位包含数字的随机数字
1. str.join(value): 用于将序列中的元素以指定的字符连接生成一个新的字符串
    - str 连接字符
    - value 要连接的元素
2. random.sample(sequence, k): 从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列
3. string.ascii_letters: 生成所有字母
4. string.digits: 生成所有数字

'''

ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 6))
print(ran_str)

ran_int = ''.join(random.sample(string.digits, 8))
print(ran_int)

'''
1. random.randint(a, b): 用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限
2. random.randrange([start], stop[, step]): 从指定范围内，按指定基数递增的集合中获取一个随机数.
    - random.randrange(10, 100, 2)，结果相当于从[10, 12, 14, 16, ... 96, 98]序列中获取一个随机数
3. random.choice(sequence): 从序列中获取一个随机元素
'''

ran_int = random.randint(10000000, 99999999)
print(ran_int)