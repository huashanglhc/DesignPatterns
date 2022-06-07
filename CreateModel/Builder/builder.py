#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：builder.py
@Author  ：WL
@Date    ：2022/6/7 9:53 
@Describe: 建造者模式

角色：
    抽象建造者
    具体建造者
    指挥者
    产品

优点：
    影藏了一个产品的内部结构和装配过程
    将构造代码与表示代码分开
    可以对构造过程进行更精细的控制

缺点：


应用场景：

抽象工厂 VS 建造者


"""
from abc import ABCMeta, abstractmethod


# 产品
class Player:
    def __init__(self, body=None, arm=None, leg=None, face=None):
        self.body = body
        self.arm = arm
        self.leg = leg
        self.face = face

    def __str__(self):
        return "{0},{1},{2},{3}".format(self.face, self.body, self.arm, self.leg)


# 抽象建造者
class PlayBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass


# 具体建造者
class SexGirlBuilder(PlayBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "漂亮脸蛋"

    def build_body(self):
        self.player.body = "苗条身材"

    def build_leg(self):
        self.player.leg = "大长腿"

    def build_arm(self):
        self.player.arm = "修长胳膊"


class Monster(PlayBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "丑八怪"

    def build_body(self):
        self.player.body = "魁梧大汉"

    def build_leg(self):
        self.player.leg = "满腿毛"

    def build_arm(self):
        self.player.arm = "巨猿臂"


# 指挥者(控制组装顺序)
class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


# client
builder = SexGirlBuilder()
director = PlayerDirector()
p = director.build_player(builder)
print(p)
