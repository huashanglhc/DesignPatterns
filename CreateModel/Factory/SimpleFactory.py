#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：SimpleFactory.py
@Author  ：WL
@Date    ：2022/6/3 18:56 
@Describe: 简单工厂方法
应用场景：

角色：
    抽象产品角色
    具体产品角色
    工厂角色

优点：

    隐藏了对象创建的实现细节
    客户端不需要修改代码
缺点：

    违反了单一职责原则，将创建逻辑集中到一个工厂类里
    当添加新产品时，需要修改工厂类代码，违反了开闭原则
"""
from abc import ABCMeta, abstractmethod


# 抽象产品角色（Product）
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# 具体产品角色（Concrete Product）
class WeChatPay(Payment):
    def pay(self, money):
        print(f"微信支付了: {money}")


class AliPay(Payment):
    def __init__(self, use_hb=False):
        self.use_hb = use_hb

    def pay(self, money):
        if self.use_hb:
            print(f"使用花呗支付了：{money}")
        else:
            print(f"使用余额宝支付了： {money}")


# 工厂角色（Creator）
class PaymentFactory:
    @staticmethod
    def create_payment(method):
        if method == "alipay":
            return AliPay()
        elif method == "huabei":
            return AliPay(use_hb=True)
        elif method == "wechat":
            return WeChatPay()
        else:
            raise TypeError(f"No such payment named {method}")


# client
pf = PaymentFactory()
p = pf.create_payment('wechat')
p.pay(1000)
