#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/16 11:00
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 66. 加一.py
@Software: PyCharm
@description: https://leetcode-cn.com/problems/plus-one/
"""

'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:

输入: [1,9,9]
输出: [2,0,0]
解释: 输入数组表示数字 200。
'''

'''
思路一：
将数组进行反转，给第0位执行+1操作后判断是否为10，如果为10则将第0为置位0并将后一位+1，然后依次判断后面几位是否为10并做相应操作。当最后一位为10时，则添加新值1。最后在反转
'''
def plusOne(digits):
    digits.reverse()
    digits[0] += 1
    for i in range(len(digits)):
        if digits[i] == 10:
            digits[i] = 0
            if i + 1 >= len(digits):
                digits.append(1)
            else:
                digits[i + 1] += 1
    digits.reverse()
    return digits