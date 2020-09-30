#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 22:31
# @Author  : Yuki
import requests

from python_practice.work11_apiTestFrameworkRequest.api_page.base_api import BaseApi

"""
页面中共用的，且不属于页面中的方法，写到utils类中，避免写到基类中，增加基类的冗余
"""


class WechatUtils(BaseApi):
    """
    每个页面的corpsecret值都不一致，所以corpsecret需要传参，corpid则是这个app中的定值，所以直接赋值
    """

    def getToken(self, corpsecret, corpid="wweb26819d4d011560"):
        data = {
            "method": "get",
            "url": f"https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            "params": {
                "corpid": corpid,
                "corpsecret": corpsecret
            }
        }
        return self.send_api(**data)["access_token"]