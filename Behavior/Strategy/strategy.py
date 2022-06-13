#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：strategy.py
@Author  ：WL
@Date    ：2022/6/13 14:49 
@Describe: 策略模式

策略模式：定义一系列算法，把它们一个个封装起来，并且使它们可以相互替换。

角色：
    抽象策略（Strategy）
    具体决策（Concrete Strategy）
    上下文（Context）

优点：
    定义了一系列可重用的算法和行为
    消除了一些条件语句
    可以提供相同行为的不同实现

缺点：
    客户必须了解不同的策略

"""
from abc import ABCMeta, abstractmethod


# 抽象策略
class AbstractStrategy(metaclass=ABCMeta):
    @abstractmethod
    def handle(self, data):
        pass


# 具体决策
class FastStrategy(AbstractStrategy):
    def handle(self, data):
        print(f"使用较快的策略处理数据：{data}")


class SlowStrategy(AbstractStrategy):
    def handle(self, data):
        print(f"使用较慢的策略处理数据：{data}")


# 上下文(封装数据和策略)
class Context:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.handle(self.data)


# Client
data_obj = [1, 3, 9, 100, 85, 66, 77, 33, 22]
s = SlowStrategy()
s2 = FastStrategy()
c = Context(s, data_obj)
c.do_strategy()

c.set_strategy(s2)
c.do_strategy()
