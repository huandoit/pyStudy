#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/7/16 17:50
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 118. 杨辉三角.py
@Software: PyCharm
@description: https://leetcode-cn.com/problems/pascals-triangle/
"""

'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''


def generate(numRows):
    pascal = [[1]]

    if numRows == 1:
        return pascal
    elif numRows == 2:
        pascal = [[1], [1, 1]]
        return pascal
    else:
        pascal = [[1], [1, 1]]
        n = pascal[1]
        n_row = []
        i = 0
        for row in range(3, numRows + 1):
            while i < row:
                if i == 0:
                    n_row.append(1)
                elif i == row - 1:
                    n_row.append(1)
                else:
                    value = n[i - 1] + n[i]
                    n_row.append(value)
                i += 1
            pascal.append(n_row)
            n = pascal[row - 1]
            i = 0
        return pascal


if __name__ == '__main__':
    generate(1)