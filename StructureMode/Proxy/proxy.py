#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：proxy.py
@Author  ：WL
@Date    ：2022/6/12 17:40 
@Describe: 代理模式

代理模式： 为其它对象提供一种代理以控制对这个对象的访问

角色：
    抽象实体（Subject）
    实体（Real Subject）
    代理（Proxy）

优点：
    远程代理：可以影藏对象位于远程地址空间的事实(ORM)
            它给位于远程服务器或不同地址空间上的实际对象提供了一个本地表示。
            例如，你希望为应用程序建立一个监控系统，而该应用涉及多个Web服务器、数据库服务器、celery任务服务器、缓存服务器，
            等等。如果我们要监视这些服务器的CPU和磁盘利用率，就需要建立一个对象，该对象能够用于监视应用程序运行的上下文中，
            同时还可以执行远程命令以获取实际的参数值。在这种情况下，建立一个作为远程对象的本地表示的远程代理对象将可以帮助
            我们实现这个目标。

    虚代理：根据需要创建一个资源消耗较大的对象，使得此对象只在需要时才会被真正创建。
            使用虚拟代理模式的好处就是代理对象可以在必要的时候才将被代理的对象加载；代理可以对加载的过程加以必要的优化。
            当一个模块的加载十分耗费资源的情况下，虚拟代理的好处就非常明显。
    保护代理：允许在访问一个对象时有一些附加的内务处理(控制对敏感对象的访问。用来控制真实对象访问时的权限)

应用场景：
    远程代理：为远程对象提供代理
    虚代理：根据需要创建很大的对象
    保护代理：控制对原始对象的访问，用于对象有不同访问权限时

    网络连接、内存和文件中的大对象
"""
from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):
    """真实代理"""

    def __init__(self, filename):
        self.filename = filename
        print("读取文件内容....")
        f = open(filename, 'r')
        self.content = f.read()
        print(self.content)
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, 'w')
        f.write(content)
        f.close()


class VirtualSubject(Subject):
    """虚代理"""

    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)


class ProjectProxy(Subject):
    """保护代理"""
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.get_content()

    def set_content(self, content):
        # 可以进行身份验证，身份验证不通过抛出权限异常
        raise PermissionError("无写入权限！！！")


# subj = RealSubject("test.txt")

subj = VirtualSubject("test.txt")
subj.get_content()
subj.set_content("hello word!!!")

# subj1 = ProjectProxy("test.txt")
# subj1.get_content()
# subj1.set_content("哈哈，写不进去吧！！！")
