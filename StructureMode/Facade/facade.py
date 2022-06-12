#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：facade.py
@Author  ：WL
@Date    ：2022/6/12 12:00 
@Describe: 外观模式
外观模式：为子系统中的一组接口提供了一个一致的界面，外观模式定义了一个高层的接口，这个接口使得这个子系统更加容易使用。

角色：
    外观
    子系统类

优点：
    减少系统相互依赖
    提高灵活性
    提高安全性
外观类的目的：是通过建立一个中间类，把调用目标类的代码都封装好。例如有时候目标类有很多个，逐一得去调用他们会很麻烦，这样
            通过中间类封装好得接口，client的调用就很简单。

外观模式的核心：在于将复杂的内部实现包装起来，只向外界提供简单的调用接口。类似现实世界中的电脑，开机按钮是一个简单的调用接口
            ，帮用户屏蔽了复杂的内部电路。

外观模式缺点：不能很好的限制客户使用子系统类，而且在不引入抽象外观类的情况下，增加新的子系统可能需要修改外观类或客户端的
            源代码，违背了“开闭原则”

外观模式值得注意的点：
    1. 外观模式对接口进行了简化，但这并不意外着对子系统进行彻底封装。如果有必要，这些子系统的接口还可以继续暴露给客户、
    2. 外观模式不能新增功能，但他可以将某些功能按次序执行
    3. 子系统与外观不是一对一关系，是多对多关系。一个子系统可以拥有多个外观，一个外观可以调用多个子系统。

应用场景：
    1. 为复杂的模块或子系统提供外界访问的模块
    2. 子系统相对独立
    3. 预防低水平人员带来的风险
"""


class CPU:
    def run(self):
        print("CPU正在高速运转")

    def stop(self):
        print("CPU停止运行")


class Disk:
    def run(self):
        print("硬盘开始工作")

    def stop(self):
        print("硬盘停止工作")


class Memory:
    def run(self):
        print("内存通电")

    def stop(self):
        print("内存断电")


class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


# client
c = Computer()
c.run()
c.stop()
