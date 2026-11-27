# -*- coding: utf-8 -*-
student = {
    "name": "Ashwini",
    "age": 21,
    "course": "Python"
}

print("Dictionary:", student)

print("\nAccessing Items:")
print("Name:", student["name"])
print("Age:", student["age"])

print("\nChecking if Key Exists:")

if "course" in student:
    print("Course key exists")
else:
    print("Course key does not exist")

if "marks" in student:
    print("Marks key exists")
else:
    print("Marks key does not exist")

print("\nUsing get() Function:")
print("Course:", student.get("course"))
print("Marks:", student.get("marks", "Not Available"))

print("\nUsing items() Function:")
for key, value in student.items():
   print(key, ":", value)

print("\nGetting All Keys:")
for key in student.keys():
    print(key)

print("\nGetting All Values:")
for value in student.values():
    print(value)
