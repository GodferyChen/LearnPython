#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Person(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for k, v in kw.items():
            setattr(self, k, v)


xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', job='Student')

print(xiaoming.name)
print(xiaoming.job)
