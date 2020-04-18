# -*- coding: utf-8 -*-

from collections import OrderedDict


def fib(n):
    """斐波那契 使用递归时间复杂度
        O(2^n)
    """
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

"""
写一个装饰器来优化，使用一个字典来记录计算过的值
"""

def cache(fun):
    store = dict()

    def wrapper(n):
        if n in store:
            return store[n]
        else:
            value = fun(n)
            store[n] = value
            return value
    return wrapper

@cache
def f(n):
    if n <= 1:
        return n
    return f(n-1) + f(n-2)

#for i in range(1,35):
#     print(f(i))


class LRUCache():
    def __init__(self, capcity=128):
        self.capcity = capcity
        self.od = OrderedDict()

    def get(self, key, default=None):
        val = self.od.get(key, default)
        self.od.move_to_end(key)
        return val

    def add_or_update(self, key, value):
        if key in self.od:
            self.od[key] = value
            self.od.move_to_end(key)
        else:
            self.od[key] = value
            if len(self.od) > self.capcity:
                self.od.popitem(last=False)

    def __call__(self, func):
        def _(n):
            if n in self.od:
                return self.get(n)
            else:
                val = func(n)
                self.add_or_update(n, val)
                return val
        return _


@LRUCache(10)
def f_use_lru(n):
    if n <= 1:  # 0 or 1
        return n
    return f_use_lru(n - 1) + f_use_lru(n - 2)


def test():
    import time
    beg = time.time()
    for i in range(34):
        print(f(i))
    print(time.time() - beg)
    beg = time.time()
    for i in range(34):
        print(f_use_lru(i))
    print(time.time() - beg)

if __name__ == '__main__':
    test()
