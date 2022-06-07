#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：原型模式.py
@Author  ：WL
@Date    ：2022/6/7 10:01 
@Describe: 原型模式
原型模式： 提供了一种创建对象的最佳方式。这种模式实现了一个原型接口，该接口用于创建当前对象的克隆。当直接创建对象的代价比较大
时，则采用这种模式。

角色：

优点：

缺点：

应用场景：
    当我们已经存在一个对象，这个对象有其属性和方法，若我们还想去获得另外一个同类型对象，此时有两种选择：
重新去创建一个新的对象，或者 根据已有的对象复制一个副本，而在很多时候我们不需要完全去重新构建一个对象，
只需要在原有对象存在的基础上（保留原对象），
去修改其属性和方法得到一个新的对象。
"""
from copy import deepcopy


class Fruit:
    def __init__(self, weight=0.0, package=False):
        self.name = None
        self.weight = weight
        self.price = 0
        self.package = package
        self.promotion_price = 0

    def show(self):
        pack = "袋装"
        if self.package:
            pack = "盒装"
        print("水果名称：%s\n重量：%.2f（千克）\n价格：%.2f（元/千克）\n包装方式：%s\n原需支付的金额：%.2f（元）\n限时促销价：%.2f（元）！！！"
              % (self.name, self.weight, self.price, pack, self.weight * self.price, self.promotion_price))
        print("-*-" * 15)

    def deep_clone(self):
        return deepcopy(self)


class Grape(Fruit):
    def __init__(self, weight=0.0, package=False):
        super().__init__(weight, package)
        self.name = "葡萄"
        self.price = 18.0
        self.promotion_price = 28.99


class Hami_Melon(Fruit):
    def __init__(self, weight=0.0, package=False):
        super().__init__(weight, package)
        self.name = "哈密瓜"
        self.price = 22.0
        self.promotion_price = 39.99


class Orange(Fruit):
    def __init__(self, weight=0.0, package=False):
        super().__init__(weight, package)
        self.name = "橘子"
        self.price = 12.5
        self.promotion_price = 18.88


class FruitCache:
    def __init__(self):
        self.fruits = []

    def load_cache(self):
        grape_1 = Grape(2.5, True)
        self.fruits.append(grape_1)

        grape_2 = grape_1.deep_clone()
        self.fruits.append(grape_2)

        hami_melon = Hami_Melon(3.2, False)
        self.fruits.append(hami_melon)

        orange = Orange(2.6, True)
        self.fruits.append(orange)

        return self.fruits


if __name__ == '__main__':
    use = FruitCache().load_cache()
    print("-*-" * 15)
    for item in use:
        item.show()

