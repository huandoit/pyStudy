#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/2 16:43
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : yaml_config.py
@Software: PyCharm
@description: 读取yaml配置文件中的内容
"""

import os
import yaml


class YamlConfig(object):
    def __init__(self, filename="config.yaml"):
        src_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        yaml_file = os.path.join(src_path, "conf", filename)
        with open(yaml_file, 'r', encoding='utf-8') as f:
            cont = f.read()

        self.load = yaml.load(cont)
        # print(self.load)

    def get_runtime(self, option):
        print(self.load["runtime"][option])


if __name__ == '__main__':
    yaml = YamlConfig()
    yaml.get_runtime("log_level")