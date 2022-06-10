#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：adapter.py
@Author  ：WL
@Date    ：2022/6/10 15:23 
@Describe: 适配器类
适配器：将一个类的接口转换成客户希望的另一个接口。适配器模式使得原本由于接口不兼容而不能一起工作的哪些类可以一起工作。

角色：
    目标抽象类：目标抽象类定义客户所需的接口，可以是一个抽象类或接口，也可以是具体类。在类适配器中，由于C#语言不支持多重继承，所以它只能是接口。
    适配器类：它可以调用另一个接口，作为一个转换器，对 Adaptee 和 Target 进行适配。它是适配器模式的核心。
    适配者类：适配者即被适配的角色，它定义了一个已经存在的接口，这个接口需要适配，适配者类包好了客户希望的业务方法。

适用场景：
    想使用一个已经存在的类，但它的接口不符合你的要求
    （对象适配器）想使用一些存在的子类，但不可能对每一个都进行子类化匹配它们的接口。对象适配器可以适配它的父亲接口
"""
from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class Wechat(Payment):
    def pay(self, money):
        print(f"微信支付了{money}元...")


class Alipay(Payment):
    def pay(self, money):
        print(f"支付宝支付了{money}元...")


class BankPay:
    def cost(self, money):
        print(f"银联支付了{money}元")


class ApplePay:
    def cost(self, money):
        print(f"苹果支付了{money}元")


# 对象适配器
# 实现接口统一（继承Payment）,代码复用（利用类的属性）
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


# client
p = PaymentAdapter(BankPay())
p.pay(1000)


# 类适配器
class NewApplePay(Payment, ApplePay):
    def pay(self, money):
        self.cost(money)


p2 = NewApplePay()
p2.pay(2000)
