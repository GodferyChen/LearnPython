import math


def add(x, y, f):
    return f(x) + f(y)


print(add(-5, 9, abs))

print(add(25, 9, math.sqrt))


def format_name(s):
    return s.capitalize()


print(list(map(format_name, ['adam', 'LISA', 'barT'])))
