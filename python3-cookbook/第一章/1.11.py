# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/18 17:29
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 1.11.py
@Software: PyCharm
@description: 切片命名
"""

# 从一段记录(字符串)中的某些固定位置提取字段
record = '....................100 .......513.25 ..........'
SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)


'''
1.硬编码和软编码：
    - 硬编码：使用固定值表示，不利于后期维护和理解
    - 软编码：通过变量取代固定值，在后期中更方便修改和维护
2.slice()
    - 语法：slice(start, stop[, step])，参数与列表切片相同
    - 返回：返回一个切片对象
    - slice.indices(size)：参数size相当于切片中的stop，一般用在slice之后：
        - 当size大于之前的stop时，则返回之前的切片元组内容(start, stop, step)
        - 当size小于之前的stop时，则将stop替换为size返回(start, size, step)
    - 其他用法：
        >>> a = slice(5, 50, 2)
        >>> a.start
        5
        >>> a.stop
        50
        >>> a.step
        2
'''