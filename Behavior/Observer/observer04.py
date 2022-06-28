#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：observer04.py
@Author  ：WL
@Date    ：2022/6/28 15:45 
@Describe: 观察者模式

推模型：主题对象向观察者推送主题的详细信息，不管观察者是否需要，推送的信息通常是主题对象的全部或部分数据。
拉模型： 主题对象在通知观察者的时候，只传递少量信息。如果观察者需要更具体的信息，由观察者主动到主题对象中获取，
        相当于是观察者从主题对象中拉数据。 一般这种模型的实现中，会把主题对象自身通过update()方法传递给观察者，
        这样在观察者需要获取数据的时候，就可以通过这个引用来获取了。

两者区别：
    推模式的Observer模式的好处：
            当有消息时，所有的观察者都会直接得到全部的消息，并进行相应的处理程序，与主体对象没什么关系，
        两者之间的关系是一种松散耦合。
    缺陷：
        所有的观察者得到的消息是一样的，也许有些信息对某个观察者来说根本就用不上，也就是观察者不能“按需所取”；
        当通知消息的参数有变化时，所有的观察者对象都要变化。

    拉模式：
        由观察者自己主动去取消息，需要什么信息，就可以取什么，不会像推模式那样得到所有的消息参数
"""
# 拉模型
from abc import ABCMeta, abstractmethod


class NewsPublisher:  # subject
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detach(self):
        return self.__subscribers.pop()

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return 'Got News:' + self.__latestNews


class Subscriber(metaclass=ABCMeta):  # Observer

    @abstractmethod
    def update(self):
        pass


class ConcreteSubscriber1:  # ConcreteObserver
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class ConcreteSubscriber2:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


news_publisher = NewsPublisher()
for Subscribers in [ConcreteSubscriber1, ConcreteSubscriber2]:  # 创建观察者对象
    Subscribers(news_publisher)

news_publisher.addNews('HELLO WORLD')
news_publisher.notifySubscribers()
news_publisher.detach()
news_publisher.addNews('SECOND NEWS')
news_publisher.notifySubscribers()
