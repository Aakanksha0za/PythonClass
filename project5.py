# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:28:32 2026
Q1. Find the Student with Highest Marks

Given:

students = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Neha": 95,
    "Ravi": 88
}

Write a program to find:

* Student with the highest marks
* Highest marks

Expected output:

Neha 95

⸻

Q2. Count Frequency of Numbers

Given:

numbers = [2, 3, 2, 5, 3, 2, 7, 5, 3, 3]

Create a dictionary that stores how many times each number appears.

Expected output:

{2: 3, 3: 4, 5: 2, 7: 1}

⸻

Q3. Find the Most Expensive Product

products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 8500
}

Write a program to find the product with the highest price.

⸻

Q4. Calculate Total and Average Marks

marks = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "Computer": 95,
    "Hindi": 88
}

Write a program to calculate:

1. Total marks
2. Average marks
3. Highest marks
4. Subject with highest marks

⸻

Q5. Dictionary from Two Lists

Given:

names = ["Rahul", "Aman", "Priya", "Neha"]
marks = [85, 92, 78, 95]

Create:

{
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Neha": 95
}

Restriction: Don’t manually create the dictionary.

⸻

Q6. Separate Even and Odd Numbers

Given:

numbers = [10, 15, 22, 33, 40, 51, 62, 77]

Create a dictionary:

{
    "even": [10, 22, 40, 62],
    "odd": [15, 33, 51, 77]
}

⸻

Q7. Find Duplicate Values

Given:

data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20,
    "f": 40
}

Find which values occur more than once.

Expected output:

10
20

⸻

Q8. Nested Dictionary — Student Result

Given:

students = {
    "Rahul": {"Math": 85, "Science": 90},
    "Aman": {"Math": 92, "Science": 88},
    "Priya": {"Math": 78, "Science": 95}
}

Write a program to calculate the total marks of each student.

Expected output:

Rahul = 175
Aman = 180
Priya = 173

⸻

Q9. Find the Topper from Nested Dictionary 

Using:

students = {
    "Rahul": {"Math": 85, "Science": 90, "English": 80},
    "Aman": {"Math": 92, "Science": 88, "English": 91},
    "Priya": {"Math": 78, "Science": 95, "English": 89}
}

Find:

* Total marks of each student
* Student with the highest total
* Highest total marks

⸻

Q10. Word Frequency Counter 

Given:

sentence = "python is easy and python is powerful and python is popular"

Create a dictionary containing the frequency of every word.

Expected output:

{
    "python": 3,
    "is": 3,
    "easy": 1,
    "and": 2,
    "powerful": 1,
    "popular": 1
}

⸻

Q11. Character Frequency 

Given:

word = "programming"

Create a dictionary showing how many times each character appears.

Expected:

{
    "p": 1,
    "r": 2,
    "o": 1,
    "g": 2,
    "a": 1,
    "m": 2,
    "i": 1,
    "n": 1
}

⸻

Q12. Remove Duplicate Values

Given:

data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20,
    "f": 40
}

Create a new dictionary containing only unique values.

Expected:

{
    "a": 10,
    "b": 20,
    "d": 30,
    "f": 40
}

⸻

Q13. Shopping Cart Problem 

cart = {
    "Laptop": {"price": 50000, "quantity": 1},
    "Mouse": {"price": 800, "quantity": 2},
    "Keyboard": {"price": 1500, "quantity": 1}
}

Calculate the total shopping bill.

Formula:

Total = price × quantity

⸻

Q14. Student Grade System

Given:

students = {
    "Rahul": 85,
    "Aman": 72,
    "Priya": 93,
    "Neha": 64,
    "Ravi": 48
}

Create a new dictionary where grades are assigned according to:

90-100 → A
80-89  → B
70-79  → C
60-69  → D
Below 60 → F

Expected:

{
    "Rahul": "B",
    "Aman": "C",
    "Priya": "A",
    "Neha": "D",
    "Ravi": "F"
}

⸻

Q15. Find the Second Highest Marks

students = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Neha": 95,
    "Ravi": 88
}

Write a program to find the student who has the second-highest marks.

Expected:

Aman 92Q1. Find the Student with Highest Marks

Given:

students = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Neha": 95,
    "Ravi": 88
}

Write a program to find:

* Student with the highest marks
* Highest marks

Expected output:

Neha 95

⸻

Q2. Count Frequency of Numbers

Given:

numbers = [2, 3, 2, 5, 3, 2, 7, 5, 3, 3]

Create a dictionary that stores how many times each number appears.

Expected output:

{2: 3, 3: 4, 5: 2, 7: 1}

⸻

Q3. Find the Most Expensive Product

products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 8500
}

Write a program to find the product with the highest price.

⸻

Q4. Calculate Total and Average Marks

marks = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "Computer": 95,
    "Hindi": 88
}

Write a program to calculate:

1. Total marks
2. Average marks
3. Highest marks
4. Subject with highest marks

⸻

