# -*- coding: utf-8 -*-
"""
@Time    : 2020/3/19 10:08
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 1.12.py
@Software: PyCharm
@description: 找出一个序列中出现次数最多的元素
"""


from collections import Counter


words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

word_counts = Counter(words)
# 出现频率最高的3个单词
top_three = word_counts.most_common(3)
print(top_three)
# 输出[('eyes', 8), ('the', 5), ('look', 4)]

print(word_counts)
# Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})

'''
1.collections.Counter
    - 为hashable对象计数，是字典的子类，返回的是(元素:计数)组成的字典
    - most_common([n])：返回一个列表，其中包含n个最常见的元素及出现次数，按常见程度由高到低排序
    - update():从 迭代对象 计数元素或者 从另一个 映射对象 (或计数器) 添加
        >>> morewords = ['why','are','you','not','looking','in','my','eyes']
        >>> word_counts.update(morewords)
        >>> word_counts['eyes']
        9
    - 进行数学运算操作：
        >>> a = Counter(words)
        >>> b = Counter(morewords)
        >>> a
        Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2,
        "you're": 1, "don't": 1, 'under': 1, 'not': 1})
        >>> b
        Counter({'eyes': 1, 'looking': 1, 'are': 1, 'in': 1, 'not': 1, 'you': 1,
        'my': 1, 'why': 1})
        >>> # Combine counts
        >>> c = a + b
        >>> c
        Counter({'eyes': 9, 'the': 5, 'look': 4, 'my': 4, 'into': 3, 'not': 2,
        'around': 2, "you're": 1, "don't": 1, 'in': 1, 'why': 1,
        'looking': 1, 'are': 1, 'under': 1, 'you': 1})
        >>> # Subtract counts
        >>> d = a - b
        >>> d
        Counter({'eyes': 7, 'the': 5, 'look': 4, 'into': 3, 'my': 2, 'around': 2,
        "you're": 1, "don't": 1, 'under': 1})
        >>>
'''