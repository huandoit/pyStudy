#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
给定一个整数数组，判断是否存在重复元素。
如果任意一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

示例 1:
输入: [1,2,3,1]
输出: true

示例 2:
输入: [1,2,3,4]
输出: false

示例 3:
输入: [1,1,1,3,3,4,3,2,4,2]
输出: true
'''

'''

'''


def containsDuplicate(nums):
    if len(nums) == 1 or nums == []:
        return False
    for index1 in range(len(nums)):
        bak = nums.copy()
        bak.pop(index1)
        if nums[index1] in bak:
            return True
    return False


if __name__ == '__main__':
    print(containsDuplicate([1,2,3,4]))