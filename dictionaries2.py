# -*- coding: utf-8 -*-
student = {
    "name": "Archisa",
    "age": 14,
    "class": 9,
    "city":"Pune"
}
for key,values in student.items():
    print(key,values)

#2
for key in student:
    print(key)

#3
student["marks"]= 79

#4
student["age"]= 17

#5
student.pop("class")

#6
if "name" in student:
    print("name exists")

#7
subjects ={
    "Subject1":{
        "marks": 90
    },
    "Subject2":{
        "marks": 57
    },
    "Subject3":{
        "marks": 89
    },
    "Subject4":{
        "marks": 32
    },
    "Subject5":{
        "marks": 70
    }
}
total_marks = 0
for e, value in subjects.items():
    for key, marks in value.items():
        total_marks = total_marks+marks
print(total_marks)

#8




