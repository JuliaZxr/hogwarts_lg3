#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 22:29
# @Author  : Yuki

"""
人员管理类：
    1、测试手动添加成员用例
    2、测试删除成员用例

思路：
    1、测试时需要启用app-->所以在setup()方法中需要实例化一个MyApp类，再去通过实例化的对象调用启动方法startApp()
    2、启动app后需要进入首页-->继续在setup()方法中实例化一个ManinPage类
    3、完成测试时需要关闭app-->通过setup()中实例化的对象调用关闭app方法stopApp()

    4、测试手动添加成员用例时需要进入手动添加页面

    5、测试用例使用参数化的方法传递
"""
import pytest
import yaml




# 从.yml文件中读取测试数据
from python_practice.work7_appiumTest.page.myApp import MyApp


def get_contactsData():
    with open("../datas/contacts.yml", encoding="utf-8") as f:
        datas = yaml.safe_load(f)
        add_members = datas["addMem"]
        del_members = datas["delMem"]
    return [add_members, del_members]


class TestMemberManage:
    def setup(self):
        self.app = MyApp()
        self.app.startApp()
        # self.mainPage = MainPage()

    def teardown(self):
        self.app.stopApp()

    @pytest.mark.parametrize("name, gender, tel", get_contactsData()[0])
    def test_addMemberByManual(self, name, gender, tel):
        """
            1、打开首页
            2、跳转通讯录页面
            3、跳转邀请人员页面
            4、跳转手动添加人员页面
            5、手动添加人员
            6、断言：弹出toast提示->添加成功
        """
        # 打开首页
        mainPage = self.app.goto_mainPage()

        # 跳转通讯录页面
        contactPage = mainPage.goto_contactPage()

        # 跳转邀请人员页面
        inviteMembersPage = contactPage.goto_inviteMembersPage()

        # 跳转手动添加人员页面
        addMembersManuallyPage = inviteMembersPage.goto_addMembersManuallyPage()

        # 手动添加人员
        addMembersByManual = addMembersManuallyPage.addMembersByManual(name, gender, tel)

        # 断言：弹出toast提示->添加成功
        toastText = addMembersByManual.get_toast()
        assert '添加成功' == toastText

    @pytest.mark.parametrize("name", get_contactsData()[1])
    def test_delMember(self, name):
        """
            1、打开首页
            2、跳转通讯录页面
            3、跳转个人信息页面
            4、跳转个人信息更多操作页面
            5、跳转个人信息编辑页面
            6、完成个人信息编辑后保存返回通讯录页面
            7、断言：搜索不存在被删除人员
        """
        # 打开首页
        mainPage = self.app.goto_mainPage()

        # 跳转通讯录页面
        contactPage = mainPage.goto_contactPage()

        # 跳转个人信息页面
        memberInfoPage = contactPage.goto_memberInfotmationPage(name)

        # 跳转个人信息更多操作页面
        memberInfoMorePage = memberInfoPage.goto_memberInfoMorePage()

        # 跳转个人信息编辑页面
        memberInfoEdit = memberInfoMorePage.goto_memberInfoEditPage()

        # 完成个人信息编辑后保存返回通讯录页面
        delRetuenContactPage = memberInfoEdit.editMemberInfo()

        # 断言：搜索不存在已经被删除人员
        searchResult = delRetuenContactPage.searchNoMember(name)
        assert "无搜索结果" == searchResult
