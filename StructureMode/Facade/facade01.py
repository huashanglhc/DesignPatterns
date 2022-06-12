#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：facade01.py
@Author  ：WL
@Date    ：2022/6/12 12:50 
@Describe: 使用外观模式步奏

步奏：
    1. 创建子系统角色
    2. 创建外观角色，该角色为子系统中的一组接口提供一个一致界面

案例：一组火警报警系统，由三个元件构成：一个警报器、一个喷水器、一个自动拨打电话的装置
"""


# 子系统角色
class AlarmSender:
    def run(self, msg):
        return "产生了高温告警: {}".format(msg)


class Sprinkler:
    def run(self):
        return "洒水降温"


class Dialer:
    def run(self, name, phone):
        return "拨打值班人：{} 电话: {}".format(name, phone)


# 步骤二：定义外观类，封装子系统的操
class EmergencyFacade:
    def __init__(self):
        self.alarm = AlarmSender()
        self.water = Sprinkler()
        self.dialer = Dialer()

    def run(self, name, phone, msg):

        return self.alarm.run(msg), self.water.run(), self.dialer.run(name, phone)


if __name__ == "__main__":
    user_name = "Bruce"
    user_phone = "210-123456"
    info = "高温告警，请立即处理"
    emergency = EmergencyFacade()
    resp = emergency.run(user_name, user_phone, info)
    print(resp)
