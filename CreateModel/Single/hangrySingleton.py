# -*- coding: utf-8 -*-
"""
@File        : HangrySingleton.py
@Author      : wangliang
@Time        : 2022/5/28 7:05
@Description : 饿汉式单例模式
单例：保证一个类仅有一个实例，并提供一个访问他的全局访问点
饿汉式单例： 当类初始化的时候，就创建这个实例对象，以后永远返回同一个实例对象。

应用场景：
    python中模块的创建就是一个天然的单例模式
    系统日志输出的场景
    资源管理的场景
    涉及共享的场景
    有关认证的场景
    操作系统的任务管理器
    线程池、数据库连接池等资源池一般也用单例模式
    Windows资源管理器是单例模式
    网站计数器
    某个服务器程序的配置信息存放在一个文件中，客户端通过一个 AppConfig 的类来读取配置文件的信息。类似 AppConfig 这样的类，我们希望在程序运行期间只存在一个实例对象。

优点：
    在内存中只有一个对象，节省内存空间
    避免频繁的创建销毁对象，可以提高性能
    避免对共享资源的多重占用，简化访问
    为整个系统提供一个全局访问点

缺点：
    不适用于变化频繁的对象
    滥用单例将带来一些负面问题，如为了节省资源将数据库连接池对象设计为的单例类，可能会导致共享连接池对象的程序过多而出现连接池溢出

"""
import time
import threading


class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            time.sleep(0.1)
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance


# a = Singleton()
# b = Singleton()
# print(id(a))
# print(id(b))

# 多线程下饿汉单例模式：多线程模式下饿汉模式是伪单例
def task():
    s = Singleton()
    print(id(s))


for i in range(1000):
    t = threading.Thread(target=task)
    t.start()

