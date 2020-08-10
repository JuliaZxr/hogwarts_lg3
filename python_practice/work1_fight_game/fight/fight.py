#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 23:33
# @Author  : Yuki


class Game():
    # 构造函数
    def __init__(self, my_hp, my_power, enemy_hp, enemy_power):
        self.my_hp = my_hp
        self.my_power = my_power
        self.enemy_hp = enemy_hp
        self.enemy_power = enemy_power

    def fight(self):
        # 初始化回合数
        fight_round = 1

        while True:
            # 计算我的剩余血量，并输出
            self.my_hp = self.my_hp - self.enemy_power
            print("第", fight_round, "轮后，我的剩余血量是：", self.my_hp)

            # 计算敌人的剩余血量，并输出
            self.enemy_hp = self.enemy_hp - self.my_power
            print("第", fight_round, "轮后，敌人的剩余血量是：", self.enemy_hp)

            # 计算回合数
            fight_round = fight_round + 1

            # 本回合打架完之后， 看谁死了哈哈哈
            if self.my_hp <= 0:
                print("我输了!")
                break
            elif self.enemy_hp <= 0:
                print("敌人输了！")
                break


game = Game(2000, 200, 1500, 300)
game.fight()

