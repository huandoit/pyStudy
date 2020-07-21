#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/16 16:55
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 88. 合并两个有序数组.py
@Software: PyCharm
@description: https://leetcode-cn.com/problems/merge-sorted-array/
"""

'''
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

说明:
    初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
    你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。

示例:
输入:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3
输出: [1,2,2,3,5,6]
'''

'''
思路一：
偷懒方法，使用list内置方法
'''
def merge(self, nums1, m, nums2, n) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1[m:] = nums2
    nums1.sort()
