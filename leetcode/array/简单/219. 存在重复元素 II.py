#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/21 13:52
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 219. 存在重复元素 II.py
@Software: PyCharm
@description: https://leetcode-cn.com/problems/contains-duplicate-ii/
"""

'''
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

示例 1:
输入: nums = [1,2,3,1], k = 3
输出: true

示例 2:
输入: nums = [1,0,1,1], k = 1
输出: true

示例 3:
输入: nums = [1,2,3,1,2,3], k = 2
输出: false
'''

'''
思路一：
创建一个空字典用于存放遍历过的列表元素和对应索引，对于遍历的列表元素，与字典中的键做对比，存在则计算索引差值，大于k则说明字典中的索引小，替换掉
'''
def containsNearbyDuplicate(nums, k):
    dict = {}
    for index in range(len(nums)):
        key = nums[index]
        if key in dict:
            if index - dict[key] > k:
                dict[key] = index
            else:
                return True
        else:
            dict[key] = index
    return False