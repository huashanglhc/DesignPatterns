#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：memo03.py
@Author  ：WL
@Date    ：2022/6/15 10:41 
@Describe:  备忘录
"""


class Hero:
    def __init__(self, attack, defense):
        self.attack = attack
        self.defense = defense

    def get_injured(self):
        self.attack = 50
        self.defense = 50
        print("英雄受伤了")

    def save_status(self):
        print("存档")
        return StatusMemento(self.attack, self.defense)

    def recover_status(self, status):
        print("恢复存档")
        self.attack = status.attack
        self.defense = status.defense

    def current_status(self):
        print(f"角色的当前状态为 攻击力：{self.attack}, 防御力：{self.defense}")


class StatusMemento:
    def __init__(self, attack, defense):
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f"存档：攻击力：{self.attack}, 防御力：{self.defense}"

    def __repr__(self):
        return f"攻击力：{self.attack}, 防御力：{self.defense}"


class Caretaker:
    statuses = {}
    num = 0

    @classmethod
    def add(cls, status):
        cls.num += 1
        print(f"存档增加状态 --- {status} ---")
        s = {cls.num: status}
        cls.statuses.update(s)

    @classmethod
    def current_statuses(cls):
        print(f"当前所有存档为 {cls.statuses}")


# 1. 新英雄登场，存档一次
hero = Hero(100, 100)
hero.current_status()
Caretaker.add(hero.save_status())

# 2. 英雄受伤了，存档一次
hero.get_injured()
hero.current_status()
Caretaker.add(hero.save_status())

# 3. 恢复存档
Caretaker.current_statuses()
hero.recover_status(Caretaker.statuses[1])      # 恢复到第一个存档
hero.current_status()

hero.recover_status(Caretaker.statuses[2])      # 恢复到第二个存档
hero.current_status()
