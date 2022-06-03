#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：AbstractFactory.py
@Author  ：WL
@Date    ：2022/6/3 19:41 
@Describe: 抽象工厂

角色：
    抽象产品角色
    具体产品角色
    抽象工厂角色
    具体工厂角色

优点：
    将客户端与类的具体实现相分离
    每个工厂创建了一个完整的产品系列，使得易于交互产品系列
    有利于产品的一致性（即产品之间的约束关系）

缺点：
    难以支持新品种的（抽象产品）

应用场景：

"""
from abc import ABCMeta, abstractmethod


# 抽象产品
class PhoneShell(metaclass=ABCMeta):
    @abstractmethod
    def show_phone(self):
        pass


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def show_cpu(self):
        pass


class OS(metaclass=ABCMeta):
    @abstractmethod
    def show_os(self):
        pass


# 具体产品
class SmallShell(PhoneShell):
    def show_phone(self):
        print("生产普通手机小手机壳")


class BigShell(PhoneShell):
    def show_phone(self):
        print("生产普通手机大手机壳")


class AppleShell(PhoneShell):
    def show_phone(self):
        print("生产苹果手机壳")


class SnapDragonCPU(CPU):
    def show_cpu(self):
        print("晓龙CPU")


class MediaCPU(CPU):
    def show_cpu(self):
        print("联发科CPU")


class AppleCPU(CPU):
    def show_cpu(self):
        print("苹果CPU")


class Android(OS):
    def show_os(self):
        print("Android系统")


class IOS(OS):
    def show_os(self):
        print("IOS系统")


# 抽象工厂
class PhoneFactory(metaclass=ABCMeta):
    @abstractmethod
    def make_shell(self):
        pass

    @abstractmethod
    def make_cpu(self):
        pass

    @abstractmethod
    def make_os(self):
        pass


# 具体工厂
class MiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return BigShell()


class HuaweiFactory(PhoneFactory):
    def make_cpu(self):
        return SnapDragonCPU()

    def make_os(self):
        return Android()

    def make_shell(self):
        return SmallShell()


class IphoneFactory(PhoneFactory):
    def make_cpu(self):
        return AppleCPU()

    def make_os(self):
        return IOS()

    def make_shell(self):
        return AppleShell()


# 客户端
class Phone:
    def __init__(self, cpu, os, shell):
        self.cpu = cpu
        self.os = os
        self.shell = shell

    def show_info(self):
        print("手机信息：")
        self.cpu.show_cpu()
        self.os.show_os()
        self.shell.show_phone()


def make_phone(factory):
    cpu = factory.make_cpu()
    os = factory.make_os()
    shell = factory.make_shell()

    return Phone(cpu, os, shell)


print("====================小米手机====================")
p1 = make_phone(MiFactory())
p1.show_info()

print("====================华为手机====================")
p2 = make_phone(HuaweiFactory())
p2.show_info()

print("====================苹果手机====================")
p3 = make_phone(IphoneFactory())
p3.show_info()
