# -*- coding: utf-8 -*-
# Input string
text = "PythonProgramming"

print("Original String:", text)
print("-" * 30)

# -------- STRING SLICING --------
print("STRING SLICING EXAMPLES")

print("First 6 characters:", text[0:6])      # Python
print("Characters from index 6 to 17:", text[6:17])  # Programming
print("Last 11 characters:", text[-11:])     # Programming
print("Every second character:", text[::2])  # PtoPormig
print("Reverse string:", text[::-1])          # gnimmargorPnohtyP

print("-" * 30)

# -------- STRING CONCATENATION --------
print("STRING CONCATENATION EXAMPLES")

str1 = "Hello"
str2 = "World"
str3 = "Python"

# Using + operator
result1 = str1 + " " + str2
print("Concatenation using + :", result1)

# Concatenating sliced strings
slice1 = text[0:6]        # Python
slice2 = text[6:]         # Programming
result2 = slice1 + " " + slice2
print("Concatenation of sliced strings:", result2)

# Using f-string
result3 = f"{str1}, welcome to {str3}!"
print("Concatenation using f-string:", result3)

print("-" * 30)
print("Program Completed")