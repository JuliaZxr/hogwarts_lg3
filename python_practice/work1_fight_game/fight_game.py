#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/4 23:00
# @Author  : Yuki

"""
题目：
一个多回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了

思路：
1、定义游戏的角色（我、敌人）的血量和攻击力；并设置初始值
2、定义方法fight，游戏规则：
    角色血量=初始血量-对方攻击力
    每一轮攻击完成后，进行比较，判断是否有角色血量为0【比较是循环的，使用while（true）,恒成立】
    如果有角色血量为0，则break输出对应结果
"""
# 定义初始血量 1000
hp = 1000

# 定义敌人初始血量 800
enemy_hp = 800

# 定义我的攻击力 200
my_power = 200

# 定义敌人的攻击力 200
enemy_power = 200


def fight():
    # 初始化回合数
    fight_round = 1

    # 先给我和敌人初始化血量
    my_hp = hp
    enemy_final_hp = enemy_hp

    while True:
        # 计算我的剩余血量，并输出
        my_hp = my_hp - enemy_power
        print("第", fight_round, "轮后，我的剩余血量是：", my_hp)

        # 计算敌人的剩余血量，并输出
        enemy_final_hp = enemy_final_hp - my_power
        print("第", fight_round, "轮后，敌人的剩余血量是：", enemy_final_hp)

        # 计算回合数
        fight_round = fight_round + 1

        # 本回合打架完之后， 看谁死了哈哈哈
        if my_hp <= 0:
            print("我输了!")
            break
        elif enemy_final_hp <= 0:
            print("敌人输了！")
            break


# 调用函数
fight()
