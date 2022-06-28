#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：observer02.py
@Author  ：WL
@Date    ：2022/6/13 12:19 
@Describe: 观察者

创建型模式基于对象的创建机制，隔离了对象的创建细节，使代码能够与要创建的对象的类型相互独立
结构型模式用于设计对象和类的结构，使它们可以相互协作以获得更大的结构
行为型模式主要关注对象的责任，用来处理对象之间的交互，以实现更大的功能


"""
from abc import ABC
from queue import Queue


class Subject(ABC):

    def __init__(self):
        self.observers = list()

    def add_observer(self, observer):
        self.observers.append(observer)

    def pop_observer(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


class GameSubject(Subject):

    def notify(self, msg):
        for observer in self.observers:
            observer.update(msg)


class Observer:
    def __init__(self):
        self.queue = Queue(100)

    def update(self):
        pass


class LolObserver(Observer):

    def __init__(self, name):
        self.name = name
        super().__init__()

    def update(self, msg):
        self.queue.put(msg)

    def get_msg(self):
        while not self.queue.empty():
            msg = self.queue.get()
            print(self.name + "正在读取消息：" + msg)


class DNFObserver(Observer):

    def __init__(self, name):
        self.name = name
        super().__init__()

    def update(self, msg):
        self.queue.put(msg)

    def get_msg(self):
        while not self.queue.empty():
            msg = self.queue.get()
            print(self.name + "正在读取消息：" + msg)


if __name__ == "__main__":
    game_subject = GameSubject()
    lol_observer = LolObserver('lol选手')
    dnf_observer = DNFObserver("DNF选手")
    game_subject.add_observer(lol_observer)
    game_subject.add_observer(dnf_observer)
    game_subject.notify("第一届游戏大赛正在开始")
    game_subject.notify("我们友情两大游戏金牌选手")
    game_subject.notify("谁会是第一名呢？")
    game_subject.pop_observer(dnf_observer)
    game_subject.notify("会是LOL选手吗？")
    game_subject.notify("貌似DNF选手掉线了啊")
    game_subject.add_observer(dnf_observer)
    game_subject.notify("我们的选手又回来了")
    lol_observer.get_msg()
    print("=" * 77)
    dnf_observer.get_msg()
