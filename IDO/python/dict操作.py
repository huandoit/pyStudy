#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/22 11:25
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : dict操作.py
@Software: PyCharm
@description: 字典类型基础操作
"""

data_dict = {
    "location": "shenzhen",
    "province": "guangzhou",
    "age": 25
}

# 访问
print(data_dict["age"])

# 修改
data_dict["sex"] = 1
print(data_dict)

# 删除
del data_dict["sex"]
print(data_dict)