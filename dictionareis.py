# -*- coding: utf-8 -*-
student = {
"name": "Rahul",
"age": 12,
"grade": "7th"
}

print("Student Dictionary:")
print(student)

print("\nStudent Name:", student["name"])

student["school"] = "Green Valley School"

student["age"] = 13

print("\nUpdated Dictionary:")
print(student)

student.pop("grade")

print("\nFinal Dictionary:")
print(student)
