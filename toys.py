# -*- coding: utf-8 -*-
toys_anna = {"Teddy", "Car", "Ball", "Robot"}
toys_ben = {"Ball", "Robot", "Doll", "Train"}

print("Anna's Toys:", toys_anna)
print("Ben's Toys:", toys_ben)

all_toys = toys_anna.union(toys_ben)
print("\n Union (All Toys):", all_toys)

toys_copy = toys_anna.copy()
toys_copy.update(toys_ben)
print("\n Update (Anna gets all toys):", toys_copy)

common_toys = toys_anna.intersection(toys_ben)
print("\n Intersection (Same Toys):", common_toys)

anna_only = toys_anna.difference(toys_ben)
print("\n Difference (Only Anna's Toys):", anna_only)

different_toys = toys_anna.symmetric_difference(toys_ben)
print("\n Symmetric Difference (Different Toys):", different_toys)