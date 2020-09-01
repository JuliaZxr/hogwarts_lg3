#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 22:19
# @Author  : Yuki
from appium.webdriver.common.mobileby import MobileBy

from python_practice.work7_appiumTest.page.addMembersManually_page import AddMembersManuallyPage
from python_practice.work7_appiumTest.page.base_page import BasePage


class InviteMembersPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    # 方法：邀请成员页面跳转手动添加成员页面
    def goto_addMembersManuallyPage(self):
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        self.findByXpath("//*[@text='手动输入添加']").click()
        return AddMembersManuallyPage(self.driver)


