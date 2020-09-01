#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 22:13
# @Author  : Yuki
from appium.webdriver.common.mobileby import MobileBy

from python_practice.work7_appiumTest.page.base_page import BasePage
from python_practice.work7_appiumTest.page.contact_page import ContactPage

"""
执行报错：'MainPage' object has no attribute 'driver'
因为每个页面都需要一个driver驱动，这个驱动我们在MyApp类的startApp()方法中已经实例化了一个driver，现在需要传递到这个页面中-->
通过MyApp类的goto_mainPage()方法return MainPage(self.driver)进行页面间driver的传递

传递到此页面需要一个构造方法来接收driver 并进行实例化

思考：
    现在我们每个页面都通过构造方法来实例化driver，实际上这个是重复的内容-->所以我们需要创建一个页面基类BasePage来共用多次重复的方法
    创建好基类BasePage以及构造方法初始化driver后，我们将所有需要使用driver的页面构造方法注释，通过继承BasePage来获取driver
    
    查找元素也是重复方法，提取到基类中
"""


class MainPage(BasePage):
    # 接收driver
    # def __init__(self, driver):
    #     self.driver = driver

    # 方法：首页跳转通讯录页面
    def goto_contactPage(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.findByXpath("//*[@text='通讯录']").click()
        return ContactPage(self.driver)
