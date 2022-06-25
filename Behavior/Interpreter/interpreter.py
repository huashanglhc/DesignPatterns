#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：interpreter.py
@Author  ：WL
@Date    ：2022/6/25 17:03 
@Describe:  解释器模式

解释器模式： 给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子

角色：
    AbstractExpression（抽象表达式）：抽象表达式，声明一个抽象的解释操作弗雷，并定义一个抽象的解释方案，
                                    其具体的实现在各个具体的子类解释器中完成。

    TerminalExpression（终结符表达式）：终结符表达式，实现文法中终结符有关的解释操作。文法中每一个终结符都有一个具体的
                                    终结表达式与之对应。

    NonterminalExpression（非终结符表达式）：非终结表达式，实现文法中非终结符有关的解释操作。
                        其中AbstractExpression的interpret()是抽象的解析方法，参数是上下文的环境，
                        而interpret()方法的具体实现则由TerminalExpression和NonterminalExpression实现。

    Context：上下文环境，包含解释器之外的全局信息
    Client：客户端，解析表达式，构建语法树，执行具体的解释操作等

用途： 给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子。

场景：
    1. 将“1+2+3-4”等字符串输入到Python的console，但是本身Python不认识这些字符串，
    就需要定义的一套文法规则来解释这些字符串，也就是设计一个自定义语言。
    2. SQL 解析、符号处理。
    3. 同一份乐谱，用钢琴、小提琴分别解释会得到不同的音乐。
    4. 第一个能想到的利用解释器模式的程序应该就是编译器了，编译器能将源代码翻译成机器能认识的机器码，这是很典型的解释器模式。
    5. 另外正则表达式(RegExp)也是解释器模式的一个应用。

优点：
    1. 可扩展性比较好，灵活
    2. 增加了新的解释表达式的方式
    3. 易于实现简单文法
缺点：
    1.可利用场景比较少。
    2.对于复杂的文法比较难维护，执行效率低。
    3.解释器模式会引起类膨胀。

"""

"""Interpreter Pattern with Python Code
"""

from abc import abstractmethod, ABCMeta


# 抽象一个解释器类
class AbstractExpression(metaclass=ABCMeta):
    @abstractmethod
    def interpreter(self, context):
        pass


# 具体解释器——终端 继承抽象解释器
class TerminalExpression(AbstractExpression):
    def interpreter(self, context):
        print("终端解释器", context)


# 具体解释器——非终端 继承抽象解释器
class NotTerminalExpression(AbstractExpression):
    def interpreter(self, context):
        print("非终端解释器", context)


class Context(object):
    def __init__(self):
        self.name = ""


def main():
    context = Context()
    context.name = 'Andy'
    arr_list = [NotTerminalExpression(), TerminalExpression(), TerminalExpression()]
    for entry in arr_list:
        entry.interpreter(context)


if __name__ == "__main__":
    main()
