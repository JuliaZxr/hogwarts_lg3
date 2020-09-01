#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 22:07
# @Author  : Yuki

"""
MyApp类：
    含一些app常用的方法：
        1、启动app
        2、关闭app
        3、进入首页

"""
from appium import webdriver




from python_practice.work7_appiumTest.page.base_page import BasePage
from python_practice.work7_appiumTest.page.main_page import MainPage


class MyApp(BasePage):
    """
    当app启动后会进入首页，而startApp()和goto_mainPage()在同一个文件中，
    所以在startApp()后，需要停留在当前文件，则在startApp()中return self

    注意：
    不是每次进入app时都有能复用的driver，所以需要进行判断：
        如果driver已经被实例化存在，则进行复用
        否则，需要重新创建一个driver
    """
    def startApp(self):
        if self.driver is None:
            desire_cap = {
                "platformName": "android",
                "deviceName": "127.0.0.1:7555",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "noReset": "true"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
            self.driver.implicitly_wait(10)
        else:
            # 启动caps里设置的appPackage appActivity
            self.driver.launch_app()
            # 启动任意一个包中的appPackage appActivity
            # self.driver.start_activity()
        return self

    def stopApp(self):
        self.driver.quit()

    # 方法：进入首页
    def goto_mainPage(self):
        return MainPage(self.driver)


