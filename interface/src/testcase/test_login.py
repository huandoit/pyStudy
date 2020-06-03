#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/2 14:29
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : test_login.py
@Software: PyCharm
@description: 01最最最简单的接口测试用例
"""

import requests


url = "http://172.18.4.206/as/user/login"


def test_login_normal():
    data = {
        "token_type":"COOKIE",
        "cookie_type":"WAL",
        "userName":"root",
        "password":"111111"
    }
    req = requests.post(url=url, data=data)
    reslut = req.status_code
    assert reslut == 200