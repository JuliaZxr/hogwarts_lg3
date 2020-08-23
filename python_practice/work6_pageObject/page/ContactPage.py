#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 20:32
# @Author  : Yuki
from python_practice.work6_pageObject.page.AddDepartmentPage import AddDepartmentPage
from python_practice.work6_pageObject.page.BasePage import BasePage


class ContactPage(BasePage):
    def goto_addDepartment(self):
        # Todo 跳转添加部门页面
        self.findByClass(".member_colLeft_top_addBtn").click()
        # self.driver.find_element(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.findByClass(".js_create_party").click()
        return AddDepartmentPage(self.driver)

    def find_deptByName(self, deptName):
        eles = self.findElementsByClass(".jstree-anchor")
        # 用循环把返回列表中的值都取出来存到定义的空列表中
        for ele in eles:
            if deptName == ele.text:
                return deptName

        return ""

