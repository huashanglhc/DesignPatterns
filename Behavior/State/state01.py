#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：state01.py
@Author  ：WL
@Date    ：2022/6/15 10:56 
@Describe: 状态模式

状态模式：对象内部状态发生改变对象行为也会发生变化

主要解决： 当控制一个对象状态的条件条件表达式过于复杂时的情况。把状态的判断逻辑转移到表示不同状态的一系列类中，
    可以把复杂的判断逻辑简化。

角色：
    State: 定义Handle()抽象方法接口。需要通过ConcreteState 类实现
    ConcreteState：实现 Handle() 方法，可以根据状态变化定义执行的实际操作
    Context：接收客户端请求，维护着对象当前状态的引用，以根据请求调用具体的行为

优点：
    1. 在状态设计模式中，对象的行为是其状态的函数结果，且行为在运行时依旧状态而改变。这消除了对 if/else
        或 switch/case 条件逻辑的依赖
    2. 使用状态模式，实现多态行为是很方便的，并且易于添加状态来支持额外的行为
    3. 状态模式提高了聚合性，针对状态的行为被聚合到 ConcreteState 类中，放置在代码的同一个地方
    4. 状态模式不仅改善了扩展应用程序行为时的灵活性，且提高了代码的可维护性。一个 ConcreteState 类即对应一种行为

缺点：
    1. 类爆炸：由于每个状态都需要在 ConcreteState 中定义，可能导致创建太多功能较为单一的类。既增加了代码量，
        又使得状态机的结构更加难以审查
    2. 随着新行为的引入，Context 类需要进行相应的更新以处理每个行为，使得上下文行为更容易受到每个新行为的影响

"""


# 状态的抽象类
class LiftState:
    def open(self):
        pass

    def close(self):
        pass

    def run(self):
        pass

    def stop(self):
        pass


# 具体的状态类
class OpenState(LiftState):
    def open(self):
        print("开: 电梯门已开，请勿重复操作")
        return self

    def close(self):
        print("开: 电梯门即将关闭...")
        print("开: 电梯门已关闭")
        return CloseState()

    def run(self):
        print("开: 开门状态，禁止运行")
        return self

    def stop(self):
        print("开: 开门状态，禁止停止")
        return self


class RunState(LiftState):
    def open(self):
        print("运行: 运行中禁止开门")
        return self

    def close(self):
        print("运行: 运行中禁止关门")
        return self

    def run(self):
        print("运行: 电梯已在运行中，请勿重复操作")
        return self

    def stop(self):
        print("运行: 电梯即将停止")
        print("运行: 电梯已停止")
        return StopState()


class StopState(LiftState):
    def open(self):
        print("停止: 电梯门即将开门")
        print("停止: 电梯门已打开")
        return OpenState()

    def close(self):
        print("停止: 电梯门即将关闭")
        print("停止: 电梯门已关闭")
        return CloseState()

    def run(self):
        print("停止: 电梯即将运行")
        return RunState()

    def stop(self):
        print("停止: 电梯已停止，请勿重复操作")
        return self


class CloseState(LiftState):
    def open(self):
        print("关: 电梯门即将开门")
        print("关: 电梯门已打开")
        return OpenState()

    def close(self):
        print("关: 电梯门已关闭，请勿重复操作")
        return self

    def run(self):
        print("关: 电梯即将运行")
        return RunState()

    def stop(self):
        print("关: 关门状态，禁止停止")
        return self


# 上下文的类
class Context:
    lift_state = ""

    def get_state(self):
        return self.lift_state

    def set_state(self, lift_state):
        self.lift_state = lift_state

    def open(self):
        self.set_state(self.lift_state.open())

    def close(self):
        self.set_state(self.lift_state.close())

    def run(self):
        self.set_state(self.lift_state.run())

    def stop(self):
        self.set_state(self.lift_state.stop())


if __name__ == "__main__":
    ctx = Context()
    ctx.set_state(StopState())
    ctx.open()
    ctx.run()
    ctx.close()
    ctx.run()
    ctx.stop()
    ctx.get_state()