Q5. Dictionary from Two Lists

Given:

names = ["Rahul", "Aman", "Priya", "Neha"]
marks = [85, 92, 78, 95]

Create:

{
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Neha": 95
}

Restriction: Don’t manually create the dictionary.

⸻

Q6. Separate Even and Odd Numbers

Given:

numbers = [10, 15, 22, 33, 40, 51, 62, 77]

Create a dictionary:

{
    "even": [10, 22, 40, 62],
    "odd": [15, 33, 51, 77]
}

⸻

Q7. Find Duplicate Values

Given:

data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20,
    "f": 40
}

Find which values occur more than once.

Expected output:

10
20

⸻

Q8. Nested Dictionary — Student Result

Given:

students = {
    "Rahul": {"Math": 85, "Science": 90},
    "Aman": {"Math": 92, "Science": 88},
    "Priya": {"Math": 78, "Science": 95}
}

Write a program to calculate the total marks of each student.

Expected output:

Rahul = 175
Aman = 180
Priya = 173

⸻

Q9. Find the Topper from Nested Dictionary 

Using:

students = {
    "Rahul": {"Math": 85, "Science": 90, "English": 80},
    "Aman": {"Math": 92, "Science": 88, "English": 91},
    "Priya": {"Math": 78, "Science": 95, "English": 89}
}

Find:

* Total marks of each student
* Student with the highest total
* Highest total marks

⸻

Q10. Word Frequency Counter 

Given:

sentence = "python is easy and python is powerful and python is popular"

Create a dictionary containing the frequency of every word.

Expected output:

{
    "python": 3,
    "is": 3,
    "easy": 1,
    "and": 2,
    "powerful": 1,
    "popular": 1
}

⸻

Q11. Character Frequency 

Given:

word = "programming"

Create a dictionary showing how many times each character appears.

Expected:

{
    "p": 1,
    "r": 2,
    "o": 1,
    "g": 2,
    "a": 1,
    "m": 2,
    "i": 1,
    "n": 1
}

⸻

Q12. Remove Duplicate Values

Given:

data = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20,
    "f": 40
}

Create a new dictionary containing only unique values.

Expected:

{
    "a": 10,
    "b": 20,
    "d": 30,
    "f": 40
}

⸻

Q13. Shopping Cart Problem 

cart = {
    "Laptop": {"price": 50000, "quantity": 1},
    "Mouse": {"price": 800, "quantity": 2},
    "Keyboard": {"price": 1500, "quantity": 1}
}

Calculate the total shopping bill.

Formula:

Total = price × quantity

⸻

Q14. Student Grade System

Given:

students = {
    "Rahul": 85,
    "Aman": 72,
    "Priya": 93,
    "Neha": 64,
    "Ravi": 48
}

Create a new dictionary where grades are assigned according to:

90-100 → A
80-89  → B
70-79  → C
60-69  → D
Below 60 → F

Expected:

{
    "Rahul": "B",
    "Aman": "C",
    "Priya": "A",
    "Neha": "D",
    "Ravi": "F"
}

⸻

Q15. Find the Second Highest Marks

students = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Neha": 95,
    "Ravi": 88
}

Write a program to find the student who has the second-highest marks.

Expected:

