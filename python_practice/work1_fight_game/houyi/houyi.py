#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/8 23:33
# @Author  : Yuki
from python_practice.work1_fight_game.fight_game_optimization import Game


class Houyi(Game):

    # 如果重名的话，子类的属性会覆盖掉父类的属性
    def __init__(self, defense):
        self.defense = defense
        # 用super（）来调用父类的构造方法
        super().__init__(2000, 200, 1500, 300)

    def Houyi_fight(self):
        fight_round = 1
        while True:

            self.my_hp = self.my_hp + self.defense - self.enemy_power
            print("第", fight_round, "轮后，我的剩余血量是：", self.my_hp)
            self.enemy_hp = self.enemy_hp - self.my_power
            print("第", fight_round, "轮后，敌人的剩余血量是：", self.enemy_hp)

            # 计算回合数
            fight_round = fight_round + 1

            if self.my_hp <= 0:
                print("我输了!")
                break
            elif self.enemy_hp <= 0:
                print("敌人输了！")
                break


# game = Game(2000, 200, 1500, 300)
# game.fight()

houyi_fight = Houyi(100)
houyi_fight.Houyi_fight()
