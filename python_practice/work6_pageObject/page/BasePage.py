#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 19:28
# @Author  : Yuki


"""
BasePage：页面类，供其他页面继承。
    -

"""
from selenium.webdriver.common.by import By


class BasePage:
    # 浏览器驱动
    driver = None
    # 浏览器地址
    url = ""

    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

    # 提取公共查找元素方法
    def findByClass(self, classSelector):
        classEle = self.driver.find_element(By.CSS_SELECTOR, classSelector)
        return classEle

    def findElementsByClass(self, classSelector):
        classEles = self.driver.find_elements(By.CSS_SELECTOR, classSelector)
        return classEles

    def findById(self, idSelector):
        idEle = self.driver.find_element(By.ID, idSelector)
        return idEle
