#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/21 14:00
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 283. 移动零.py
@Software: PyCharm
@description: https://leetcode-cn.com/problems/move-zeroes/
"""

'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
'''

'''
思路一：
设置计数器n，遍历列表，遇到0时将0删除同时计数器+1，遍历完成后在列表末尾添加n个0
'''
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = 0
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            nums.pop(i)
            n += 1
        else:
            i += 1
    for v in range(n):
        nums.append(0)
    # i = j = 0
    # for i in range(len(nums)):
    #     if nums[i] != 0:
    #         nums[j], nums[i] = nums[i], nums[j]
    #         j += 1

if __name__ == '__main__':
    moveZeroes([0,1,0,3,12])