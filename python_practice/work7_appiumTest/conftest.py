#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 21:34
# @Author  : Yuki


from typing import List


# 中文编码
def pytest_collection_modifyitems(
        session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
