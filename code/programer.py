#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Chen'

class Programer(object):
    hobby = 'Play computer'

    def __new__(cls, *args, **kwargs):
        # print('call __new__method')
        # print(args)
        return super(Programer, cls).__new__(cls)

    def __init__(self, name, age, weight):
        # print('call __init__method')
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')
        self.__weight = weight

    def __str__(self):
        return '%s is %s years old' % (self.name, self.age)

    def __dir__(self):
        return self.__dict__.keys()

    def __getattribute__(self, item):
        # return getattr(self,item)
        # return self.__dict__[item]
        return super(Programer,self).__getattribute__(item)

    def __setattr__(self, key, value):
        # setattr(self,key,value)
        self.__dict__[key] = value

    def __eq__(self, other):
        if isinstance(other, Programer):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('The type of object must be Programer')

    def __add__(self, other):
        if isinstance(other, Programer):
            return self.age + other.age
        else:
            raise Exception('The type of object must be Programer')

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print('My name is %s \nI am %s years old\n' % (self.name, self._age))


class BackendProgramer(Programer):
    def __init__(self, name, age, weight, language):
        super(BackendProgramer, self).__init__(name, age, weight)
        self.language = language

    def self_introduction(self):
        print('My name is %s \nMy favorite language is %s' % (self.name, self.language))


def introduce(programer):
    if isinstance(programer, Programer):
        programer.self_introduction()


if __name__ == '__main__':
    p1 = Programer('Tim', 23, 120)
    # p2 = Programer('Raki', 25, 130)
    print(p1.name)
    # backend_programer = BackendProgramer("Raki", 25, 130,'Python')
    # introduce(programer)
    # introduce(backend_programer)
