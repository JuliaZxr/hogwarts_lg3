#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
from python_practice.work10_testFrameworkOptimization.page.base_page import BasePage


class LoginPage(BasePage):
    # 通过手机号及密码登录 --> 需要传参username，password
    def login_by_password(self, username, password):
        self.po_runSteps("login_by_password", username = username, password = password)
