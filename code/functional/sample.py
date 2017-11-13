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
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())
