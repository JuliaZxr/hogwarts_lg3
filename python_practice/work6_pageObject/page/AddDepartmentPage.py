#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 21:09
# @Author  : Yuki
from python_practice.work6_pageObject.page.BasePage import BasePage


class AddDepartmentPage(BasePage):
    def addDepartment(self, deptName):
        self.findByClass("input.qui_inputText.ww_inputText[name='name']").send_keys(deptName)
        self.findByClass(".qui_btn.ww_btn.ww_btn_Dropdown.js_toggle_party_list").click()
        self.findByClass(".js_party_list_container .jstree-anchor").click()
        self.findByClass(".ww_btn[d_ck='submit']").click()
