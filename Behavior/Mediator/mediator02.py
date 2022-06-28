#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：mediator02.py
@Author  ：WL
@Date    ：2022/6/28 11:22 
@Describe: 中介者模式02

中介者模式： 用一个中介对象封装一系列的对象交互。中介者使各对象不需要显示地相互引用，从而使其耦合松散，而且可以独立地改变
            它们之间的关系。

角色介绍：
    抽象中介者：定义好同事类对象到中介者对象的接口，用于各个同事类之间的通信。一般包括一个或几个抽象的事件方法，
                并由子类去实现。

    中介者实现类：从抽象中介者继承而来，实现抽象中介者中定义的事件方法。从一个同事类接收消息，然后通过消息影响其他同时类。

    同事类：如果一个对象会影响其他的对象，同时也会被其他对象影响，那么这两个对象称为同事类。同事类只有一个，
            这其实是现实的省略，在实际应用中，同事类一般由多个组成，他们之间相互影响，相互依赖。同事类越多，
            关系越复杂。并且，同事类也可以表现为继承了同一个抽象类的一组实现组成。在中介者模式中，同事类之间必须通过中介者
            才能进行消息传递。


优点：降低各个模块的耦合性
缺点：中介对象容易变得复杂和庞大
"""
"""Mediator Pattern with Python Code
"""
from abc import ABCMeta, abstractmethod


class AbstractColleague(metaclass=ABCMeta):
    def __init__(self, number):
        self.number = number

    def get_number(self):
        return self.number

    def update_number(self, number):
        self.number = number

    @abstractmethod
    # am 为一个中介者
    def set_number(self, am, number):
        pass


class ColleagueA(AbstractColleague):
    def set_number(self, am, number):
        self.number = number
        am.affect_b()


class ColleagueB(AbstractColleague):
    def set_number(self, am, number):
        self.number = number
        am.affect_a()


class AbstractMediator(metaclass=ABCMeta):
    def __init__(self, a: AbstractColleague, b: AbstractColleague):
        self.A = a
        self.B = b

    @abstractmethod
    def affect_a(self):
        pass

    @abstractmethod
    def affect_b(self):
        pass


class Mediator(AbstractMediator):
    def __init__(self, a: AbstractColleague, b: AbstractColleague):
        AbstractMediator.__init__(self, a, b)

    # 处理A对B的影响
    def affect_b(self):
        number = self.A.get_number()
        self.B.update_number(number * 100)

    # 处理B对A的影响
    def affect_a(self):
        number = self.B.get_number()
        self.A.update_number(number / 100)


def main():
    coll_a = ColleagueA(0)
    coll_b = ColleagueB(0)

    am = Mediator(coll_a, coll_b)

    print("==========通过设置A影响B==========")
    coll_a.set_number(am, 1000)
    print("coll_a的number值为：%d" % coll_a.get_number())
    print("coll_b的number值为A的10倍：%d" % coll_b.get_number())

    print("==========通过设置B影响A==========")
    coll_b.set_number(am, 1000)
    print("coll_b的number值为：%d" % coll_b.get_number())
    print("coll_a的number值为B的0.1倍：%d" % coll_a.get_number())


if __name__ == "__main__":
    main()
