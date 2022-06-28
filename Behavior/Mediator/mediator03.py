#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：mediator03.py
@Author  ：WL
@Date    ：2022/6/28 11:53 
@Describe: 中介者模式

应用场景：各对象已定义良好，但是对象间有复杂的通讯
"""

from abc import ABCMeta, abstractmethod


class Unit(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def declare(self, count, message):
        pass


class Nations(Unit):
    def __init__(self):
        super(Nations, self).__init__()
        self._china = None
        self._american = None

    def set_china(self, china):
        self._china = china

    def set_american(self, american):
        self._american = american

    def declare(self, country, message):
        if self._china.name == country.name:
            self._american.get_message(message)
        elif self._american.name == country.name:
            self._china.get_message(message)


class Country(object):
    __metaclass__ = ABCMeta

    def __init__(self, name, nations):
        self.nations = nations
        self.name = name
        pass

    @abstractmethod
    def declare(self, message):
        pass

    @abstractmethod
    def get_message(self, msg):
        pass


class China(Country):
    def __init__(self, name, nations):
        super(China, self).__init__(name, nations)

    def declare(self, message):
        self.nations.declare(self, message)

    def get_message(self, msg):
        print(msg)


class American(Country):
    def __init__(self, name, nations):
        super(American, self).__init__(name, nations)

    def declare(self, message):
        self.nations.declare(self, message)

    def get_message(self, msg):
        print(msg)


if __name__ == '__main__':
    nations = Nations()
    china = China("中国", nations)
    american = American("美国", nations)
    nations.set_china(china)
    nations.set_american(american)

    china.declare("美国你给我注意点，我要打你了")
    print("")
    american.declare("打死我吧")
