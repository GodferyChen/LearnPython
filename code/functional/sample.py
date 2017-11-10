import math
from functools import reduce


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 9, abs))

print(add(25, 9, math.sqrt))


def format_name(s):
    return s.capitalize()


print(list(map(format_name, ['adam', 'LISA', 'barT'])))

def prod(x, y):
    return x*y

print(reduce(prod, [2, 4, 5, 7, 12]))

def is_sqr(x):
    r = int(math.sqrt(x))
    return r*r==x

print(list(filter(is_sqr, range(1, 101))))
