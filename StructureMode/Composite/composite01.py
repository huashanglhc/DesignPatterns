#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：composite01.py
@Author  ：WL
@Date    ：2022/6/10 11:22 
@Describe: 组合模式

内容：江对象组合成树形结构以表示“部分-整体”的层次结构。组合模式使得用户对单个对象和组合对象的使用具有一致性

角色：
    抽象组件
    叶子组件
    复合组件


应用场景：
    表示对象的"整体-部分"层次结构(特别是结构式递归的)
    希望用户忽略组合对象与单一对象的不同，用户统一地使用组合结构中所有对象

优点：
    定义了包含基本对象和组合对象的类层次结构
    简化客户端代码，即客户端可以一致地使用组合对象和单个对象
    更容易增加新类型组件
"""

from abc import ABCMeta, abstractmethod


# 抽象组件
class Graphic(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass


# 叶子组件
class Point(Graphic):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "点坐标(%s,%s)" % (self.x, self.y)

    def draw(self):
        print(str(self))


# 叶子组件
class Line(Graphic):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return "线段[%s,%s]" % (self.p1, self.p2)

    def draw(self):
        print(str(self))


# 复合组件
class Picture(Graphic):
    def __init__(self, iterable):
        self.children = []
        for g in iterable:
            self.add(g)

    def add(self, graphic):
        self.children.append(graphic)

    def draw(self):
        print("============复合图像===========")
        for g in self.children:
            g.draw()
        print("============复合图像===========")


# 客户端
point = Point(1, 3)
l1 = Line(Point(2, 2), Point(6, 8))
l2 = Line(Point(5, 2), Point(8, 9))
pic1 = Picture([point, l1, l2])
print("point", point)
print("l1", l1)
print("l2", l2)
pic1.draw()

point2 = Point(4, 3)
l2 = Line(Point(4, 2), Point(5, 6))
l3 = Line(Point(1, 6), Point(2, 8))
pic2 = Picture([point2, l2, l3])
pic2.draw()

pic = Picture([pic1, pic2])
pic.draw()
