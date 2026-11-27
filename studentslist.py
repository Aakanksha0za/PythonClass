# -*- coding: utf-8 -*-
students = ["Aarav", "Diya", "Rohan", "Meera"]

print("Original List:")
print(students)

print("\nAccessing Items:")
print("First student:", students[0])
print("Last student:", students[-1])

print("\nChanging Item:")
students[1] = "Anaya"
print("Updated List:", students)

print("\nAdding Items:")
students.append("Kabir") 
students.insert(1, "Ishaan") 
print("After Adding:", students)

print("\nRemoving Items:")
students.remove("Rohan") 
students.pop() 
print("After Removing:", students)

print("\nFinal Student List:")
print(students)