#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：decorator.py
@Author  ：WL
@Date    ：2022/6/12 17:19 
@Describe: 装饰模式

装饰器： 需要为某一个对象添加额外的动作、行为时，在不改变类的情况下可以使用装饰器。

角色：
    Component（抽象构件）
    ConcreteComponent（具体构件）
    Decorator（抽象装饰类）
    ConcreteDecorator（具体装饰类）

装饰器VS装饰模式:
    设计模式中的装饰模式:
        1. 是设计模式的一种。是一种编程思想，与编程语言无关
        2. 在不必改变原类文件和使用继承的情况下，动态地扩展一个对象的功能。它是通过创建一个包装对象，
        也就是装饰来包裹真实的对象。
    Python装饰器:
        1. 是Python中的高级函数使用上的一种语法糖。
        2. 是对装饰模式的一个更宽泛的应用，不仅仅能够应用于类，也能应用于函数，类方法和类属性

应用场景：插入日志、性能測试、事务处理、权限处理等
"""
