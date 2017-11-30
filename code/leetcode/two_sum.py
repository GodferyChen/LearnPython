#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    @staticmethod
    def twosum(nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            if nums[i] not in dict:
                dict[nums[i]] = i
