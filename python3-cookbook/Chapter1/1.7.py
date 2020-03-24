# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/17 17:05
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 1.7.py
@Software: PyCharm
@description: 创造一个可以控制元素顺序的字典
"""

from collections import OrderedDict
import json

d = OrderedDict()
d['foo'] = 3
d['bar'] = 2
d['spam'] = 1
d['grok'] = 4
for key in d:
    print(key, d[key])
    # foo 1 bar 2 spam 3 grok 4

print(d)
# OrderedDict([('foo', 1), ('bar', 2), ('spam', 3), ('grok', 4)])

print(json.dumps(d))
# {"foo": 1, "bar": 2, "spam": 3, "grok": 4}