# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:56:29 2026
11. Filter products by price

products = [
    ("Laptop", 80000),
    ("Mouse", 500),
    ("Keyboard", 1500),
    ("Monitor", 15000)
]

Use lambda and filter() to find products costing more than 5000.

Expected:

[
    ("Laptop", 80000),
    ("Monitor", 15000)
]

12. Use map() + filter() together

Given:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Using lambda, filter() and map(), find the squares of only the even numbers.

Expected:

[4, 16, 36, 64, 100]
@author: Admin
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_squares = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))

print(even_squares)