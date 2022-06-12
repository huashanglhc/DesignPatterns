#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：DesignModel 
@File    ：proxy03.py
@Author  ：WL
@Date    ：2022/6/12 18:07 
@Describe:
应用场景：访问某个网站并没有访问权限。可以通过代理去访问这个网站，然后代理把内容传给你。

正向代理：客户端访问某网站，先访问代理，代理去访问某网站，然后把内容返回给客户端，这就是正向代理。

反向代理：客户端去访问某个网站的某个资源，但这个网站没有这个资源，同时这个网站被设置为反向代理，
    那么这个网站就会从其他服务器上获取这个资源返回给客户端。因此客户端并不知道这个资源是谁提供的，
    它只要知道代理网站的网站即可。比如我们访问百度，背后有成千上万的反向代理服务器在为我们服务，
    但我们只要知道baid.com这个网站就行了，不必知道访问的资料具体来自哪里。nginx是高流量web服务器流行选择，
    它支持反向代理和负载均衡。

"""


# author guoyibo
class Cache(object):
    """
    use for save source that ofen is requested
    """

    def __init__(self):
        self.cache = {}

    def get(self, key):
        return self.cache.get(key)

    def set(self, key, value):
        self.cache[key] = value
        print('set %s to %s' % (value, key))


cache = Cache()


class Source(object):
    def __init__(self, name):
        self.name = name

    @property
    def obtain(self):
        print('get source from source')
        return 'source of %s' % self.name


class SourceProxy(object):
    def __init__(self, source):
        self.source = source

    @property
    def obtain(self):
        content = cache.get(self.source.name)

        if not content:
            content = self.source.obtain
            cache.set(self.source.name, content)
        else:
            print('get source from cache')
        return content


class Client(object):

    def __init__(self, source):
        self.source = source

    def show(self):
        print('from backend get source %s' % self.source.obtain)


if __name__ == '__main__':
    source = Source('picture.jpg')
    proxy = SourceProxy(source)
    # first visit
    client = Client(proxy)
    client.show()
    # second visit
    print('*' * 20)
    client.show()


