# -*- coding: utf-8 -*-
"""
@File        : multiSingleton.py
@Author      : wangliang
@Time        : 2022/5/28 7:57
@Description : 多线程单例
"""
import time
import threading


class MultiSingleton:
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        time.sleep(0.05)

        with cls._lock:
            if not hasattr(cls, "_instance"):
                time.sleep(0.05)
                cls._instance = super(MultiSingleton, cls).__new__(cls)

            return cls._instance


def task():
    s = MultiSingleton()
    print(id(s))


for i in range(100):
    t = threading.Thread(target=task)
    t.start()
