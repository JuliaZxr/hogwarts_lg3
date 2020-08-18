#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/18 23:27
# @Author  : Yuki

import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

"""
1、要先获取到企业微信的cookie
    -采用复用已有浏览器的方式（只能使用chrome，window先把chrome快捷方式地址配置到path环境变量，关闭所有chrome浏览器页面，命令行执行chrome --remote-debugging-port=9222）
    -在打开的chrome浏览器中登录企业微信后台管理账号

    -在setup方法中，设置调试器地址 (debugger_address)，设置的端口号与命令行执行的一致，引用option时要注意引用chrome的，代码语句如下：
        option = Options()
        option.debugger_address = "localhost:9222"

    -在实例化driver对象时，注意此处是chrome的，然后参数方法要使用options=，代码语句如下：
        self.driver = webdriver.Chrome(options=option)

2、在test_cookie方法中，要先去获取cookie，使用driver.get_cookies方法，并在控制台输出以便使用，代码语句如下：
    cookies = self.driver.get_cookies()
    print(cookies)

3、然后执行test_cookie方法，获取到cookies，在控制台复制并赋值给自定义变量cookies

4、此时已获取到cookies，则实例化driver时，不再需要复用浏览器cookie，即把实例化中参数删去；并且不需要重复获取和输出cookies，即注释掉2、中的代码

5、使用for循环和driver.add_cookie方法将cookie添加，用以完成登录验证(添加cookie如果遇到浮点型的参数，运行会报错，这种情况，可以去做处理，在for循环中添加if判断，通过对应key值判断，pop删除这个值)

6、然后就可以进行登陆后的操作验证等
"""


class TestCookie():
    def setup(self):
        option = Options()
        option.debugger_address = "localhost:9222"

        # self.driver = webdriver.Chrome(options=option)

        # 实例化driver
        self.driver = webdriver.Chrome()
        # 窗口最大化
        self.driver.maximize_window()
        # 设置隐式等待，使用后无需在方法中每句代码后再去添加sleep()方法；而是自行每步等待5s，使之可以有时间找到元素继续测试，避免网速慢等原因导致元素未被加载，从而导致用例执行失败
        self.driver.implicitly_wait(5)

    def teardown(self):
        # 回收driver
        self.driver.quit()

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # print(cookies)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

        cookies = [
            {'domain': '.qq.com', 'expiry': 1597760910, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
             'value': 'zCJN9bj5hIEp-ge_9OmsVA5P9H'
                      '-hQmUyMKLijXcDOAEu1FvTsIzkgSAmntWAPT7x4vHeDKS6LyLvX2DPI7aQVtpN_drbT9YQq00DdCJLPa9hBbX0Uo1xHmPXlknpEFwOp7J1KHmJEXefolxR-tulXHpWitKgjzasZdwSS7Gw1JbMhVAIVDZDgtPZs8cnqGB8mkskz_muHNN-FHTc7zQMVIlFrUct8Y_jEw3-K0BbwqS_3LK61KqZibEmBmYYn_KDJD_mdptWJY0bnbVkz2PQlQ'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
             'value': 'T_h16DFd3taFuy_PCBcZvkVPTOZTMKmBX0BvJxtm5CpO8R0zxorZ7Ip9DczE9h7v'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
             'value': 'a6733667'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
             'value': '1688850230607478'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
             'value': '1970325104156516'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
             'value': '1688850230607478'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
             'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'expiry': 1629293008, 'httpOnly': False,
                                  'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False,
                                  'value': '1597755312'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
             'value': '1'},
            {'domain': 'work.weixin.qq.com', 'expiry': 1597786847, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/',
             'secure': False, 'value': '1c2o3ge'},
            {'domain': '.qq.com', 'expiry': 1597847250, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False,
             'value': 'GA1.2.825355124.1597755314'},
            {'domain': '.qq.com', 'expiry': 1660832850, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False,
             'value': 'GA1.2.14811911.1597755314'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1629291311, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
             'path': '/', 'secure': False, 'value': '0'},
            {'domain': '.work.weixin.qq.com', 'expiry': 1600352851, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
             'path': '/', 'secure': False, 'value': 'zh-cn'},
            {'domain': '.qq.com', 'expiry': 2147483649, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False,
             'value': 'd373084511cd8612f34fde516358e5bcdd50498b75a3482ba303f64f4df27707'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
             'path': '/', 'secure': False, 'value': '1597757008'},
            {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
             'value': '03310121'},
            {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False,
             'value': 'GDbFsZgHYi'}]

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传文件使用元素.send_keys方法，window的路径粘贴过来需要把\换成/
        self.driver.find_element(By.ID, "js_upload_file_input").send_keys("F:/Study/Document/myDatasDemo.xlsx")
        # 添加断言，通过元素.text 去验证上传后的文件名称是否一致
        myfileName = self.driver.find_element(By.ID, "upload_file_name").text
        assert "myDatasDemo.xlsx" == myfileName
