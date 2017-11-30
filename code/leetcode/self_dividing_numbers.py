#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    @staticmethod
    def selfDividingNumbers(left, right):
        def check(num):
            digits = set(map(int, str(num)))
            if 0 in digits: return False
            return not any(num % d for d in digits)

        return filter(check, range(left, right + 1))


if __name__ == '__main__':
    dict = Solution().selfDividingNumbers(1, 22)
    print(list(dict))
