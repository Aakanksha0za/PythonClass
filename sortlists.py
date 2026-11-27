# -*- coding: utf-8 -*
1.
numbers = [4, 2, 7, 1]

numbers.sort()

print("Original list after sort:", numbers)

2.
numbers = [4, 2, 7, 1]

new_list = sorted(numbers)

print("Original list:", numbers)
print("New sorted list:", new_list)

3.
words = ["apple", "kiwi", "banana"]

words.sort(key=len)

print(words)

4.
numbers = [4, 2, 7, 1]

numbers.sort(reverse=True)

print(numbers)

5.
numbers = [5, 1, 9, 3]

new_list = sorted(numbers, reverse=True)

numbers.sort()

print("Original after sort():", numbers)
print("New list using sorted():", new_list)
