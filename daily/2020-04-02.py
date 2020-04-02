#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/4/2 11:00
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 2020-04-02.py
@Software: PyCharm
@description: https://github.com/junges521/taobao_crawler/blob/master/Xhs.py
"""

import json
import time
from pprint import pprint

import requests


# 返回一个基础的请求参数
def buildCommonParam():
    channel = "YingYongBao"
    timestamp = time.time()
    t = int(timestamp)
    deviceId = "7a750e37-f5a7-3936-9205-2a5c6d7c00c1"
    versionName = "6.26.0"
    device_fingerprint = "20191209121443dbc50fa4445184eb6d0105db6dc7d8a8019e126986183db0"
    params = {
        "channel": channel,
        "deviceId": deviceId,
        "device_fingerprint": device_fingerprint,
        "device_fingerprint1": device_fingerprint,
        "lang": "zh-Hans",
        "platform": "Android",
        "t": str(t),
        "type": "login",
        "versionName": versionName,
    }
    return params


def searchNote(keyword, authorization):

    # 请求api传的参数
    params = buildCommonParam()
    params["keyword"] = keyword
    params["filters"] = ""
    params["page"] = str(1)
    params["page_size"] = str(20)
    params["search_id"] = "01776AE76A678E55F8C1C6FE9B5184B0"
    params["sort"] = ""
    params["source"] = "explore_feed"
    params["sid"] = authorization

    # 拼接api请求参数
    paramStr = ""
    for key, value in params.items():
        paramStr = paramStr + key + "=" + value + "&"

    api = "https://www.xiaohongshu.com/api/sns/v10/search/notes?" + paramStr

    arr = {
        "action": "getShield",
        "url": api,
        "deviceId": params["deviceId"],
        "device_fingerprint": params["device_fingerprint"],
        "authorization": authorization
    }
    shield, sign = getShield(arr)
    xhsApi = api + "sign=" + sign
    # 请求api
    xhsRequest(xhsApi, shield, params["deviceId"], authorization)


def getSmsCode(phone, authorization):
    params = buildCommonParam()
    params["phone"] = phone
    params["zone"] = "86"

    paramStr = ""
    for key, value in params.items():
        paramStr = paramStr + key + "=" + value + "&"

    api = "https://www.xiaohongshu.com/api/sns/v1/system_service/vfc_code?" + paramStr

    arr = {
        "action": "getShield",
        "url": api,
        "deviceId": params["deviceId"],
        "device_fingerprint": params["device_fingerprint"],
        "authorization": authorization
    }
    shield, sign = getShield(arr)
    xhsApi = api + "sign=" + sign
    xhsRequest(xhsApi, shield, params["deviceId"], authorization)


def xhsRequest(xhsApi, shield, deviceId, authorization):
    # 防止请求频繁
    if shield:
        xhsHeaders = {
            "shield": shield,
            "device_id": deviceId,
            "Authorization": authorization,
            "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 7.1.2; Redmi 5 Plus MIUI/8.11.2) Resolution/1080*2030 Version/6.26.0 Build/5210121 Device/(Xiaomi;Redmi 5 Plus)"
        }
        proxyUrl = "http://dy.1918.cn/api/sign/proxy?tdsourcetag=s_pctim_aiomsg"
        result = requests.get(proxyUrl, timeout=20)
        pprint(result)

        jobj = json.loads(result.text)
        proxy = jobj["proxy"]
        pprint(proxy)
        # proxies = None

        proxies = {
            'http': 'http://{0}'.format(proxy),
            'https': 'https://{0}'.format(proxy)
        }

        result = requests.get(xhsApi, timeout=20, headers=xhsHeaders, proxies=proxies, verify=True)
        pprint(result.text)


def getShield(arr):
    """
    请求了一个接口，该接口返回结果为json格式的字符串，从返回结果中取出shield和sign的值
    :param arr:
    :return:
    """
    requestURL = "http://127.0.0.1:9999/fakeXhsParam"

    headers = {
        "allow_access": "true",
        "user-agent": "xhs"
    }

    result = requests.post(requestURL, data=json.dumps(arr), timeout=20, headers=headers)
    pprint(result)
    shield = ""
    # 当接口请求正常时执行下面的代码
    if result.status_code == requests.codes.ok:
        dataStr = result.text
        # 将返回的json字符串解码为dict对象
        jobj = json.loads(dataStr)
        shield = jobj["data"]["shield"]
        sign = jobj["data"]["sign"]
    pprint(shield)
    return shield, sign


if __name__ == '__main__':
    phone = "13335938860"
    authorization = "session.1566023018517656053845"
    # getSmsCode(phone, authorization)
    keyword = u"电脑"
    searchNote(keyword, authorization)
