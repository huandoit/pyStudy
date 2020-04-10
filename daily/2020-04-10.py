#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2020/4/10 11:21
@Author  : WangHuan
@Contact : hi_chengzi@126.com
@File    : 2020-04-10.py
@Software: PyCharm
@description: 与2020-04-10.md配套的运行代码
"""

import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# 使用.send_keys()操作
def send_keys_demo():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    # 定位百度首页搜索输入框
    search_input = driver.find_element(By.ID, 'kw')
    # 在输入框中输入内容
    search_input.send_keys('Selenium')
    # 在输入框中按键盘回车键
    search_input.send_keys(Keys.ENTER)
    time.sleep(10)


def select_demo():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    # 定位百度首页设置-搜索设置中的“搜索结果显示条数”下拉列表选择框
    mouse = driver.find_element_by_link_text("设置")
    ActionChains(driver).move_to_element(mouse).perform()
    driver.find_element_by_link_text("搜索设置").click()
    select_nr = driver.find_element(By.ID, 'nr')

    # 创建select对象
    select = Select(select_nr)
    select.select_by_index(0)


if __name__ == '__main__':
    # send_keys_demo()
    select_demo()