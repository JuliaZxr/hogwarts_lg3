#!/usr/bin/env pytho
# -*- coding: utf-8 -*-
"""
登录的测试用例：
    首先需要一个setup方法，去实例化login_page页面
    存在登录测试方法：test_login（其中需要用户名、密码参数）
        则test_login方法需要数据驱动(通过pytest.mark.parametrize)


"""
import pytest

from python_practice.work10_testFrameworkOptimization.page.base_page import BasePage
from python_practice.work10_testFrameworkOptimization.page.common_page import CommonPage
from python_practice.work10_testFrameworkOptimization.utils.file_util import FileUtil


class TestDemo:
    testdata_file_search = "../datas/test_search.yml"
    po_file = "../datas/page_search.yml"

    data = FileUtil.from_file(testdata_file_search)

    def setup_class(self):
        # 启动app
        self.app = BasePage()
        self.app.start()

    def teardown_class(self):
        self.app.stop()

    # 用common_page代替demo_page
    @pytest.mark.parametrize(data["keys"], data["values"])
    def test_search_common_page(self, keyword1):
        demo = CommonPage(self.po_file)
        demo.search(keyword3=keyword1)
        demo.back()

    def test_loginByPassword(self):
        # 定义login_page的po_file文件路径
        po_file = "../datas/page_login.yml"
        # 初始化一个login页面，并传参对应的测试步骤po_file文件路径
        login = CommonPage(po_file)
        # 调用login页面的login_by_password方法，并完成传参
        login.login_by_password(username = "13322226666", password = "111111")