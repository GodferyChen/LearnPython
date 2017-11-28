#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math
from functools import reduce
import functools


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 9, abs))

print(add(25, 9, math.sqrt))


def format_name(s):
    return s.capitalize()


print(list(map(format_name, ['adam', 'LISA', 'barT'])))


def prod(x, y):
    return x * y


print(reduce(prod, [2, 4, 5, 7, 12]))


def is_sqr(x):
    r = int(math.sqrt(x))
    return r * r == x


print(list(filter(is_sqr, range(1, 101))))


def cmp_ignore_case(s1, s2):
    x = s1
    y = s2
    x = x.lower()
    y = y.lower()
    if x < y:
        return -1

    if x > y:
        return 1

    if x == y:
        return 0


print(list(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)))


# python中返回函数
def calc_prod(lst):
    def lazy_prod():
        def f(x, y):
            return x * y

        return reduce(f, lst, 1)

    return lazy_prod


f = calc_prod([1, 2, 3, 4])
print(f())


# python中闭包
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g

        r = f(i)
        fs.append(r)
    return fs


f1, f2, f3 = count()
print(f1(), f2(), f3())


# Python 中的匿名函数
def is_not_empty(s):
    return s and len(s.strip()) > 0


print(list(filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])))
print(list(filter(lambda s: s and len(s.strip()) > 0, ['test', None, '', 'str', '  ', 'END'])))

# python中编写无参数decorator
import time


def performance(f):
    def fn(*args, **kw):
        t1 = time.time()
        r = f(*args, **kw)
        t2 = time.time()
        print('call %s() in %fs' % (f.__name__, (t2 - t1)))
        return r

    return fn


@performance
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))

# python中编写带参数decorator
import time


def performance(unit):
    def perf_decorator(f):
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r

        return wrapper

    return perf_decorator


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))

# python中完善decorator
import time, functools


def performance(unit):
    def perf_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r

        return wrapper

    return perf_decorator


@performance('ms')
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial.__name__)

# python中的偏函数
import functools

sorted_ignore_case = functools.partial(sorted, key=str.lower)

print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))

# 导包
from os.path import isdir, isfile

print(isdir(r'/data/webroot/resource/python'))
print(isfile(r'/data/webroot/resource/python/test.txt'))

# python中动态导入模块
try:
    import json as json
except ImportError:
    import simgplejson as json

print(json.dumps({'python': 2.7}))

# python之使用__future__

s = 'am I an unicode?'
# print(isinstance(s, unicode))
