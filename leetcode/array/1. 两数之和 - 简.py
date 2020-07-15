#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/15 9:58
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 1. 两数之和 - 简.py
@Software: PyCharm
@description: https://leetcode-cn.com/problems/two-sum
"""

'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

示例:
    给定 nums = [2, 7, 11, 15], target = 9
    因为 nums[0] + nums[1] = 2 + 7 = 9
    所以返回 [0, 1]
'''

'''
思路一：
两次for循环遍历，分别取出两个值与目标值进行比对，成功则返回，失败则进行下一轮遍历
时间复杂度：O(n^2)
空间复杂度：O(1)
'''
class Solution:
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    l = [i, j]
                    return l


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 26
    l = Solution().twoSum(nums, target)
    print(l)
