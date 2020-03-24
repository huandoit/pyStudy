# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/18 13:22
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 1.10.py
@Software: PyCharm
@description: 删除序列相同元素并保持顺序
"""

# 针对数值为hashable类型，利用集合和生成器解决
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

# 针对不可哈希类型的序列
def dedupe2(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

if __name__ == "__main__":
    a = [1, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))

    b = [{'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
    print(list(dedupe2(b, key=lambda d: (d['x'],d['y']))))

'''
1.yeild 与 return 的区别：
    - yield返回执行结果后不中断程序继续执行
    - return在返回执行结果后中断程序执行
2.hashable类型
    - 能通过哈希值来确定唯一对象的，称为可哈希对象
    - 数值、字符串、元组和函数等是hashable
    - 列表、字典和集合是unhashable
    - 可哈希对象可作为字典的键，或集合的成员
3.lambda的用法
    - lambda：匿名函数，可使用单行定义一个函数
    - 语法：(lambda 参数:函数体)
'''