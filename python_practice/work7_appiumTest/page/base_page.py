#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 23:32
# @Author  : Yuki


"""
基类：用来存放一些最常用的方法
    1、接收driver
    2、查找元素方法
    3、打印日志：一般都是在基类中进行
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    # 打印日志
    logging.basicConfig(level=logging.INFO)

    # driver: WebDriver是给driver定义成WebDriver类型
    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    # 提取公共查找元素方法
    def findByXpath(self, xpathSelector):
        logging.info("通过xpath查找元素")
        logging.info(xpathSelector)
        classEle = self.driver.find_element(MobileBy.XPATH, xpathSelector)
        return classEle

    def findElementsByClass(self, classSelector):
        logging.info("通过CSS_SELECTOR查找多个元素")
        logging.info(classSelector)
        classEles = self.driver.find_elements(MobileBy.CSS_SELECTOR, classSelector)
        return classEles

    def findById(self, idSelector):
        logging.info("通过Id查找元素")
        logging.info(idSelector)
        idEle = self.driver.find_element(MobileBy.ID, idSelector)
        return idEle

    def get_toast(self):
        logging.info("获取toast信息")
        text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(text)
        return text
