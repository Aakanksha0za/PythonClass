# -*- coding: utf-8 -*-
print("=== Python range() Function Demo ===")

print("\n1. Numbers from 0 to 4:")
for i in range(5):
    print(i)

print("\n2. Numbers from 5 to 10:")
for i in range(5, 11):
    print(i)

print("\n3. Even numbers from 2 to 20:")
for i in range(2, 21, 2):
    print(i)

print("\n4. Odd numbers from 1 to 19:")
for i in range(1, 20, 2):
    print(i)

print("\n5. Countdown from 10 to 1:")
for i in range(10, 0, -1):
    print(i)

num = int(input("\nEnter a number for multiplication table: "))

print(f"\nMultiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("\nProgram Completed!")