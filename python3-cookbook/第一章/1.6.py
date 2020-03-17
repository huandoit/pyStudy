# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/17 15:39
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 1.6.py
@Software: PyCharm
@description: 实现字典中的键映射多个值
"""

from collections import defaultdict


d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
for key in d.keys():
    print(key,  d[key])

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
for key in d.keys():
    print(key,  d[key])

pairs = [('a',1), ('a',2), ('a',3), ('b',1)]
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)

'''
defaultdict对象，返回一个新的类似字典的对象：
- defaultdict(list)即将(键-值对组成的)序列转换为(键-列表组成的)字典
- 对于不存在的键会自动创建
- 当值变成list、set类型时就可以使用append函数
'''