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

xz = XuZhu()  # 因为xuzhu类引用了tonglao类，所以在子类实例化之前就会解析执行父类的代码
xz.read()
xz.fight_zms(500, 50)
xz.see_people("momo")
