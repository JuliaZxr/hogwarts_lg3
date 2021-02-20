#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/28 22:06
# @Author  : Yuki
import json

import requests


class BaseApi:

    """
    api抽象类
    """
    def send_api(self, **keyword):
        """
        发送 api
        """
        # json.dumps()用于将字典形式的数据转化为字符串，json.loads()用于将字符串形式的数据转化为字典
        # dumps()的indent参数-->自动缩进，默认为None, 修改为一定的数值即可
        print(json.dumps(keyword, indent=2))
        return requests.request(**keyword).json()