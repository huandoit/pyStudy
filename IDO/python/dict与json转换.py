#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

# dict类型转json
a = {
    "name": "idoxu",
    "sex": "male",
    "age": 30
}
print('a: ', a)
print("a type: ", type(a))

b = json.dumps(a)
print("b: ", b)
print("b type: ", type(b))

print("**************************")
# json转dict
a = '{"name": "idoxu","sex": "male","age": 30}'
print('a: ', a)
print("a type: ", type(a))

b = json.loads(a)
print("b: ", b)
print("b type: ", type(b))