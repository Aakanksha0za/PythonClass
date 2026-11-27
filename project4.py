# -*- coding: utf-8 -*-
#Write a program to remove duplicate value forms: numbers=[10,20,10,30,20,40,30,50]
numbers = [10, 20, 10, 30, 20, 40, 30, 50]
duplicate_numbers = []
for x in numbers:
    if x not in duplicate_numbers:
        duplicate_numbers.append(x)
print(duplicate_numbers)

 #Given list of marks: marks=[78,45,89,32,67,91,55] Find the highest, lowest, 
 #Average and the number of students who scored 600 or above
marks = [78, 45, 89, 32, 67, 91, 55]
highest = max(marks)
lowest = min(marks)
average = sum(marks) / len(marks)
count = 0
for x in marks:
    if x >= 600:
        count = count + 1
print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Average mark:", average)
print("Students scoring 600 or above:", count)

#Write a program to reverse a list numbers=[10,20,30,40,50]
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]
common_elements = []
for x in list1:
    if x in list2:
        common_elements.append(x)

print(common_elements)
