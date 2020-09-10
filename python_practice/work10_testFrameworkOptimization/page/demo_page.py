#!/usr/bin/env pytho
# -*- coding: utf-8 -*-


"""
DemoPage是定义个一个需要测试的页面，继承与基类BasePage
在这个类中，定义这个页面需要的一个方法，eg.登录，忘记密码等

search()方法实现后，再使用po的数据驱动去实现，将search需要的步骤写到yaml文件中，
再在demo_page.py中去读取page_demo.yml数据
"""
from python_practice.work10_testFrameworkOptimization.page.base_page import BasePage


class DemoPage(BasePage):
    # _search_button = (By.ID, "com.xueqiu.android:id/home_search")

    # TODO：PO的数据驱动
    # 定义的登录方法，需要两个参数：username, password
    def loginIn(self, username, password):
        pass

    def forget_pwd(self):
        pass

    def back(self):
        self.po_runSteps("back")
        return self

    # 定义的搜索方法，需要一个参数：keyword
    def search(self, keyword2):
        # # 普通的search方法实现
        # self.find(self._search_button).click()

        # 通过po数据驱动实现
        self.po_runSteps("search", keyword=keyword2)
        return self
