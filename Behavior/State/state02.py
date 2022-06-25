#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：state02.py
@Author  ：WL
@Date    ：2022/6/25 22:28 
@Describe: 状态模式

状态模式： 让你能在一个对象内部状态变化时改变其行为。

该模式将与状态相关的行为抽象到独立的状态类中，让原对象将工作委托给这些类的实例，而不是自行处理

状态模式建议为对象的所有可能的状态新建一个类，然后将所有状态的对应行为抽象到这些类中。

原始对象被称为上下文（context）,它并不会自动实现所有行为，而是会保存一个指向表示当前状态对象的引用，且将所有与状态相关的工作
委派给该对象。

状态模式 VS 策略模式： 在状态模式中，特定状态知道其他所有状态的存在，且能触发从一个状态到另一个状态转换；策略模式几乎完全不知
                    道其他策略存在。

角色：
    上下文（Context）: 保存了对于一个具体状态对象的引用，并会将所有与该状态相关的工作委派给它。上下文通过状态接口与状态对象
                    交互，且会提供一个设置器用于传递新的状态对象。
    状态（State）: 接口会声明特定于状态的方法。这些方法能被其他所有具体状态所理解，因为你不希望某些状态所拥有的方法永远不会
                被调用。
    具体状态（Concrete States）: 会自行实现特定于状态的方法。为了避免多个状态中包含相似代码，你可以提供一个封装有部分通用
                                行为的中间抽象类。

上下文和具体状态都可以设置上下文的下个状态，并可通过替换连接到上下文的状态对象来完成时间的状态转换。

状态模式适用场景：
    1. 如果对象需要根据自身当前状态进行不同行为，同时状态的数量非常多且与状态相关的代码会频繁变更的话，可使用状态模式。
    2. 模式建议你将所有特定于状态的代码抽取到一组独立的类中。这样一来，你可以独立于其他状态的情况下添加信状态或修改已有
        状态，从而减少维护成本。
    3. 如果某个类需要根据成员变量的当前值改变自身行为，从而需要使用大量的条件语句时，可使用该模式。
    4. 状态模式会将这些条件语句的分支抽取到相应状态的方法中。同时，你还可以清除主要类中特定状态相关的临时成员变量和帮手方法代码
    5. 当相似状态和基于条件的状态机转换中存在许多重复代码时，可使用状态模式。
    6. 状态模式让你能够生成状态类层次结构，通过将公用代码抽取到抽象基类中来减少重复。
 实现方式
    1. 确定哪些类是上下文。 它可能是包含依赖于状态的代码的已有类； 如果特定于状态的代码分散在多个类中，
        那么它可能是一个新的类。
    2. 声明状态接口。 虽然你可能会需要完全复制上下文中声明的所有方法， 但最好是仅把关注点放在那些可能包含特
        定于状态的行为的方法上。
    3. 为每个实际状态创建一个继承于状态接口的类。 然后检查上下文中的方法并将与特定状态相关的所有代码抽取到新建的类中。
        在将代码移动到状态类的过程中， 你可能会发现它依赖于上下文中的一些私有成员。 你可以采用以下几种变通方式：
            将这些成员变量或方法设为公有。
            将需要抽取的上下文行为更改为上下文中的公有方法， 然后在状态类中调用。 这种方式简陋却便捷， 你可以稍后再对其进行修补。
            将状态类嵌套在上下文类中。 这种方式需要你所使用的编程语言支持嵌套类。
    4. 在上下文类中添加一个状态接口类型的引用成员变量， 以及一个用于修改该成员变量值的公有设置器。
    5. 再次检查上下文中的方法， 将空的条件语句替换为相应的状态对象方法。

优点：
    单一职责：将与特定状态相关的代码放在单独的类中
    开闭原则：无需修改已有状态类和上下文就能引入新状态
    通过消除臃肿的状态机条件语句简化上下文代码

缺点：
    如果状态机只有很少几个状态，或者很少发生改变，那么应用该模式可能会显得小题大作。

与其他模式的关系：
    桥接模式、状态模式和策略模式的接口非常相似。实际上，它们都基于组合模式---即将工作委派给其他对象。
    状态可被视为策略的扩展。两者都基于组合机制：它们都通过将部分工作委派给 “帮手” 对象来改变其在不同情景下的行为。
                    策略使得这些对象相互之间完全独立， 它们不知道其他对象的存在。 但状态模式没有限制具体状态之间的依赖，
                     且允许它们自行改变在不同情景下的状态。
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Context(ABC):
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class ConcreteStateA(State):
    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        self.context.transition_to(ConcreteStateA())


if __name__ == "__main__":
    # The client code.

    c = Context(ConcreteStateA())
    c.request1()
    c.request2()
