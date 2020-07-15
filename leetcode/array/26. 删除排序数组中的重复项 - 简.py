#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/15 11:16
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 26. 删除排序数组中的重复项 - 简.py
@Software: PyCharm
@description: https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
"""

'''
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例:
给定 nums = [0,0,1,1,1,2,2,3,3,4],
函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。
你不需要考虑数组中超出新长度后面的元素。
'''

'''
思路一：
通过数组内置方法获取一个数值的出现次数，如果次数大于1进行下面的操作：获取这个数值第一次出现的位置索引，把该位置后对应数量的元素删除，即去除重复值。然后进行下一次判断

知识点：
- list.count(value)：返回value在list中出现的数量
- list.index(value)：返回元素value第一次出现时的索引
- list.pop(index)：将列表中索引为index的元素删除
'''

def removeDuplicates(nums):
    for i in nums:
        if nums.count(i) != 1:
            index = nums.index(i)
            for n in range(0, nums.count(i) - 1):
                nums.pop(index)
    print(nums)
    return len(nums)

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    removeDuplicates(nums)