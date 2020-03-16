# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/16 16:17
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 1.4.py
@Software: PyCharm
@description: 查找最大或最小的N个元素
"""
import heapq


# 在一个列表中找到最大的N个元素
def maxN(nums, n):
    maxn = heapq.nlargest(n, nums)
    print(maxn)


# 在一个列表中找到最小的N个元素
def mixN(nums, n):
    mixn = heapq.nsmallest(n, nums)
    print(mixn)


# 当列表中存在多组值时可以根据关键字排序获取最大值
def maxKey(portfolio, n):
    maxn = heapq.nlargest(n, portfolio, key=lambda s: s['price'])
    print(maxn)


if __name__ == "__main__":
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    maxN(nums, 4)
    mixN(nums, 4)
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    maxKey(portfolio, 1)

'''
1.堆数据结构(heap)：
    - 是一个近似完全二叉树的的结构
    - 同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点
2.heapq模块：
    - 利用堆数据的结构来进行相关操作的一个模块，主要是进行排序操作
    - heap = [] 创建一个空堆
    - heappush(heaq, item) 往堆中插入一条新的值
    - heappop(heap) 从堆中弹出最小值
    - heap[0] 查看堆中的最小值，不弹出
    - heapify(x) 以线性时间将一个列表转换成堆
    - heapq.nlargest(n , iterbale, key=None) 返回堆中最大的N个值
        >>> list = [3, 5, 7, 10, -5]
        >>> import heapq
        >>> heapq.heapify(list)
        >>> list
[-5, 3, 7, 10, 5]
3.友情提示：
    - 当要查找的元素个数相对比较小的时候，函数 nlargest() 和 nsmallest() 是很合适的
    - 如果想查找唯一的最小或最大(N=1)的元素的话，那么使用 min() 和 max() 函数会更快些
    - 如果 N 的大小和集合大小接近的时候，通常先排序这个集合然后再使用切片操作会更快点(sorted(items)[:N] 或者是 sorted(items)[-N:])
'''