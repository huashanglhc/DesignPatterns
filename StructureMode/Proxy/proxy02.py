#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：proxy02.py
@Author  ：WL
@Date    ：2022/6/12 17:52 
@Describe: 
"""
from abc import ABC, abstractmethod


# 步骤一：定义业务抽象接口
class Subject(ABC):
    """
    抽象接口类，定义Proxy类和具体业务RealSubject类需要实现的通用方法。这样可以在任何使用RealSubject的地方使用Proxy
    """

    @abstractmethod
    def request(self) -> None:
        pass


# 步骤二：定义核心业务类
class RealSubject(Subject):
    """
    具体业务的核心代码实现。RealSubject类可能包含某些执行缓慢的操作，或者需要访问某些敏感数据。
    例如：校验输入数据。Proxy模式可以实现这种功能，并且不需要修改RealSubject核心业务代码
    """

    def request(self) -> None:
        print("RealSubject: Handling request.")


# 步骤三：定义Proxy，将业务请求传递给业务类，并在请求发生前后做额外处理
class Proxy(Subject):
    """
    Proxy类保存引用代理的实体，并提供与业务实体类相同的接口。这样Proxy可以用来代替实体
    """

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject

    def request(self) -> None:
        """
        代理模式常用场景：惰性计算，访问控制，日志等。
        Proxy在执行实际的RealSubject对象之前，添加额外的处理过程
        """
        if self.check_access():
            self._real_subject.request()
            self.log_access()

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self) -> None:
        print("Proxy: Logging the time of request.", end="")


def client(subject: Subject) -> None:
    """
    client同时支持实现了Subject类的所有对象（Proxy类和RealSubject类对象）。
    在实际项目中，clients通常是直接接收RealSubject类实例。
    """
    subject.request()


if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client(real_subject)

    print("*" * 30)
    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client(proxy)
