#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：visitor.py
@Author  ：WL
@Date    ：2022/6/23 17:32 
@Describe: 访问者模式

访问者模式： 数据结构中保存者许多元素，当改变一种对元素的处理方式时，我们避免重复的修改数据类的结构，那我们在设计之初就将
数据的处理分离。

角色：
    Visitor：接口或者抽象类,定义了对每个Element访问的行为，它的参数就是被访问的元素，它的方法个数理论上与元素的个数是一样
            的，因此，访问者模式要求元素的类型要稳定，如果经常添加、移除元素类，必然会导致频繁地修改Visitor接口。如果出现
            这种情况，则说明不适合使用访问者模式。
    ConcreteVisitor具体的访问者，它需要给出对每一个元素类访问时所产生的具体行为。
    Element:元素的接口或者抽象类，它定义了一个接受访问者（accept）的方法，其意义是指每一个元素都要可以被访问者访问。
    ConcreteElement:具体的元素类，它提供接收访问者的具体实现，而这个具体的实现，通常情况下是使用访问者者提供的访问元素类的
            方法。
    ObjStruct: 定义当中所提到的对象结构，对象结构是一个抽象表述，它内部管理了元素的集合，并且可以迭代这些元素提供
            访问者访问。

目的：是在不修改已有程序结构前提下，通过添加额外的访问者完成对代码功能的拓展。
"""
from abc import ABCMeta, abstractmethod


class Element(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

    @abstractmethod
    def do_entry(self):
        pass


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visitor_element1(self, e):
        pass

    @abstractmethod
    def visitor_element2(self, e):
        pass


class ConcreteElement1(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visitor_element1(self)

    def do_entry(self):
        print("This is Element 1")


class ConcreteElement2(Element):
    def accept(self, visitor: Visitor) -> None:
        visitor.visitor_element2(self)

    def do_entry(self):
        print("This is Element 2")


class ConcreteVisitor(Visitor):
    def visitor_element1(self, e: Element):
        e.do_entry()

    def visitor_element2(self, e: Element):
        e.do_entry()


class ObjStruct:
    @staticmethod
    def get_elements():
        return ConcreteElement1(), ConcreteElement2()


def main():
    ele_list = ObjStruct.get_elements()
    for e in ele_list:
        e.accept(ConcreteVisitor())


if __name__ == '__main__':
    main()