Aman 92
@author: Admin
"""
# ==============================================================================
#=============================================================================

# --- Q1. Find the Student with Highest Marks ---
print("--- Q1 Output ---")
students_q1 = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Neha": 95,
    "Ravi": 88
}

highest_marks = 0
top_student = ""

for name in students_q1:
    if students_q1[name] > highest_marks:
        highest_marks = students_q1[name]
        top_student = name

print(top_student, highest_marks)
print()


# --- Q2. Count Frequency of Numbers ---
print("--- Q2 Output ---")
numbers_q2 = [2, 3, 2, 5, 3, 2, 7, 5, 3, 3]
frequency = {}

for x in numbers_q2:
    if x in frequency:
        frequency[x] = frequency[x] + 1
    else:
        frequency[x] = 1

print(frequency)
print()


# --- Q3. Find the Most Expensive Product ---
print("--- Q3 Output ---")
products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000,
    "Printer": 8500
}

highest_price = 0
expensive_product = ""

for item in products:
    if products[item] > highest_price:
        highest_price = products[item]
        expensive_product = item

print(expensive_product, highest_price)
print()


# --- Q4. Calculate Total and Average Marks ---
print("--- Q4 Output ---")
marks_q4 = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "Computer": 95,
    "Hindi": 88
}

total = sum(marks_q4.values())
average = total / len(marks_q4)
highest = max(marks_q4.values())

top_subject = ""
for subject in marks_q4:
    if marks_q4[subject] == highest:
        top_subject = subject

print("Total:", total)
print("Average:", average)
print("Highest Mark:", highest)
print("Top Subject:", top_subject)
print()


# --- Q5. Dictionary from Two Lists ---
print("--- Q5 Output ---")
names_list = ["Rahul", "Aman", "Priya", "Neha"]
marks_list = [85, 92, 78, 95]
student_dict = {}

for i in range(len(names_list)):
    student_dict[names_list[i]] = marks_list[i]

print(student_dict)
print()


# --- Q6. Separate Even and Odd Numbers ---
print("--- Q6 Output ---")
numbers_q6 = [10, 15, 22, 33, 40, 51, 62, 77]
result_q6 = {"even": [], "odd": []}

for x in numbers_q6:
    if x % 2 == 0:
        result_q6["even"].append(x)
    else:
        result_q6["odd"].append(x)

print(result_q6)
print()


# --- Q7. Find Duplicate Values ---
print("--- Q7 Output ---")
data_q7 = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20,
    "f": 40
}

seen_values_q7 = []
duplicates = []

for val in data_q7.values():
    if val in seen_values_q7:
        if val not in duplicates:
            duplicates.append(val)
    else:
        seen_values_q7.append(val)

for x in duplicates:
    print(x)
print()


# --- Q8. Nested Dictionary — Student Result ---
print("--- Q8 Output ---")
students_q8 = {
    "Rahul": {"Math": 85, "Science": 90},
    "Aman": {"Math": 92, "Science": 88},
    "Priya": {"Math": 78, "Science": 95}
}

for name in students_q8:
    total_marks = sum(students_q8[name].values())
    print(name + " =", total_marks)
print()


# --- Q9. Find the Topper from Nested Dictionary ---
print("--- Q9 Output ---")
students_q9 = {
    "Rahul": {"Math": 85, "Science": 90, "English": 80},
    "Aman": {"Math": 92, "Science": 88, "English": 91},
    "Priya": {"Math": 78, "Science": 95, "English": 89}
}

highest_total = 0
topper = ""

for name in students_q9:
    total_marks = sum(students_q9[name].values())
    print(name + " Total:", total_marks)
    
    if total_marks > highest_total:
        highest_total = total_marks
        topper = name

print("Topper:", topper)
print("Highest Total Marks:", highest_total)
print()


# --- Q10. Word Frequency Counter ---
print("--- Q10 Output ---")
sentence = "python is easy and python is powerful and python is popular"
words = sentence.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

print(word_count)
print()


# --- Q11. Character Frequency ---
print("--- Q11 Output ---")
word_q11 = "programming"
char_count = {}

for char in word_q11:
    if char in char_count:
        char_count[char] = char_count[char] + 1
    else:
        char_count[char] = 1

print(char_count)
print()


# --- Q12. Remove Duplicate Values ---
print("--- Q12 Output ---")
data_q12 = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20,
    "f": 40
}

unique_dict = {}
seen_values_q12 = []

for key in data_q12:
    if data_q12[key] not in seen_values_q12:
        unique_dict[key] = data_q12[key]
        seen_values_q12.append(data_q12[key])

print(unique_dict)
print()


# --- Q13. Shopping Cart Problem ---
print("--- Q13 Output ---")
cart = {
    "Laptop": {"price": 50000, "quantity": 1},
    "Mouse": {"price": 800, "quantity": 2},
    "Keyboard": {"price": 1500, "quantity": 1}
}

total_bill = 0

for item in cart:
    price = cart[item]["price"]
    quantity = cart[item]["quantity"]
    total_bill = total_bill + (price * quantity)

print("Total shopping bill:", total_bill)
print()


# --- Q14. Student Grade System ---
print("--- Q14 Output ---")
students_q14 = {
    "Rahul": 85,
    "Aman": 72,
    "Priya": 93,
    "Neha": 64,
    "Ravi": 48
}

student_grades = {}

for name in students_q14:
    score = students_q14[name]
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    student_grades[name] = grade

print(student_grades)
print()


# --- Q15. Find the Second Highest Marks ---
print("--- Q15 Output ---")
students_q15 = {
    "Rahul": 85,
    "Aman": 92,
    "Priya": 78,
    "Neha": 95,
    "Ravi": 88
}

marks_list_q15 = list(students_q15.values())
marks_list_q15.sort(reverse=True)
second_highest_value = marks_list_q15[1]

for name in students_q15:
    if students_q15[name] == second_highest_value:
        print(name, second_highest_value)
print()


# ==============================================================================
#
# ==============================================================================
print("--- Basic Loop Exercises Output ---")

# 3. For loop to print numbers from 1 to 10
print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i)
print()

# 4. While loop to print numbers from 10 to 1
print("Numbers 10 to 1:")
i = 10
while i >= 1:
    print(i)
    i -= 1
print()

# 5. Print even numbers from 1 to 20 without if formula (simplified)
print("Even numbers 1 to 20:")
for i in range(2, 21, 2):
    print(i)
print()

# 6. Multiplication table with user input (W3Schools string concatenation)
print("Multiplication Table:")
num = int(input("Enter a number for the table: "))
for i in range(1, 11):
    print(str(num) + " x " + str(i) + " = " + str(num * i))

