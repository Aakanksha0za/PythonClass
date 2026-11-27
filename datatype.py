# -*- coding: utf-8 -*-
age = 25
print("Age:", age)                # Integer data type
print("Type of age:", type(age))

height = 5.7
print("\nHeight:", height)
print("Type of height:", type(height))              # Float data type

name = "Ashwini"
print("\nName:", name)                 # String data type
print("Type of name:", type(name))

age_float = float(age)
print("\nAge after casting int to float:", age_float)
print("Type:", type(age_float))             # int to float

height_int = int(height)   # decimal part is removed
print("\nHeight after casting float to int:", height_int)           # int to string
print("Type:", type(height_int))

age_str = str(age)
print("\nAge after casting int to string:", age_str)
print("Type:", type(age_str))

number_str = "100"
number_int = int(number_str)                   # string to int
print("\nString to int:", number_int)
print("Type:", type(number_int))

price_str = "249.50"
price_float = float(price_str)                    # string to float
print("\nString to float:", price_float)
print("Type:", type(price_float))
