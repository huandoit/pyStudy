#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/3 11:10
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : data.py
@Software: PyCharm
@description: 读取excel中的数据方便testcase直接使用
"""

import os
import json
import xlrd


class ReadData(object):

    def __init__(self, filename):
        scr_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        data_path = os.path.join(scr_path, "data", filename)
        data_open = xlrd.open_workbook(data_path)
        self.data_excel = data_open.sheet_by_index(0)

    def get_url(self):
        '''
        获取请求的url
        :return:
        '''
        url = self.data_excel.cell(1, 3).value
        return url

    def get_method(self, case_name):
        '''
        获取请求类型
        :param case_name:
        :return:
        '''
        return self.get_case(case_name=case_name)[4]

    def get_data(self, case_name):
        '''
        获取请求数据，转化为字典格式
        :param case_name:
        :return:
        '''
        return json.loads(self.get_case(case_name)[6])

    def get_expect(self, case_name):
        '''
        期望结果
        :param case_name:
        :return:
        '''
        return self.get_case(case_name)[7]

    def get_case(self, case_name):
        '''
        根据case_name找到对应用例行
        :param case_name:
        :return: 用例所在行
        '''

        for i in range(1, self.data_excel.nrows):
            if self.data_excel.cell(i, 1).value == case_name:
                return self.data_excel.row_values(i)

        print("用例名称未找到")
        return None


if __name__ == '__main__':
    data = ReadData("test_login_data.xlsx")
    url = data.get_url()
    method = data.get_method("test_login_normal")
    json = data.get_data("test_login_normal")
    expect = data.get_expect("test_login_normal")
    print(url, method)
    print(type(json))
    print(json)
    print(expect)
