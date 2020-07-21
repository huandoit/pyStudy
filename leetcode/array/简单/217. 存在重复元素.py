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
思路一：
哈希表，依次遍历数组，将已遍历的数组存入字典中，遍历下一个数时与字典中的键进行对比，存在表示有重复项，不存在则是没有
'''
def containsDuplicate(nums):
    if len(nums) < 2:
        return False
    dict = {}
    for i in nums:
        if i in dict:
            return True
        else:
            dict[i] = 1
    return False


if __name__ == '__main__':
    print(containsDuplicate([1, 2, 3, 4]))