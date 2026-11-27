# -*- coding: utf-8 -*-
student1 = ("Arjun", 85, 90, 88)
student2 = ("Meera", 78, 82, 80)
student3 = ("Rahul", 92, 88, 95)

students = (student1, student2, student3)

for student in students:
    name = student[0]
maths = student[1]
science = student[2]
english = student[3]

total = maths + science + english
average = total / 3

print("Name:", name)
print("Marks:", maths, science, english)
print("Total:", total)
print("Average:", average)
print("---------------------------------------")
