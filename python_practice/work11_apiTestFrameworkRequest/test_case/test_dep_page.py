#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 22:22
# @Author  : Yuki
from python_practice.work11_apiTestFrameworkRequest.api_page.contact_page import ContactPage


class TestContactPage:
    def setup_class(self):
        # 初始化通讯录页面对象
        self.contact_page = ContactPage()

    def test_getDep(self):
        result = self.contact_page.get_dep()
        print(result)
        assert result["errcode"] == 0

    def test_addDep(self):
        result = self.contact_page.add_dep()
        print(result)
        assert result["errcode"] in [0, 60008]

    def test_updateDep(self):
        result = self.contact_page.update_dep()
        print(result)
        assert result["errcode"] in [0, 60003]

    def test_delDep(self):
        result = self.contact_page.delete_dep()
        print(result)
        assert result["errcode"] in [0, 60123]
