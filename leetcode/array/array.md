> https://leetcode-cn.com/tag/array/

# 数组
> 数组是在程序设计中，为了处理方便， 把具有相同类型的若干元素按有序的形式组织起来的一种形式。
> 
> 首先，数组会利用 索引 来记录每个元素在数组中的位置，且在大多数编程语言中，索引是从 0 算起的。我们可以根据数组中的索引，快速访问数组中的元素。事实上，这里的索引其实就是内存地址。
> 
> 其次，作为线性表的实现方式之一，数组中的元素在内存中是 连续 存储的，且每个元素占用相同大小的内存。
> 
> 例如对于一个数组 ['oranges', 'apples', 'bananas', 'pears', 'tomatoes']，为了方便起见，我们假设每个元素只占用一个字节，它的索引与内存地址的关系如下图所示。

# Python中的“数组”
在python中没有“数组”这个数据类型，数组可以看做是数据的集合，python中有四个数据类型与此类似：
- 列表list
- 元组tuple
- 集合set
- 字典dictionary

# List
list是一个有序且可更改的集合，允许有重复的成员

## 创建列表
```python
new_list = [1, "a", 2, "b"]
```

## 访问元素
- 列表第一个元素的索引为0
- 负索引表示从末尾开始
    - -1表示最后一个元素
    - -2表示倒数第二个元素
- 索引范围(切片)
    - `list[start:stop]`：表示取列表中索引为start到stop的所有元素，但不包含索引为stop的元素
    - `list[start:stop:step]`：表示以step为间隔，去列表中索引为start到stop的所有元素

## 更改元素值
直接使用等号赋值即可

## 遍历列表
可以使用for循环遍历列表
```python
def test(nums):
    for i in nums:
        print(i)
    for i in nums:
        print(i)
        nums.remove(i)

test([1,2,3,4,5,6])
# 输出结果分别为
# 1 2 3 4 5 6
# 1 3 5
```
for循环遍历列表时，是按索引遍历，所以在上面第二个循环时第一次循环索引0输出1后1被弹出，2的索引变为了0，第二次循环索引1时输出的是3

## 内置方法
- `list.append(i)`: 在列表末尾处添加新元素i
- `list.count(i)`: 返回元素i在列表中出现的次数
- `list.insert(index, i)`: 在指定索引处添加新元素
- `list.remove(i)`: 删除指定元素i
- `list.pop(index)`: 删除指定索引处的元素
- `list.clear()`: 清空列表
- `list.reverse()`: 反转list的顺序，不会返回新的列表
- `list.sort()`: 对list进行排序，不会返回新的列表
- `list1.extend(list2)`: 将list2中的元素添加到list1末尾中

## 其他操作
- 复制列表
    - `list2 = list1` 不是复制操作，list2只是list1的引用，list1和list2在地址中指向的是同一个列表，list1上的变动会同步到list2上
    - `list2 = list1.copy()` 复制
- 将其他类型变量转换成list
    - `list(object)` object可以是元组、集合和字典等
- 将两个列表合并
    - `list1 + list2`
    - `list1.extend(list2)`
- 统计列表的长度
    - `len(list)`
- 返回列表元素最大\最小值
    - `max(list)`
    - `min(list)`

# Dictionary
dictionary是一个无序、可变和有索引的集合，没有重复的成员

## 创建字典
- 字典中的数据以键值对的形式存在
- 键 是不能重复且不可变的，如字符串、数字和元组等
- 值 可以重复，可修改，可以是任意类型
```python
dict = {
    "key1": "value1",
    "key2": "value"
}
```

## 字典操作
- 访问字典中的值
    - `dict['key']`
    - `dict.get(key)`
- 修改字典，包括增加新的键值对和修改键的值
    - 修改键的值，直接给键赋值即可 `dict['key'] = new_value`
    - 增加新的键值对，同上 `dict['new_key'] = value`
- 删除字典元素
    - 清空字典 `dict.clear()`
    - 删除字典中的某个键值对 `del dict['key']`
    - 删除字典 `del dict`

## 内置方法
- `dict.clear()` 删除字段中的所有元素
- `dict.copy()` 返回字典的副本，简称复制
- `dict.fromkeys(keys, values)` keys和values可以都是列表，然后将keys中的元素提取做键，values中元素提取做值，排列组合生成新的字典
- `dict.get(key, default=None)` 返回key的值，如果key不存在则返回默认值
- `dict.has_key(key)` 如果键在dict里返回true，否则返回false
- `dict.items()` 将键值对保存为(键,值)，然后以列表的形式返回，如[(key1,value1), (key2,value2)]
- `dict.setdefault(key, default=None)` 获取在dict中key对应的值，如果key不存在则将key添加到dict中，值为设置的默认值，然后返回默认值
- `dict.update(dict2)` 将dict2中的键值对添加到dict1中
- `dict.values()` 以列表的形式返回字典中的所有值
- `dict.keys()` 以列表的形式返回字典中的所有键
- `dict.pop(key)` 删除指定键值对
- `dict.popitem()` 删除最后插入的键值对

## 其他操作
- 计算字典中元素的个数
    - `len(dict)`
- 将其他类型元素转换成字典类型
    - `dict(key=value, key1=value)`
- 遍历字典
    - `for x in dict` 遍历键
    - `for x, y in dict.items()` 遍历键和值