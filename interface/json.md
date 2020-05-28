# python json解析

## json概述
> 百度百科：
>
> JSON(JavaScript Object Notation, JS 对象简谱) 是一种轻量级的数据交换格式。
>
> 它基于 ECMAScript (欧洲计算机协会制定的js规范)的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。

```json
{
    "name": "中国",
    "province": [{
        "name": "黑龙江",
        "cities": {
            "city": ["哈尔滨", "大庆"]
        }
    }, {
        "name": "广东",
        "cities": {
            "city": ["广州", "深圳", "珠海"]
        }
    }, {
        "name": "台湾",
        "cities": {
            "city": ["台北", "高雄"]
        }
    }, {
        "name": "新疆",
        "cities": {
            "city": ["乌鲁木齐"]
        }
    }]
}
```
语法规则：
- 对象表示为键值对
- 数据由逗号分隔
- 花括号保存对象
- 方括号保存数组

## python的json模块
> https://docs.python.org/zh-cn/3/library/json.html

### json.dumps/json.dump

### json.loads/json.load