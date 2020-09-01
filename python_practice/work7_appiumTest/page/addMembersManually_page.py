#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 22:21
# @Author  : Yuki
"""
当两个页面需要相互引用时，全局引用-执行时会报错->因为会引起循环引用：
    需要局部引用以解决这个问题（快捷键：alt+enter）

手动添加成员addMembersByManual()方法需要三个必需参数：name，gender，tel -->在方法中传形参

"""
from python_practice.work7_appiumTest.page.base_page import BasePage


class AddMembersManuallyPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver

    # 方法：完成手动添加成员，提交保存后将跳转至上一级页面->邀请成员页面
    def addMembersByManual(self, name, gender, tel):
        # todo 手动添加成员
        # //*[contains(@text,'姓名')]/../android.widget.EditText -->text包含姓名的元素的父级，class=android.widget.EditText的元素
        # self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        self.findByXpath("//*[contains(@text,'姓名')]/../android.widget.EditText").send_keys(name)
        # self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        self.findByXpath("//*[@text='男']").click()
        if gender == '男':
            # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/e5c" and @text="男"]').click()
            self.findByXpath("//*[@resource-id='com.tencent.wework:id/e5c' and @text='男']").click()

        else:
            # self.driver.find_element(MobileBy.XPATH, '//*[@resource-id="com.tencent.wework:id/e5c" and @text="女"]').click()
            self.findByXpath("//*[@resource-id='com.tencent.wework:id/e5c' and @text='女']").click()

        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f9s").send_keys(tel)
        self.findById("com.tencent.wework:id/f9s").send_keys(tel)
        # self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hk6").click()
        self.findById("com.tencent.wework:id/hk6").click()

        from python_practice.work7_appiumTest.page.inviteMembers_page import InviteMembersPage
        return InviteMembersPage(self.driver)
