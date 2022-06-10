#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：adapter03.py
@Author  ：WL
@Date    ：2022/6/10 16:16 
@Describe: 
"""


# 步骤一：定义老接口


class Human(object):
    def __init__(self):
        self.name = "Human"

    def work(self, work_type):
        return "{} is a {}".format(self.name, work_type)


# 步骤二：定义新接口


class Dog(object):
    def __init__(self, name):
        self.name = name

    def pet(self):
        return "{} is a dog, make fun".format(self.name)


class Computer(object):
    def execute(self, cpu, memory, hdd):
        return "execute projram, configure is cpu: {} memory: {} hdd: {} ".format(cpu, memory, hdd)


# 步骤三：定义适配器


class Adapter(object):
    def __init__(self, obj, adapt_method):
        """
        :param obj: 被适配的新接口对象
        :param adapt_method: dict(key, value),key为老接口方法，value为新接口方法
        """
        self.obj = obj
        self.obj.__dict__.update(adapt_method)


# 步骤四：新旧函数/方法适配

if __name__ == '__main__':
    computer_obj = Computer()
    Adapter(computer_obj, dict(work=computer_obj.execute))

    dog_obj = Dog("狗狗")
    Adapter(dog_obj, dict(work=dog_obj.pet))

    # 用统一的work适配不同对象的方法，这样在无需修改源对象的情况下就实现了不同对象方法的适配
    print(computer_obj.work("4 cores", "4G", "500G"))
    print(dog_obj.work())
