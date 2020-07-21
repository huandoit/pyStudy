#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/21 16:57
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 11. 盛最多水的容器.py
@Software: PyCharm
@description: https://leetcode-cn.com/problems/container-with-most-water/
"""
'''
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。

示例：
输入：[1,8,6,2,5,4,8,3,7]
输出：49
'''

'''
思路一：
双指针，两个指针一个指向头一个指向尾，计算面积，每次计算面积时保留大的那个数值，根据元素的大小判断指针左移还是右移
'''
def maxArea(height: List[int]) -> int:
    i = 0
    j = len(height) - 1
    area = 0
    while i < j:
        high = min(height[i], height[j])
        area = max(area, high * (j - i))
        if height[i] > height[j]:
            j -= 1
        else:
            i += 1
    return area