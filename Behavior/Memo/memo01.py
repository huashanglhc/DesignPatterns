#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：memo01.py
@Author  ：WL
@Date    ：2022/6/15 9:58 
@Describe: 备忘录模式

备忘录： 保存一个对象的某个状态，以便在适当的时候恢复对象。备忘录模式属于行为模式。

意图： 在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态。

应用案例：
    1. 后悔药
    2. 打游戏时的存档
    3. Windows里的ctri + z
    4. IE中的后退
    5. 数据库的事务管理

优点：
    1. 给用户提供一种可以恢复状态的机制，可以使用户能够比较方便的回到某个历史状态
    2. 实现了信息的封装，使得用户不需要关系状态的保存细节
    3. 有时一些发起人对象内部的信息必须保存在发起人对象以外的地方，但是必须要发起人对象自己读取，这时，使用备忘录模式可以
        把复杂的发起人内部信息对其他的对象屏蔽起来，从而可以恰当地保持封装边界。
    4. 本模式简化了发起人类，发起人不再需要管理和保存其内部状态的一个个版本，客户端可以自行管理他们所需要的这些状态版本。
    5. 当发起人角色的状态改变的时候，有可能这个状态无效，这时候可以使用暂时存储起来的备忘录讲状态复原。

缺点：
    1. 消耗资源。如果类的成员变量过多，势必会占用较大的资源，而且每一次保存都会消耗一定的内存
    2. 如过发起人角色的状态需要完整地存储到备忘录对象中，那么在资源消耗上面备忘录对象会很昂贵。
    3. 当负责人角色将一个备忘录存储起来的时候，负责人可能并不知道这个状态会占用多大的存储空间，从而无法提醒用户一个操作是否
    很昂贵。


使用场景：
    1. 需要保存/恢复数据的相关状态场景 2. 提供一个可回滚的操作

注意事项：
    1. 为了符合迪米特原则，还要增加一个管理备忘录的类。
    2. 为了节约内存，可使用原型模式 + 备忘录模式

备忘录角色：
    1.Originator(发起人)：负责创建一个备忘录Memento,用以记录当前时刻自身内部的状态，并可使用备忘录恢复内部状态。Originator
    可以根据需要决定Memento存储自己的哪些内存状态。

    2.Memento(备忘录)： 负责存储Originator对象的内存状态，并可以防止Originator以外的其他对象访问备忘录。备忘录有两个接口：
    Caretaker只能看到备忘录的窄接口，他只能将备忘录传递给其他对象。Originator却可看到备忘录的宽接口，允许它访问返回到
    先前状态所需要的所有数据。

    3. Caretaker(管理者):负责备忘录Memento，不能对Memento的内容进行访问或者操作。
"""


# 发起人
class Originator:

    def __init__(self, state):
        self.state = state

    def create_memento(self):
        return Memento(self.state)

    def set_memento(self, memento):
        self.state = memento.state

    def show(self):
        print("当前状态 ", self.state)


# 备忘录
class Memento:

    def __init__(self, state):
        self.state = state


# 管理者
class Caretaker:

    def __init__(self, memento):
        self.memento = memento


if __name__ == "__main__":
    # 初始状态
    originator = Originator(state='On')
    originator.show()
    # 备忘录
    caretaker = Caretaker(originator.create_memento())
    # 修改状态
    originator.state = 'Off'
    originator.show()
    # 复原状态
    originator.set_memento(caretaker.memento)
    originator.show()
