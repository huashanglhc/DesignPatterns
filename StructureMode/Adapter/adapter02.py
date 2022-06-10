#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：adapter02.py
@Author  ：WL
@Date    ：2022/6/10 15:57 
@Describe: 
"""


class Target:
    """
    Target定义客户端代码使用的特定于领域的接口。
    """

    def request(self) -> str:
        return "Target: The default target's behavior."


class Adaptee:
    """
    Adaptee包含一些有用的行为，但是它的接口是不兼容的使用现有的客户机代码。被改写者在被改写之前需要做一些调整
    客户端代码可以使用它。
    """

    def specific_request(self) -> str:
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    Adapter使Adaptee的接口与Target的接口兼容通过多重继承接口。
    """

    def request(self) -> str:
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:
    """
    客户端代码支持所有遵循Target接口的类。
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Client: I can work just fine with the Target objects:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Client: The Adaptee class has a weird interface. "
          "See, I don't understand it:")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")

    print("Client: But I can work with it via the Adapter:")
    adapter = Adapter()
    client_code(adapter)
