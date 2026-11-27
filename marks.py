# -*- coding: utf-8 -*-
marks = [85, 42, 78, 90, 66]

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)

highest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

print("Highest Marks:", highest)