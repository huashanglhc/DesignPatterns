#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：chain.py
@Author  ：WL
@Date    ：2022/6/13 10:39 
@Describe: 责任链模式

责任链： 使多个对象都有机会处理请求，从而避免请求的发送者和接收者之间的耦合关系。将这些对象链成一条链，并沿着这条链传递
        该请求，直到有一个对象处理它为止。

角色：
    抽象处理者
    具体处理者
    客户端

应用场景：
    1. 有多个对象可以处理一个请求，哪个对象处理由运行时决定
    2. 在不明确接受者的情况下，向多个对象中的一个提交一个请求
优点：
    降低耦合：一个对象无需知道其他哪一个对象处理七请求

缺点：
    1. 如果责任链比较长，会有较大的性能问题
    2. 如果责任链比较长，若业务出现问题，比较难定位是哪个处理者的问题
"""
from abc import ABCMeta, abstractmethod


# 抽象处理者
class Handle(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass


# 具体处理者
class GeneralManager(Handle):
    def handle_leave(self, day):
        if day < 15:
            print("总经理准假%d天" % day)
        else:
            print("直接递交辞职报告吧！！！")


class DepartmentManager(Handle):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 5:
            print("部门经理准假%d天" % day)
        else:
            print("超出职权范围内，请假申请转交总经理处理")
            self.next.handle_leave(day)


class ProjectDirector(Handle):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print("项目经理准假%d天" % day)
        else:
            print("超出职权范围内，请假申请转交部门经理处理")
            self.next.handle_leave(day)


# 客户端
# d = 18
d = 2
# d = 5
h = ProjectDirector()
h.handle_leave(d)
