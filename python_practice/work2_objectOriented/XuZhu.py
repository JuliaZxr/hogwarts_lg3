#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 11:53
# @Author  : Yuki
from python_practice.work2_objectOriented.TongLao import TongLao


class XuZhu(TongLao):
    def __init__(self):
        super().__init__(100, 1)

    def read(self):
        print("罪过罪过！阿弥陀佛~")


xz = XuZhu()
xz.read()
xz.fight_zms(500, 50)
xz.see_people("momo")
