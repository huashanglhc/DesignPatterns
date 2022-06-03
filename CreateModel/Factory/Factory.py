#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：Factory.py
@Author  ：WL
@Date    ：2022/6/3 19:21 
@Describe: 工厂方法模式

角色：
    抽象工厂角色
    具体工厂角色
    抽象产品角色
    具体产品角色

优点：
    每个具体产品都对应一个具体工厂类，不需要修改工厂类代码
    隐藏了对象创建的具体实现细节

缺点：
    每增加一个具体产品类，就必须增加一个相应的具体工厂类

应用场景：

"""
from abc import ABCMeta, abstractmethod


# 抽象产品
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


# 具体产品
class WechatPay(Payment):
    def pay(self, money):
        print(f"微信支付了{money}元")


class BankPay(Payment):
    def pay(self, money):
        print(f"银行卡支付了{money}元")


class AliPay(Payment):
    def __init__(self, use_hb=False):
        self.use_hb = use_hb

    def pay(self, money):
        if self.use_hb:
            print(f"花呗支付了{money}元")
        else:
            print(f"余额宝支付了{money}元")


# 抽象工厂
class PayFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_factory(self):
        pass


# 具体工厂
class HuaBeiFactory(PayFactory):
    def create_factory(self):
        return AliPay()


class BankPayFactory(PayFactory):
    def create_factory(self):
        return BankPay()


class WechatPayFactory(PayFactory):
    """微信支付工厂"""

    def create_factory(self):
        return WechatPay()


class AliPayFactory(PayFactory):
    """阿里支付工厂"""
    def create_factory(self):
        return AliPay()


# client
pf = HuaBeiFactory()
p = pf.create_factory()
p.pay(1000)

pf1 = BankPayFactory()
p1 = pf1.create_factory()
p1.pay(2000)
