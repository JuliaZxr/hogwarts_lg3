#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/24 23:18
# @Author  : Yuki
import requests

corpid = "wweb26819d4d011560"
corpsecret = "9pHQAev8cSagX0UqNKIKpH53m_aaS1zjF04kcpDPkOI"


def getToken():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
    result = requests.get(url).json()
    # print(result["access_token"])
    return result["access_token"]


def test_getDep():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={getToken()}&id=1"
    r = requests.get(url).json()
    print(r)
    assert r["errmsg"] == "ok"


def test_createDep():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={getToken()}"
    depData = {
        "name": "测试一部",
        "name_en": "CSYB",
        "parentid": 2,
        "order": 2,
        "id": 3
    }
    r = requests.post(url, json=depData).json()
    print(r)
    assert r["errmsg"] == "created"


def test_updateDep():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={getToken()}"
    depData = {
        "id": 3,
        "name": "测试二部",
        "name_en": "CSEB",
        "parentid": 2,
        "order": 2
    }
    r = requests.post(url, json=depData).json()
    print(r)
    assert r["errmsg"] == "updated"


def test_delDep():
    url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={getToken()}&id=3"
    r = requests.get(url).json()
    print(r)
    assert r["errmsg"] == "deleted"