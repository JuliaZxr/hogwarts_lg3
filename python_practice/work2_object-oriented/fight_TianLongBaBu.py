#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/10 22:44
# @Author  : Yuki

"""
定义一个天山童姥类 ，类名为TongLao，属性有血量hp，武力值mp（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”

fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""


class TongLao:
    def __init__(self, hp, mp):
        # hp:血量
        self.hp = hp
        # mp：法力
        self.mp = mp

    def see_people(self, name):
        if name == "无崖子":
            print("师弟！！！！")
            xuzhu = XuZhu()
            xuzhu.read()
        elif name == "李秋水":
            print("呸，贱人！")
            self.fight_zms(800, 80)
            xuzhu = XuZhu()
            xuzhu.read()
        elif name == "丁春秋":
            print("叛徒！我杀了你！")
            self.fight_zms(200, 20)
            xuzhu = XuZhu()
            xuzhu.read()
        else:
            print("来者何人？？!!!")

    def fight_zms(self, enemy_hp, enemy_mp):
        self.hp = self.hp / 2 - enemy_mp
        self.mp = self.mp * 10
        enemy_hp = enemy_hp - self.mp
        if self.hp > enemy_hp:
            print("废物！连我这个老太婆都伤不了!(附图：洪世贤-你好sao啊.jpg)")
        elif self.hp < enemy_hp:
            print("无耻小人！(附图：周星驰吐血.jpg)")
        else:
            print("虚竹,给我上!!")


class XuZhu(TongLao):
    def __init__(self):
        super().__init__(100, 1)

    def read(self):
        print("罪过罪过！阿弥陀佛~\n")


tonglao = TongLao(1000, 10)
tonglao.see_people("李秋水")
tonglao.see_people("无崖子")
tonglao.see_people("丁春秋")
