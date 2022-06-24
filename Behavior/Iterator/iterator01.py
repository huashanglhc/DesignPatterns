#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：iterator01.py
@Author  ：WL
@Date    ：2022/6/13 22:20 
@Describe: 迭代器模式

迭代器： 是一种行为设计模式，让你能在不暴露复杂数据结构内部细节的情况下遍历其中所有的元素。

注意： 迭代器是一次性的，当迭代过一轮后，再次迭代将获取不到元素

创建迭代器方法：
    1. iter(),将可迭代对象转化成迭代器
    2. __iter__()与__next__()魔术方法
        __iter__: 用于生成迭代器
        __next__: 用于获取遍历迭代器内容
    3. itertools模块，使用内置模块生成迭代器
    4. 其他创建方法：zip(),map(),enumerate()

为什么有了迭代器还要存在可迭代对象（列表）？？
    （1）写法简便，用意直白；（2）可重复迭代，避免一次性迭代器的缺陷；（3）不需要创建迭代器，减少开销。

迭代器 VS 可迭代对象
    列表、元组、字典和集合都是可迭代的对象。它们是可迭代的容器，您可以从中获取迭代器（Iterator）。所有这些对象都有用于
    获取迭代器的 iter()

for 循环实际上创建了一个迭代器对象，并为每个循环执行 next() 方法。
"""