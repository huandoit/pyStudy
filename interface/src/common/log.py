#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/6/5 14:41
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : log.py
@Software: PyCharm
@description: 日志模块封装
"""

import os
import time
import logging
from interface.src.common.config import Config, src_path


class Log(object):
    '''
    1.配置log输出格式 time - loglevel - file - func - line - msg
    2.支持输出到log文件和屏幕
    3.支持返回一个logger，让其他模块调用
    '''

    @classmethod
    def config_log(cls):
        '''
        对日志的输入格式、level、日志文件位置等进行配置
        :return:
        '''
        # 从配置文件中获取日志级别
        config = Config()
        log_level = config.get_runtime("log_level")

        # 定义日志文件的输出位置和命名规则
        log_dir = os.path.join(src_path, config.get_runtime("log_dir"))
        timestamp = time.strftime("%Y%m%d", time.localtime(time.time()))
        log_file = os.path.join(log_dir, timestamp+".log")

        # 声明logger并配置level
        cls.logger = logging.getLogger()
        cls.logger.setLevel(log_level)

        # 建立handler
        fh = logging.FileHandler(log_file, mode="a", encoding='utf-8')
        ch = logging.StreamHandler()

        # 定义输出格式
        ft = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
        fh.setFormatter(ft)
        ch.setFormatter(ft)

        # 将handler加入到logger中
        cls.logger.addHandler(fh)
        cls.logger.addHandler(ch)
        return cls.logger

    @classmethod
    def get_logger(cls):
        cls.logger = cls.config_log()
        return cls.logger


if __name__ == '__main__':
    l = Log.get_logger()
    l.info("abc")
    l.debug("debug")