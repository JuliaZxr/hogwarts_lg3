#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/20 11:51
# @Author  : Yuki


class TongLao:
    def __init__(self, hp, mp):
        # hp:血量
        self.hp = hp
        # mp：法力
        self.mp = mp

    def see_people(self, name):
        if name == "无崖子":
            print("师弟！！！！")
        elif name == "李秋水":
            print("呸，贱人！")
        elif name == "丁春秋":
            print("叛徒！我杀了你！")
        else:
            print("来者何人？？!!!")

    def fight_zms(self, enemy_hp, enemy_mp):
        self.hp = self.hp / 2 - enemy_mp
        self.mp = self.mp * 10
        enemy_hp = enemy_hp - self.mp
        if self.hp > enemy_hp:
            print("废物！连我这个老太婆都伤不了!")
        elif self.hp < enemy_hp:
            print("无耻小人！")
        else:
            print("虚竹,给我上!!")


t1 = TongLao(1000, 10)
t1.see_people("李秋水")
t1.see_people("无崖子")
t1.see_people("丁春秋")
t1.see_people("yuki")
print()

t1.fight_zms(500, 100)
t2 = TongLao(1000, 10)
t2.fight_zms(600, 100)
t3 = TongLao(1000, 10)
t2.fight_zms(400, 100)
print()