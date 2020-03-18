# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/18 10:28
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 1.8.py
@Software: PyCharm
@description: 在数据字典中执行一些计算操作（比如求最小值、最大值、排序等等）
"""

'''
思路：使用zip()将键与值进行反转后进行操作
'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 获取最大最小值
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price)
# (10.75, 'FB')
print(max_price)
# (612.78, 'AAPL')

# 排序
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.78, 'AAPL')]

'''
1.字典的一些特殊性质：
    - mix(prices)返回的是最小的键
    - mix(prices.values())返回的是最小的值
2.zip()
    - 参数：可迭代对象
    - 返回值：将可迭代对象元素打包成一个个元组后组成的对象
3.sorted()
    - 参数：可迭代对象，还有其他参数
    - 返回值：将可迭代对象排序后返回为列表
    - 与sort()的区别，sort()是应用在list上的方法，无返回值，sorted()是应用在对象上的方法，返回新的list
'''