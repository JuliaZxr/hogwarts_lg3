#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/1 0:22
# @Author  : Yuki
from python_practice.work7_appiumTest.page.base_page import BasePage


class MemberInfoPage(BasePage):
    # 跳转个人信息更多操作页面
    def goto_memberInfoMorePage(self):

        self.findById("com.tencent.wework:id/hjz").click()
        from python_practice.work7_appiumTest.page.memberInfoMore_page import MemberInfoMorePage
        return MemberInfoMorePage(self.driver)