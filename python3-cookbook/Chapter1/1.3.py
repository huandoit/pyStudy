# -*- coding: utf-8 -*-
"""
@Time    : 2020/03/14 16:02
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 1.3.py
@Software: PyCharm
@Description:如何保留最后N个元素
"""

from collections import deque


# 读取文本内容并返回匹配行前N行
def search(lines, pattern, history=5):
    pervious_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, pervious_lines
        pervious_lines.append(line)


if __name__ == '__main__':
    with open(r'./1.2.md') as f:
        for l, prevlines in search(f, 'records', 3):
            for pline in prevlines:
                print(pline, end='')
            print(l, end='')
            print('-' * 20)

'''
deque(maxlen=N)用法：
- 该构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满时，老元素会自动被移初
- deque()表示创建一个无限大小的队列，可以在队列当两端执行添加和弹出元素操作
>>> q.append(1)
>>> q.append(2)
>>> q.append(3)
>>> q
deque([1, 2, 3])
>>> q.appendleft(4)
>>> q
deque([4, 1, 2, 3])
>>> q.pop()
3
>>> q
deque([4, 1, 2])
>>> q.popleft()
4
'''