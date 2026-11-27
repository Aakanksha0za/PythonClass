# -*- coding: utf-8 -*-
# Creating complex numbers using casting
real_part = 5        # int
imag_part = 7.5      # float

num = complex(real_part, imag_part)

print("Complex number:", num)
print("Type of num:", type(num))

# Casting int and float to complex
a = complex(10)
b = complex(3.2)

print("\nComplex from int:", a)
print("Complex from float:", b)

# Note: Direct casting from string to complex
c = complex("4+6j")
print("\nComplex from string:", c)

