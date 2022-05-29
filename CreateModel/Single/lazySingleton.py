# -*- coding: utf-8 -*-
"""
@File        : lazySingleton.py
@Author      : wangliang
@Time        : 2022/5/28 7:28
@Description : 懒汉式单例模式
懒汉式单例模式：初始化类的时候不创建对象，第一次调用才创建。这个时候就要注意线程安全性了。

优点：
    资源利用合理，不调用 get_instance 方法不创建单例对象

缺点：
    线程不安全，多线程时可能会获取到不同单例对象的情况。解决办法是加互斥锁，但会降低效率建议使用
"饿汉式单例模型"，若采用 "懒汉式单例模型"，则特别注意加锁考虑线程安全问题。
"""
import time
import threading


class LazySingleton:
    _instance = None

    def __init__(self):
        if not hasattr(LazySingleton, '_instance'):
            print("__init__ method called, but no instance created")
        else:
            print("instance already created:", self._instance)

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            time.sleep(0.05)
            cls._instance = LazySingleton()
        return cls._instance


# a1 = LazySingleton().get_instance()
# print("a1------------------->", a1)
# a2 = LazySingleton().get_instance()
# print("a2------------------->", a2)
#
#
# a3 = LazySingleton()
# print("a3------------------->", a3)
# a4 = LazySingleton()
# print("a4------------------->", a4)

def task():
    s = LazySingleton().get_instance()
    print(id(s))


for i in range(1000):
    t = threading.Thread(target=task)
    t.start()

# 多线程场景下并不是真正的单例模式
