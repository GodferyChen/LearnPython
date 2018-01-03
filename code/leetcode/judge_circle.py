#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    @staticmethod
    def judgeCircle(self, moves):
        x = y = 0
        for move in moves:
            if move == 'U':
                y -= 1
            elif move == 'D':
                y += 1
            elif move == 'L':
                x -= 1
            elif move == 'R':
                x += 1

        return x == y == 0
