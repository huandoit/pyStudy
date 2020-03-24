# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/17 14:16
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 1.5.py
@Software: PyCharm
@description: 使用heapq实现一个优先级队列
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item)) # 优先级为负数的目的是使得元素按照优先级从高到低排序
        self._index += 1 # index 变量的作用是保证同等优先级元素的正确排序

    # 返回优先级最高的元素
    def pop(self):
        return heapq.heappop(self._queue)[-1] # -1是指返回(-priority, self._index, item)中的'item'


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 4)
    q.push(Item('spam'), 5)
    q.push(Item('grok'), 3)
    q.push(Item('wang00'), 2)
    print(q.pop())
    print(q.pop())
