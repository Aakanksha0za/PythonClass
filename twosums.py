# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 15:09:29 2026

@author: Admin
"""
def two_sums(nums,target):
  num_map = {}
  for i, num in enumerate (nums):
    complement = target - num
    if complement in num_map:
        return[num_map[complement],i]
    num_map[num] =i
  return[]

nums = [2,7,11,15]
target = 9
result = two_sums(nums,target)
print("Indices:",result)
