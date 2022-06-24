#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：visitor02.py
@Author  ：WL
@Date    ：2022/6/24 22:20 
@Describe: 访问者模式

访问者模式：数据结构中保存着许多元素，当改变一种对元素的处理方式，我们避免重复的修改数据类的结构，那我们在设计之初就将数据的
处理分离，即数据类只提供一个数据处理的接口，而数据类的处理方法叫它访问者，那么相同结构的数据面临不同的处理结果时，我们只需要
创建不同的访问者。

意图： 将数据结构与数据操作分离
主要解决：稳定的数据结构和易变的操作耦合问题
关键代码：在数据基础类里面有一个方法接受访问者，将自身引用传入访问者

优点：1. 符合单一职责 2.优秀的扩展 3.灵活性
缺点：1. 具体元素对访问者公布细节，违反了迪米特法则 2. 具体元素变更比较困难 3. 违反了依赖倒置原则，依赖了具体类，没有依赖抽象

业务场景：上市公司原始财务数据，对于会计来说需要制作各种报表，对于财务总监来说需要分析公司业绩，对于战略顾问来说需要分析行业
变化。
"""


class Finance:
    """财务数据结构类"""

    def __init__(self):
        # 销售额
        self.sales = None
        # 成本
        self.cost = None
        # 历史销售额
        self.history_sales = None
        # 历史成本
        self.history_cost = None

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def accept(self, visitor):
        pass


class FinanceYear(Finance):
    """往年财务数据结构类"""

    def __init__(self, year):
        super().__init__()
        # 安排工作人员
        self.work = []
        self.year = year

    def add_work(self, work):
        self.work.append(work)

    def accept(self):
        for obj in self.work:
            obj.visit(self)


class Accounting:
    """会计类"""
    def __init__(self):
        self.id = "会计"
        self.duty = "计算报表"

    def visit(self, table):
        print('会计年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.id, self.duty))
        print('本年度纯利润： {}'.format(table.sales - table.cost))
        print('------------------')


class Audit:
    """财务总监类"""

    def __init__(self):
        self.id = "财务总监"
        self.duty = "分析业绩"

    def visit(self, table):
        print('财务总监年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.id, self.duty))
        if table.sales - table.cost > table.history_sales - table.history_cost:
            msg = "较同期上涨"
        else:
            msg = "较同期下跌"
        print('本年度公司业绩： {}'.format(msg))
        print('------------------')


class Adviser:
    """战略顾问"""

    def __init__(self):
        self.id = "战略顾问"
        self.duty = "制定明年战略"

    def visit(self, table):
        print('战略顾问年度： {}'.format(table.year))
        print("我的身份是： {} 职责： {}".format(self.id, self.duty))
        if table.sales > table.history_sales:
            msg = "行业上行，扩大生产规模"
        else:
            msg = "行业下行，减小生产规模"
        print('本年度公司业绩： {}'.format(msg))
        print('------------------')


class Work:
    """工作类"""

    def __init__(self):
        # 需要处理的年度数据列表
        self.works = []

    def add_work(self, obj):
        self.works.append(obj)

    def remove_work(self, obj):
        self.works.remove(obj)

    def visit(self):
        for obj in self.works:
            obj.accept()


if __name__ == '__main__':
    work = Work()  # 计划安排财务、总监、顾问对2018年数据处理
    # 实例化2018年数据结构
    finance_2018 = FinanceYear(2018)
    finance_2018.sales = 200
    finance_2018.cost = 100
    finance_2018.history_sales = 180
    finance_2018.history_cost = 90
    # 实例化会计
    accounting = Accounting()
    # 实例化总监
    audit = Audit()
    # 实例化顾问
    adviser = Adviser()
    # 会计安排到2018分析日程中
    finance_2018.add_work(accounting)
    # 总监安排到2018分析日程中
    finance_2018.add_work(audit)
    # 顾问安排到2018分析日程中
    finance_2018.add_work(adviser)
    print("finance_2018的work列表", finance_2018.work)
    # 添加2018年财务工作安排
    work.add_work(finance_2018)
    print("需要处理的年度数据列表", work.works)
    work.visit()
