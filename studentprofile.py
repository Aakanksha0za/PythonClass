# -*- coding: utf-8 -*-
name = "Rohan"
age = "15"
marks = 85.5                                 #string
is_pass = "true"

print(name)
print(age)
print(marks)
print(is_pass)

age = int(age)                      #type casting

def update_marks():
    global marks
    bonus = 5          #local variable
    marks = marks + bonus
    
update_marks()
print("Name", name,"Age", age, "Marks", marks, "Pass", is_pass)



