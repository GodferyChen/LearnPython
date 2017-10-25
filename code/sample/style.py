#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Chen'


class OldSytle:
    def __init__(self, name, description):
        self.name = name
        self.desciption = description


class NewSytle(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


old = OldSytle('old', "old style class")
print(old)
print(type(old))
print(dir(old))

new = NewSytle('new', 'new style class')
print('------------------------------------------')
print(new)
print(type(new))
print(dir(new))
