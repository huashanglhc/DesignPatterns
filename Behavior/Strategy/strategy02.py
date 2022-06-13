#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：strategy02.py
@Author  ：WL
@Date    ：2022/6/13 15:38 
@Describe: 策略模式

主要解决：在有多种算法相似的情况下，使用if...else所带来的复杂和难以维护

注意事项： 如果一个系统的策略多于四个，就需要考虑使用混合模式，解决策略类膨胀的问题。

应用场景：
    1. 当你想使用对象中各种不同的算法变体， 并希望能在运行时切换算法时， 可使用策略模式。
    2. 当类中使用了复杂条件运算符以在同一算法的不同变体中切换时， 可使用该模式。
    3. 当你有许多仅在执行某些行为时略有不同的相似类时， 可使用策略模式。

"""
from abc import ABCMeta, abstractmethod
from typing import List


class AbstractStrategy(metaclass=ABCMeta):
    """策略接口声明了某个算法各个不同版本间所共有的操作。上下文会使用该接口来调用有具体策略定义的算法。"""

    @abstractmethod
    def algorithm(self, data: List):
        pass


class StragegyA(AbstractStrategy):
    """具体策略会在遵循策略基础接口的情况下实现算法。该接口实现了它们在上下文中的互换性。"""

    def algorithm(self, data: List):
        print(f"使用策略:{type(self).__name__}")
        return sorted(data)


class StragegyB(AbstractStrategy):
    def algorithm(self, data: List):
        print(f"使用策略:{type(self).__name__}")
        return reversed(sorted(data))


class Context(object):
    """
    上下文定义了客户端关注的接口.
    上下文会维护指向某个策略对象的引用。上下文不知晓策略的具体类。上下文必须通过策略接口来与所有策略进行交互.
    上下文通常会通过构造函数来接收策略对象，同时还提供设置器以便在运行时切换策略。
    上下文会将一些工作委派给策略对象，而不是自行实现不同版本的算法。
    """

    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        """上下文会维护指向某个策略对象的引用。上下文不知晓策略的具体类。上下文必须通过策略接口来与所有策略进行交互."""
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        """设置器以便在运行时切换策略"""
        self._strategy = strategy

    def biz_logic(self, data: List):
        """上下文会将一些工作委派给策略对象"""
        result = self._strategy.algorithm(data)
        print(','.join(result))


def main():
    data = ["a", "c", "d", "b", "e"]
    context = Context(StragegyA())
    context.biz_logic(data)
    print()

    context.strategy = StragegyB()
    context.biz_logic(data)


if __name__ == "__main__":
    main()
