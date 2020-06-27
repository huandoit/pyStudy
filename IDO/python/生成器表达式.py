#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用生成器表达式构建生成器
a = (i for i in range(0, 10))
print("a type: ", type(a))

# 生成器无法直接全部输出结果
print(a)

# 使用next()函数访问生成器中的值
print(next(a))

print("*" * 20)
# 使用for循环逐个访问生成器中的值
for v in a:
    print(v)

