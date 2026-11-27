# -*- coding: utf-8 -*-
age = 17
marks = 78
passing_marks = 40
math = 80
science = 80
roll_number = 23

print("---- Student Report ----")

if age >= 18:
    print("Eligible for exam ")
else:
    print("Not eligible for exam ")

if marks >= passing_marks:
    print("Result: Pass ")
else:
    print("Result: Fail ")

if marks > 85:
    print("Grade: Excellent ")
elif marks >= 50:
    print("Grade: Good ")
else:
    print("Grade: Needs Improvement ")

if math == science:
    print("Math and Science marks are equal ")
else:
    print("Math and Science marks are different ")

if roll_number % 2 == 0:
    print("Roll Number is Even ")
else:
    print("Roll Number is Odd ")

if marks != 100:
    print("Not a full score yet ")

print("-------------------")