#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：strategy03.py
@Author  ：WL
@Date    ：2022/6/13 15:48 
@Describe: 策略模式
"""

from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def discount(self, order):
        pass


class StrategyA(Strategy):

    def discount(self, order):
        return order._price * 0.1


class StrategyB(Strategy):

    def discount(self, order):
        return order._price * 0.2 + 50


class OrderContext(object):

    def __init__(self, price, discount_strategy=None):
        self._price = price
        self._strategy = discount_strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def price_with_discount(self):
        if self._strategy:
            discount = self._strategy.discount(self)
        else:
            discount = 0
        pay = self._price - discount
        print(f'折扣策略{type(self._strategy).__name__},原价{self._price}, 折扣价: {pay}')
        return pay


def main():
    order = OrderContext(1000)
    order.price_with_discount()
    st = StrategyA()
    order.strategy = st
    order.price_with_discount()
    st2 = StrategyB()
    order.strategy = st2
    order.price_with_discount()


if __name__ == "__main__":
    main()
