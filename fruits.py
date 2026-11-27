# -*- coding: utf-8 -*-
fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "potato"]

print("Original Fruits List:", fruits)
print("Vegetables List:", vegetables)

fruits_copy = fruits.copy()

fruits_copy.append("orange")

print("\nAfter Copy and Modify:")
print("Original Fruits:", fruits)
print("Copied Fruits:", fruits_copy)

fruits_slice_copy = fruits[:]
fruits_slice_copy.append("grapes")

print("\nSlicing Copy:")
print("Original Fruits:", fruits)
print("Slice Copy:", fruits_slice_copy)

joined_list_plus = fruits_copy + vegetables

print("\nJoined using + operator:")
print(joined_list_plus)

fruits_extend = fruits.copy()
fruits_extend.extend(vegetables)

print("\nJoined using extend():")
print(fruits_extend)

print("\n--- Final Summary ---")
print("Original Fruits:", fruits)
print("Copy (copy method):", fruits_copy)
print("Copy (slicing):", fruits_slice_copy)
print("Joined (+):", joined_list_plus)
print("Joined (extend):", fruits_extend)
