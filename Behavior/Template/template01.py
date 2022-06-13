#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：template01.py
@Author  ：WL
@Date    ：2022/6/13 21:21 
@Describe: 模板模式

模板模式：定义一个操作中的算法骨架，而将一些步骤延迟到子类中。模板方法使得子类可以不改变一个算法的结构即可重定义该算法的
        某些特性。

角色：
    抽象类（AbstractClass）：定义抽象的原子操作（钩子操作）；实现一个模板方法作为算法的骨架。
    具体类（Concrete Class）：实现原子操作。

优点：
    可变的部分可以充分扩展，不变的步骤可以充分封装
    提取公共代码，减少冗余代码，便于维护
    具体过程可以定制，总体流程方便掌控
    使用模板方法可以将代码的复用最大化

缺点：
    模板模式在抽象类中定义了子类的方法，即子类对父类产生了影响，部分影响了代码的可读性。

应用场景：
    一次性实现算法的不变的部分
    各个子类中的公共行为应该被提取出来并集中到一个公共父类中以避免代码重复
    控制子类扩展
    某超类的子类中有公有的方法，并且逻辑基本相同，可以使用模板模式。必要时可以使用钩子方法约束其行为
"""
from abc import ABCMeta, abstractmethod
from time import sleep


class Windows(metaclass=ABCMeta):
    @abstractmethod
    def start(self):
        """原子操作/钩子操作"""
        pass

    @abstractmethod
    def repaint(self):
        """原子操作/钩子操作"""
        pass

    @abstractmethod
    def stop(self):
        """原子操作/钩子操作"""
        pass

    def run(self):
        """模板方法"""
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindows(Windows):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口开启")

    def stop(self):
        print("窗口关闭")

    def repaint(self):
        print(self.msg)


# client
MyWindows("hello...").run()
