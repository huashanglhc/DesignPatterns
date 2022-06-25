#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：command01.py
@Author  ：WL
@Date    ：2022/6/25 18:05 
@Describe: 命令模式

命令模式： 命令模式是一种行为设计模式，他用于封装触发事件（完成任何一个操作）所包含的所有信息。一般有方法名称，
        拥有方法对象，方法参数等。

角色：
    抽象的命令基类（Command）：命令的抽象类，定义命令的接口，可以理解为一个基类。
    具体的命令实现类（ConcreteCommand）：命令接口实现对象，通常会持有接收者，并调用接收者的功能来完成命令要执行的操作。
    命令接受者（Receiver）：真正接收并执行具体命令的对象。任何类都可能成为一个接收者，只要它能够实现命令要求实现的相应功能。
    命令调用者（Invoker）：对命令进行调用，然后将命令发送给接收者。通常会持有命令对象，可以持有很多的命令对象，相当于使用命令对象的入口。
    命令装配者（Client）：客户端会创建具体的命令对象，组装命令对象和接收者。

优点
    把调用操作的类与知道如何执行该操作的对象分开了
    结合队列可以创造一系列命令
    添加命令方便，不用改现有代码
    可以用命令模式定义回滚系统
缺点
    要很多类和对象协作，要确保正确
    每个单独的命令都是一个类，增加了实现和维护的类的数量
"""
class Command:
    """声明命令模式接口"""
    def __init__(self, obj):
        self.obj = obj

    def execute(self):
        pass


class ConcreteCommand(Command):
    """实现命令模式接口"""
    def execute(self):
        self.obj.run()


class Invoker:
    """接受命令并执行命令的接口"""
    def __init__(self):
        self._commands = []

    def add_command(self, cmd):
        self._commands.append(cmd)

    def remove_command(self, cmd):
        self._commands.remove(cmd)

    def run_command(self):
        for cmd in self._commands:
            cmd.execute()


class Receiver:
    """具体动作"""
    def __init__(self, word):
        self.word = word

    def run(self):
        print(self.word)


def client():
    """装配者"""
    test = Invoker()
    cmd1 = ConcreteCommand(Receiver('命令一'))
    test.add_command(cmd1)
    cmd2 = ConcreteCommand(Receiver('命令二'))
    test.add_command(cmd2)
    cmd3 = ConcreteCommand(Receiver('命令三'))
    test.add_command(cmd3)
    test.run_command()


if __name__ == '__main__':
    client()

