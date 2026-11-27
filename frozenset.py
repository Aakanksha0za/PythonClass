set1 = frozenset({"pizza", "burger", "fries", "cola"})
set2 = frozenset({"burger", "cola", "icecream", "cake"})

print("Set 1:", set1)
print("Set 2:", set2)

copy_set = set1.copy()
print("\nCopy of Set1:", copy_set)

diff_set = set1.difference(set2)
print("\nDifference (items only in Set1):", diff_set)

inter_set = set1.intersection(set2)
print("\nIntersection (common items):", inter_set)

print("\nAre Set1 and Set2 disjoint?", set1.isdisjoint(set2))

small_set = frozenset({"burger", "cola"})
print("\nIs small_set subset of Set1?", small_set.issubset(set1))

print("Is Set1 superset of small_set?", set1.issuperset(small_set))

sym_diff = set1.symmetric_difference(set2)
print("\nSymmetric Difference:", sym_diff)

union_set = set1.union(set2)
print("\nUnion of Set1 and Set2:", union_set)
