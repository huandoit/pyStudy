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
from interface.src.common.data import ReadData


# url = "http://172.18.4.206/as/user/login"
data = ReadData("test_login_data.xlsx")
url = data.get_url()


def test_login_normal():
    case_name = "test_login_normal"
    case_data = data.get_data(case_name)
    req = requests.get(url=url, params=case_data)
    reslut = req.status_code
    assert reslut == 200


def test_login_wrong_username():
    case_name = "test_login_wrong_username"
    case_data = data.get_data(case_name)
    case_expect = data.get_expect(case_name)
    req = requests.get(url=url, params=case_data)
    reslut = req.text
    assert reslut == case_expect