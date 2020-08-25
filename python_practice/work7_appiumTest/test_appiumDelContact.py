#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/25 22:43
# @Author  : Yuki

"""
不应该每一步操作都去断言，只检查重要的步骤即可
"""

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestAppiumWechat:
    def setup(self):
        desire_cap = {
            "platformName": "android",
            "deviceName": "127.0.0.1:7555",
            "appPackage": "com.tencent.wework",
            "appActivity": ".launch.LaunchSplashActivity",
            "noReset": "true"
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desire_cap)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_addContact(self):
        name = "Momo"
        gender = '女'
        tel = "15511112223"

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # //*[contains(@text,'姓名')]/../android.widget.EditText -->text包含姓名的元素的父级，class=android.widget.EditText的元素
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f9s").send_keys(tel)
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk6").click()
        # toast 弹框,打印当前页面的布局结构 ，xml结构，每个页面都有个toast类,class名称是android.widget.Toast
        # sleep(2)
        # print(self.driver.page_source)
        toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        assert '添加成功' == toasttext

    def test_deleteContact(self):
        name = "Momo"

        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='Momo']").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hjz").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b53").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e_1").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bfe").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk9").click()
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/g75").send_keys(name)
        searchResult = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c5m").text
        assert "无搜索结果" == searchResult
