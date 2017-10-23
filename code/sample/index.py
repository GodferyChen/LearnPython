#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Chen'

import math

#for多层嵌套
print ([100*m+10*n+x for m in range(1,10) for n in range(0,10) for x in range(1,10) if m == x])

#条件过滤
# def toUppers(L):
#     return [x.upper() for x in L if isinstance(x,str)]
#
# print (toUppers(['Hello', 'world', 101]))

#迭代dict
# d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
#
# sum = 0.0
# for k, v in d.items():
#     sum = sum + v
#     print (k,':',v)
# print ('average', ':', sum / len(d))

# d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
#
# sum = 0.0
# for v in d.__iter__():
#     sum = sum + v
# print (sum / len(d))

#迭代
# for i in range(1,101):
#     if i % 7 ==0:
#         print (i)

#对字符串切片
# def firstCharUpper(s):
#     return s[0].upper()+s[1:]
#
# print (firstCharUpper('hello'))
# print (firstCharUpper('sunday'))
# print (firstCharUpper('september'))

#函数 求根公式
# def quadratic_equation(a, b, c):
#     t = math.sqrt((b * b - 4 * a * c))
#     return (-b + t) / (2 * a), (-b - t) / (2 * a)
#
#
# print(quadratic_equation(2, 3, 0))
# print(quadratic_equation(1, -6, 5))

# 函数
# def square_of_sum(L):
#     result = 0
#     for x in L:
#         result = result + x * x
#     return result
#
#
# print(square_of_sum([1, 2, 3, 4, 5]))
# print(square_of_sum([-5, 0, 5, 15, 25]))

# s = set(['Adam', 'Lisa', 'Paul'])
# L = ['Adam', 'Lisa', 'Bart', 'Paul']
# for name in L:
#     if name in s:
#         s.remove(name)
#     else:
#         s.add(name)
# print(s)
