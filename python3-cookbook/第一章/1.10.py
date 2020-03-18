# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/18 13:22
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 1.10.py
@Software: PyCharm
@description: 删除序列相同元素并保持顺序
"""

# 针对hashable类型，利用集合和生成器解决
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
    - 
'''