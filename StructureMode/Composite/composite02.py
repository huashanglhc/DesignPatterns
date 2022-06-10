#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：composite02.py
@Author  ：WL
@Date    ：2022/6/10 14:42 
@Describe: 公司部门组织结构
"""
from abc import ABCMeta, abstractmethod


# 抽象组件
class CompositeBase(metaclass=ABCMeta):
    """部门抽象出来的抽象基类"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def remove(self, obj):
        pass

    @abstractmethod
    def display(self, level):
        pass


# 节点
class Node(CompositeBase):
    def __init__(self, name, duty):
        super().__init__(name)
        self.duty = duty
        self.children = []

    def add(self, obj):
        self.children.append(obj)

    def remove(self, obj):
        self.children.remove(obj)

    def display(self, level=1):
        print("部门：{} 级别：{} 职责：{}".format(self.name, level, self.duty))
        n = level + 1
        for obj in self.children:
            obj.display(n)


if __name__ == '__main__':
    root = Node("总经理办公室", "总负责人")
    print("root", root.__dict__)
    node1 = Node("财务部门", "公司财务管理")
    root.add(node1)

    node2 = Node("业务部门", "销售产品")
    root.add(node2)

    node3 = Node("生产部门", "生产产品")
    root.add(node3)

    node4 = Node("销售事业一部门", "A产品销售")
    node2.add(node4)
    print("root", root.__dict__)
    node5 = Node("销售事业二部门", "B产品销售")
    node2.add(node5)
    print("root", root.__dict__)
    root.display()
