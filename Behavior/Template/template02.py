#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：template02.py
@Author  ：WL
@Date    ：2022/6/13 21:27 
@Describe: 模板方法02

识别方法：模板方法可以通过行为方法来识别，该方法已有一个在基类中定义的“默认”行为

模板设计模式旨在消除代码重复。如果我们发现结构相近的（多个）算法中有重复代码，则可以把算法的不变（通用）部分留在一个模板
方法/函数中，把易变（不同）的部分移到动作/钩子方法/函数中

策略模式 VS 模板模式
    模板取决于继承，而策略使用组合。模板方法模式是通过子类化在编译时进行算法选择，而策略模式是运行时进行选择
"""
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    抽象类定义了一个模板方法，它包含一个框架一些算法，由(通常)对抽象原语的调用组成操作。
    具体的子类应该实现这些操作，但保留模板方法本身不变。
    """

    def template_method(self) -> None:
        """
        模板方法定义了算法的框架。
        """

        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    # 这些操作已经有了实现。.

    def base_operation1(self) -> None:
        print("AbstractClass says: I am doing the bulk of the work")

    def base_operation2(self) -> None:
        print("AbstractClass says: But I let subclasses override some operations")

    def base_operation3(self) -> None:
        print("AbstractClass says: But I am doing the bulk of the work anyway")

    # 这些操作必须在子类中实现。

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

    # 这些都是“钩子”。子类可以重写它们，但这不是强制的
    # 因为钩子已经有默认的(但为空)实现。钩子的一些关键位置提供额外的扩展点算法

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class ConcreteClass1(AbstractClass):
    """
    具体类必须实现基类的所有抽象操作类。它们还可以用默认实现覆盖某些操作。
    """

    def required_operations1(self) -> None:
        print("ConcreteClass1 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass1 says: Implemented Operation2")


class ConcreteClass2(AbstractClass):
    """
    通常，具体类只重写基类的一小部分操作。
    """

    def required_operations1(self) -> None:
        print("ConcreteClass2 says: Implemented Operation1")

    def required_operations2(self) -> None:
        print("ConcreteClass2 says: Implemented Operation2")

    def hook1(self) -> None:
        print("ConcreteClass2 says: Overridden Hook1")


def client_code(abstract_class: AbstractClass) -> None:
    """
   客户端代码调用模板方法来执行算法。客户端代码不必知道它所处理的对象的具体类，比如只要它通过对象基类的接口来处理对象。
    """

    # ...
    abstract_class.template_method()
    # ...


if __name__ == "__main__":
    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass1())
    print("")

    print("Same client code can work with different subclasses:")
    client_code(ConcreteClass2())
