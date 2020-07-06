直接手写一个 Python 类

直接手写一个构造函数

紧接着上面的代码，直接手写，补充完整代码，要求：

对列表中的人进行排序，并筛选出分数大于80的人的名单，组成一个新的列表显示出来。
代码如下：

class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Student(Person):
    def __init__(self, name, gender, age,score):
        super(Student, self).__init__(name, gender, age)
        self.score = score

People = [kathy, Jim, John, Alice, Leo]
Python 的高阶函数有哪些，分别都有什么作用？

简单说说生成器，迭代器，装饰器是什么，都有哪些作用？

Python 中，如何将字符串转化为整型？

TCP 三次握手和四次挥手，请分别直接写出来

HTTP 常见的状态码有哪些？都是什么含义？

webdriver 的核心原理是什么？

Appium 是什么？主要用来做什么的？它的核心原理是什么？

selenium1 和 selenium2 的区别是什么，为何要抛弃 selenium1? 它有什么缺陷？

常见的元素定位方法有哪些？

直接手写一个冒泡排序和快速排序，时间复杂度是多少？空间复杂度是多少？是否稳定？

如何查询 Linux 后台日志，直接写出命令

如何查看当前进程？

Dockerfile 是什么？如何去创建一个 Dockerfile？

Python 有没有垃圾回收机制？它又是通过什么来的？

熟悉 TestNG？那请说一下用法？

熟悉 Java，那请直接手写一个单例模式？

数据库增删改查，手写 SQL

Redis 是做什么用的？ElasticSearch是什么？做什么用的？

接口测试怎么做的？如果存在接口依赖关系，怎么做？

元组和列表的区别是什么？

Python中，*arg 和 *kwarg 分别代表什么含义，都有哪些作用？

写过爬虫吗？那请说一下常见的反爬机制有哪些？如果是动态加载的页面，看不到数据，如何去进行爬取？