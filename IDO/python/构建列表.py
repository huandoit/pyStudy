#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用for循环构建列表
list_for = []
for i in range(1,100):
    list_for.append(i)
print("使用for循环构建列表")
print(list_for)

print("使用列表推导式（也交列表生成式）构建列表")
# 使用列表推导式（也叫列表生成式）构建列表
list_build = [i for i in range(1, 100)]
print(list_build)