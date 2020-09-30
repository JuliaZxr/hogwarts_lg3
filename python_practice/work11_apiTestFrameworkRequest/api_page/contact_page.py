#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 22:05
# @Author  : Yuki
import requests

from python_practice.work11_apiTestFrameworkRequest.api_page.base_api import BaseApi
from python_practice.work11_apiTestFrameworkRequest.api_page.wechat_utils import WechatUtils


class ContactPage(BaseApi):
    """
    通讯录页面 包括：增删改查
    """

    def __init__(self):
        """
        每个页面的corpsecret值都不一致，所以将corpsecret赋值写在页面的构造函数中

        """
        _corpsecret = "9pHQAev8cSagX0UqNKIKpH53m_aaS1zjF04kcpDPkOI"
        self.utils = WechatUtils()
        self.token = self.utils.getToken(_corpsecret)

    def get_dep(self):

        data = {
            "method" : "get",
            "url" : f"https://qyapi.weixin.qq.com/cgi-bin/department/list",
            "params" : {
                "access_token" : self.token,
                "id" : "1"
            }
        }
        return self.send_api(**data)

    def add_dep(self):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/create",
            "params": {
                "access_token": self.token
            },
            "json" : {
                "name": "测试一部",
                "name_en": "CSYB",
                "parentid": 2,
                "order": 2,
                "id": 3
             }
        }
        return self.send_api(**data)

    def update_dep(self):
        data = {
            "method": "post",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/update",
            "params": {
                "access_token": self.token
            },
            "json": {
                "id": 3,
                "name": "测试二部",
                "name_en": "CSEB",
                "parentid": 2,
                "order": 2
            }
        }
        return self.send_api(**data)

    def delete_dep(self):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/department/delete",
            "params": {
                "access_token": self.token,
                "id": "3"
            }
        }
        return self.send_api(**data)