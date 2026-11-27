# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:48:00 2026
Q1. Student Result System

Create a program that stores 5 students in a dictionary. Each student should have:

* A tuple containing marks of 3 subjects
* A set containing their subjects

Use a for loop to calculate total and average marks.

Print:

* Student name
* Total marks
* Average
* "Pass" if average ≥ 40
* "Fail" otherwise

⸻

Q2. Find Common Subjects

Create two sets:

class_a
class_b

Store subjects taken by two classes.

Write a program to display:

* Subjects common to both classes
* Subjects only in Class A
* Subjects only in Class B
* All unique subjects

Use set operators.

⸻

Q3. Remove Duplicate Numbers

Take a list of numbers from the user.

Convert the list into a set to remove duplicates.

Then:

1. Convert the set back into a list.
2. Use a loop to find even numbers.
3. Store the even numbers in a tuple.
4. Print the tuple.

⸻

Q4. Employee Salary Analysis

Create a dictionary containing employee names and their salaries.

Example structure:

employees = {
    "Amit": 45000,
    "Rahul": 60000,
    "Neha": 75000
}

Using a loop:

* If salary ≥ 70000 → "Senior"
* If salary ≥ 50000 → "Middle"
* Otherwise → "Junior"

Store the results in another dictionary.

⸻

Q5. Student Subject Management

Create a dictionary where every student has a set of subjects.

Example:

students = {
    "Amit": {"Python", "Math", "Science"},
    "Rahul": {"Python", "English"},
    "Neha": {"Python", "Math", "English"}
}

Write a program to:

1. Find students who study Python.
2. Find students who study both Python and Math.
3. Find all unique subjects.
4. Find the student having the maximum number of subjects.

⸻

Q6. Shopping Cart

Create a dictionary containing products and prices.

Create a tuple containing products purchased by a customer.

Using a loop:

* Calculate the total bill.
* If total > ₹5000, give 10% discount.
* If total > ₹2000, give 5% discount.
* Otherwise, no discount.

Print the final bill.

⸻

Q7. Even/Odd Number Classification

Create a list of numbers.

Using a loop and if/else:

* Store even numbers in one set.
* Store odd numbers in another set.
* Store numbers divisible by both 3 and 5 in a tuple.

Finally create a dictionary:

{
    "even": ...,
    "odd": ...,
    "divisible_by_3_and_5": ...
}

⸻

Q8. Cricket Player Analysis

Create a dictionary containing player names and a tuple of their scores in 5 matches.

Example:

players = {
    "Virat": (80, 45, 100, 60, 75),
    "Rohit": (50, 90, 40, 110, 60)
}

Write a program to:

* Calculate total runs.
* Calculate average.
* Find the highest score.
* Print "Excellent" if average ≥ 70.
* Print "Good" if average ≥ 50.
* Otherwise print "Needs Improvement".

⸻

Q9. Common Student Names

Create two lists containing names of students from two classes.

Convert them into sets and find:

* Students present in both classes
* Students only in Class A
* Students only in Class B
* Total unique students

Store the final results inside a dictionary.

⸻

Q10. Word Frequency

Take a sentence from the user.

1. Convert the sentence into a list of words.
2. Create a set of unique words.
3. Create a dictionary containing each word and its frequency.
4. Use a for loop.
5. Use if/else where required.

Example:

Input:
python is easy and python is powerful

Expected dictionary concept:

{
    "python": 2,
    "is": 2,
    "easy": 1,
    "and": 1,
    "powerful": 1
}

⸻

Q11. Hospital Patient Analysis

Create a dictionary containing patients.

Each patient should have:

* Name
* Age
* Tuple of test scores
* Set of diseases

Example structure:

patients = {
    "P1": {
        "age": 45,
        "tests": (80, 70, 90),
        "diseases": {"Diabetes", "BP"}
    }
}

Write a program to:

* Calculate average test score.
* Identify patients whose average is above 75.
* Find patients having "Diabetes".
* Find all unique diseases.
* Count the total number of patients.

⸻

Q12. Exam Eligibility System

Create a dictionary containing students.

Each student should contain:

Name
Attendance
Marks
Subjects

Marks should be stored as a tuple and subjects as a set.

A student is eligible if:

Attendance >= 75
AND
Average marks >= 40
AND
Number of subjects >= 3

Print eligible and non-eligible students separately.

⸻

Q13. Inventory Management

Create a dictionary containing products.

Each product should have:

price
quantity
categories

categories should be a set.

Write a program to:

* Calculate inventory value = price × quantity.
* Find products with quantity < 10.
* Find products belonging to "Electronics".
* Find the product with the highest inventory value.
* Calculate total inventory value.

⸻

Q14. Number Analysis System

Take a list of numbers.

Create a program that:

1. Removes duplicates.
2. Finds even numbers.
3. Finds odd numbers.
4. Finds numbers divisible by 3.
5. Finds numbers divisible by both 3 and 5.
6. Finds the largest number.
7. Finds the smallest number.
8. Stores all results in a dictionary.
9. Use a tuple for the final unique numbers.

⸻

Q15. Student Performance Ranking

Create a dictionary containing at least 5 students.

Each student should have a tuple containing marks of 5 subjects.

Your program should:

* Calculate total marks.
* Calculate average.
* Assign grade:
    * A → average ≥ 80
    * B → average ≥ 60
    * C → average ≥ 40
    * F → below 40
* Store grades in a dictionary.
* Find the student with the highest total.
* Find the class average.
* Find students who scored above the class average.

⸻

Q16. Library Management

Create a dictionary where each student has a set of borrowed books.

Create another dictionary containing book prices.

Write a program that:

* Displays books borrowed by each student.
* Finds students who borrowed more than 3 books.
* Finds common books between two students.
* Finds all borrowed books.
* Calculates the total value of books borrowed by each student.
* Applies a fine if the total value exceeds ₹2000.

⸻

Q17. E-Commerce Order System

Create a dictionary containing customers.

Each customer should have a list of orders.

Each order should contain:

(product_name, quantity, price)

Use tuples for individual orders.

Calculate:

* Total amount spent by each customer.
* Number of different products purchased.
* Highest-value order.
* Apply discount:
    * ≥ ₹10,000 → 20%
    * ≥ ₹5,000 → 10%
    * Otherwise → 0%
* Store the final customer bill in another dictionary.

⸻

Q18.Master Challenge

Create a Student Management System using:

* Dictionary
* List
* Tuple
* Set
* for
* if/elif/else
* Arithmetic operators
* Comparison operators
* Logical operators
* Membership operators

The system should allow you to store:

Student Name
Roll Number
Marks
Subjects
Hobbies

Requirements:

1. Marks must be stored as a tuple.
2. Subjects must be stored as a set.
3. Hobbies must be stored as a list.
4. Calculate total and average.
5. Assign grade.
6. Check whether the student studies "Python".
7. Check whether the student has "Cricket" as a hobby.
8. Find the student with the highest average.
9. Find all unique subjects across the class.
10. Display students who passed all subjects.
11. Display students who failed any subject.
12. Store the final result in a dictionary.print("\n--- Q1. Student Result System ---")
@author: Admin
"""
print("\n--- Q1. Student Result System ---")

students_q1 = {
    "Aarav": {"marks": (85, 78, 92), "subjects": {"Math", "Physics", "Chemistry"}},
    "Bhavna": {"marks": (32, 45, 38), "subjects": {"Math", "English", "Biology"}},
    "Chetan": {"marks": (65, 70, 68), "subjects": {"History", "Civics", "English"}},
    "Diyya": {"marks": (25, 30, 40), "subjects": {"Math", "Physics", "Computer"}},
    "Esha": {"marks": (90, 95, 88), "subjects": {"Biology", "Chemistry", "English"}},
}

for student, data in students_q1.items():
    total = sum(data["marks"])
    average = total / len(data["marks"])
    status = "Pass" if average >= 40 else "Fail"

    print(f"Student: {student}")
    print(f"  Total Marks: {total}")
    print(f"  Average: {average:.2f}")
    print(f"  Status: {status}\n")



print("--- Q2. Find Common Subjects ---")

class_a = {"Math", "Physics", "Chemistry", "English"}
class_b = {"Biology", "Chemistry", "English", "Computer"}

common_subjects = class_a & class_b
only_class_a = class_a - class_b
only_class_b = class_b - class_a
all_unique_subjects = class_a | class_b

print("Subjects common to both classes:", common_subjects)
print("Subjects only in Class A:", only_class_a)
print("Subjects only in Class B:", only_class_b)
print("All unique subjects:", all_unique_subjects)



print("\n--- Q3. Remove Duplicate Numbers ---")


raw_numbers = [12, 5, 8, 12, 21, 8, 14, 3, 10, 5]

unique_list = list(set(raw_numbers))

even_list = []
for num in unique_list:
    if num % 2 == 0:
        even_list.append(num)

even_tuple = tuple(even_list)
print("Original List:", raw_numbers)
print("Unique Evens (Tuple):", even_tuple)


print("\n--- Q4. Employee Salary Analysis ---")

employees = {
    "Amit": 45000,
    "Rahul": 60000,
    "Neha": 75000,
    "Pooja": 92000,
    "Suresh": 35000,
}

employee_categories = {}

for name, salary in employees.items():
    if salary >= 70000:
        employee_categories[name] = "Senior"
    elif salary >= 50000:
        employee_categories[name] = "Middle"
    else:
        employee_categories[name] = "Junior"

print("Salary Categories:", employee_categories)

print("\n--- Q5. Student Subject Management ---")

students_q5 = {
    "Amit": {"Python", "Math", "Science"},
    "Rahul": {"Python", "English"},
    "Neha": {"Python", "Math", "English"},
    "Karan": {"History", "Civics"},
}

python_students = [
    name for name, subs in students_q5.items() if "Python" in subs
]
python_and_math_students = [
    name
    for name, subs in students_q5.items()
    if "Python" in subs and "Math" in subs
]

all_subjects_q5 = set()
for subs in students_q5.values():
    all_subjects_q5.update(subs)

max_subject_student = max(students_q5, key=lambda s: len(students_q5[s]))

print("Students studying Python:", python_students)
print("Students studying both Python & Math:", python_and_math_students)
print("All unique subjects across students:", all_subjects_q5)
print("Student with maximum subjects:", max_subject_student)


print("\n--- Q6. Shopping Cart ---")

product_catalog = {
    "Laptop": 55000,
    "Headphones": 2500,
    "Mouse": 800,
    "Keyboard": 1500,
    "Backpack": 1200,
}

purchased_items = ("Headphones", "Mouse", "Keyboard")

total_bill = 0
for item in purchased_items:
    total_bill += product_catalog.get(item, 0)

discount = 0
if total_bill > 5000:
    discount = 0.10
elif total_bill > 2000:
    discount = 0.05

final_payable = total_bill * (1 - discount)

print(f"Subtotal: ₹{total_bill}")
print(f"Discount Applied: {int(discount * 100)}%")
print(f"Final Payable Amount: ₹{final_payable:.2f}")


print("\n--- Q7. Even/Odd Number Classification ---")

numbers_q7 = [10, 15, 22, 30, 45, 60, 7, 11, 90, 33]

even_set = set()
odd_set = set()
div_3_5_list = []

for num in numbers_q7:
    if num % 2 == 0:
        even_set.add(num)
    else:
        odd_set.add(num)

    if num % 3 == 0 and num % 5 == 0:
        div_3_5_list.append(num)

classification_result = {
    "even": even_set,
    "odd": odd_set,
    "divisible_by_3_and_5": tuple(div_3_5_list),
}

print("Classification Result Dictionary:")
print(classification_result)


print("\n--- Q8. Cricket Player Analysis ---")

players = {"Virat": (80, 45, 100, 60, 75), "Rohit": (50, 90, 40, 110, 60)}

for player, scores in players.items():
    total_runs = sum(scores)
    avg_runs = total_runs / len(scores)
    highest_score = max(scores)

    if avg_runs >= 70:
        performance = "Excellent"
    elif avg_runs >= 50:
        performance = "Good"
    else:
        performance = "Needs Improvement"

    print(f"Player: {player}")
    print(f"  Total Runs: {total_runs}")
    print(f"  Average Runs: {avg_runs:.2f}")
    print(f"  Highest Score: {highest_score}")
    print(f"  Performance Tier: {performance}\n")

print("--- Q9. Common Student Names ---")

class_a_students = ["Aarav", "Neha", "Rohan", "Siddharth", "Priya"]
class_b_students = ["Priya", "Amit", "Rohan", "Vikram", "Neha"]

set_a = set(class_a_students)
set_b = set(class_b_students)

student_overlap_analysis = {
    "both_classes": set_a & set_b,
    "only_class_a": set_a - set_b,
    "only_class_b": set_b - set_a,
    "total_unique_students": len(set_a | set_b),
}

print("Student Overlap Analysis Dictionary:")
print(student_overlap_analysis)

print("\n--- Q10. Word Frequency ---")

sentence = "python is easy and python is powerful"
word_list = sentence.lower().split()
unique_words = set(word_list)

frequency_dict = {}

for word in word_list:
    if word in frequency_dict:
        frequency_dict[word] += 1
    else:
        frequency_dict[word] = 1

print("Word Frequency Dictionary:")
print(frequency_dict)

print("\n--- Q11. Hospital Patient Analysis ---")

patients = {
    "P1": {"age": 45, "tests": (80, 70, 90), "diseases": {"Diabetes", "BP"}},
    "P2": {"age": 60, "tests": (60, 65, 58), "diseases": {"Arthritis"}},
    "P3": {
        "age": 35,
        "tests": (85, 88, 92),
        "diseases": {"Diabetes", "Asthma"},
    },
}

high_avg_patients = []
diabetes_patients = []
all_diseases = set()

for pid, info in patients.items():
    avg_score = sum(info["tests"]) / len(info["tests"])
    if avg_score > 75:
        high_avg_patients.append(pid)

    if "Diabetes" in info["diseases"]:
        diabetes_patients.append(pid)

    all_diseases.update(info["diseases"])

print("Patients with Avg Test Score > 75:", high_avg_patients)
print("Patients with Diabetes:", diabetes_patients)
print("All unique diseases registered:", all_diseases)
print("Total registered patients:", len(patients))



print("\n--- Q12. Exam Eligibility System ---")

students_q12 = {
    "Aarav": {
        "attendance": 80,
        "marks": (55, 60, 70),
        "subjects": {"Math", "Physics", "Chemistry"},
    },
    "Bhavna": {
        "attendance": 70,
        "marks": (80, 85, 90),
        "subjects": {"English", "History", "Civics"},
    },
    "Chetan": {
        "attendance": 90,
        "marks": (30, 35, 40),
        "subjects": {"Math", "Physics", "Chemistry"},
    },
    "Divya": {
        "attendance": 85,
        "marks": (75, 80),
        "subjects": {"Biology", "Chemistry"},
    },
}

eligible_students = []
non_eligible_students = []

for name, info in students_q12.items():
    avg_mark = sum(info["marks"]) / len(info["marks"])
    is_eligible = (
        info["attendance"] >= 75
        and avg_mark >= 40
        and len(info["subjects"]) >= 3
    )

    if is_eligible:
        eligible_students.append(name)
    else:
        non_eligible_students.append(name)

print("Eligible Students:", eligible_students)
print("Non-Eligible Students:", non_eligible_students)



print("\n--- Q13. Inventory Management ---")

inventory = {
    "Laptop": {
        "price": 60000,
        "quantity": 8,
        "categories": {"Electronics", "Computers"},
    },
    "Phone": {
        "price": 30000,
        "quantity": 15,
        "categories": {"Electronics", "Mobile"},
    },
    "Desk": {
        "price": 5000,
        "quantity": 5,
        "categories": {"Furniture", "Office"},
    },
    "Monitor": {
        "price": 12000,
        "quantity": 12,
        "categories": {"Electronics", "Accessories"},
    },
}

low_stock_products = []
electronics_products = []
max_inv_val = -1
max_inv_product = ""
total_inventory_value = 0

for item, data in inventory.items():
    inv_value = data["price"] * data["quantity"]
    total_inventory_value += inv_value

    if data["quantity"] < 10:
        low_stock_products.append(item)

    if "Electronics" in data["categories"]:
        electronics_products.append(item)

    if inv_value > max_inv_val:
        max_inv_val = inv_value
        max_inv_product = item

print("Low Stock Products (< 10):", low_stock_products)
print("Electronics Category Products:", electronics_products)
print(f"Product with Highest Inventory Value: {max_inv_product} (₹{max_inv_val})")
print(f"Total Inventory Value: ₹{total_inventory_value}")


print("\n--- Q14. Number Analysis System ---")

raw_nums_q14 = [15, 3, 22, 15, 30, 45, 8, 12, 9, 30]

unique_set_q14 = set(raw_nums_q14)
even_nums = [n for n in unique_set_q14 if n % 2 == 0]
odd_nums = [n for n in unique_set_q14 if n % 2 != 0]
div_3 = [n for n in unique_set_q14 if n % 3 == 0]
div_3_5 = [n for n in unique_set_q14 if n % 3 == 0 and n % 5 == 0]

num_analysis_results = {
    "unique_numbers_tuple": tuple(unique_set_q14),
    "even_numbers": even_nums,
    "odd_numbers": odd_nums,
    "divisible_by_3": div_3,
    "divisible_by_3_and_5": div_3_5,
    "largest_number": max(unique_set_q14),
    "smallest_number": min(unique_set_q14),
}

print("Number Analysis System Output:")
print(num_analysis_results)


print("\n--- Q15. Student Performance Ranking ---")

student_marks = {
    "Aarav": (85, 90, 88, 92, 80),
    "Bhavna": (60, 65, 70, 58, 62),
    "Chetan": (40, 45, 50, 42, 38),
    "Divya": (30, 35, 25, 40, 32),
    "Esha": (95, 92, 98, 91, 94),
}

student_grades = {}
student_totals = {}
total_class_marks = 0

for name, marks in student_marks.items():
    total = sum(marks)
    avg = total / len(marks)

    student_totals[name] = total
    total_class_marks += avg

    if avg >= 80:
        student_grades[name] = "A"
    elif avg >= 60:
        student_grades[name] = "B"
    elif avg >= 40:
        student_grades[name] = "C"
    else:
        student_grades[name] = "F"

top_student = max(student_totals, key=student_totals.get)
class_average = total_class_marks / len(student_marks)

above_class_avg = [
    name
    for name, marks in student_marks.items()
    if (sum(marks) / len(marks)) > class_average
]

print("Assigned Grades:", student_grades)
print(
    f"Highest Total Scorer: {top_student} with {student_totals[top_student]} marks"
)
print(f"Overall Class Average Score: {class_average:.2f}")
print("Students Scoring Above Class Average:", above_class_avg)


print("\n--- Q16. Library Management ---")

borrowed_books = {
    "Aarav": {"Python", "Physics", "Math", "Chemistry"},
    "Bhavna": {"History", "English"},
    "Chetan": {"Python", "Math", "Data Structures", "Algorithms"},
}

book_prices = {
    "Python": 600,
    "Physics": 500,
    "Math": 450,
    "Chemistry": 550,
    "History": 300,
    "English": 250,
    "Data Structures": 700,
    "Algorithms": 800,
}

print("Borrowed Books by Student:")
for student, books in borrowed_books.items():
    print(f"  {student}: {books}")

more_than_3_books = [s for s, b in borrowed_books.items() if len(b) > 3]
common_between_a_c = borrowed_books["Aarav"] & borrowed_books["Chetan"]

all_borrowed_books = set()
for books in borrowed_books.values():
    all_borrowed_books.update(books)

print("\nStudents who borrowed > 3 books:", more_than_3_books)
print("Common books between Aarav and Chetan:", common_between_a_c)
print("All unique borrowed books:", all_borrowed_books)

print("\nValue Breakdown & Fines:")
for student, books in borrowed_books.items():
    total_val = sum(book_prices.get(b, 0) for b in books)
    fine = 100 if total_val > 2000 else 0
    print(f"  {student} -> Value: ₹{total_val} | Fine Applied: ₹{fine}")


print("\n--- Q17. E-Commerce Order System ---")

customer_orders = {
    "Aarav": [("Laptop", 1, 60000), ("Mouse", 2, 800)],
    "Bhavna": [("Shirt", 3, 1200), ("Jeans", 1, 2000)],
    "Chetan": [("Phone", 1, 8000)],
}

final_customer_bills = {}

for customer, orders in customer_orders.items():
    total_spent = 0
    unique_products = set()
    highest_order_val = 0

    for product, qty, price in orders:
        order_cost = qty * price
        total_spent += order_cost
        unique_products.add(product)

        if order_cost > highest_order_val:
            highest_order_val = order_cost

    if total_spent >= 10000:
        discount_rate = 0.20
    elif total_spent >= 5000:
        discount_rate = 0.10
    else:
        discount_rate = 0.0

    final_amount = total_spent * (1 - discount_rate)

    final_customer_bills[customer] = {
        "gross_total": total_spent,
        "products_count": len(unique_products),
        "highest_order_val": highest_order_val,
        "discount_applied": f"{int(discount_rate * 100)}%",
        "final_bill": final_amount,
    }

print("E-Commerce Final Billing Analysis:")
for cust, bill in final_customer_bills.items():
    print(f"  {cust}: {bill}")


print("\n--- Q18. Master Challenge ---")

master_students = {
    101: {
        "name": "Aarav",
        "marks": (85, 92, 78, 88),  # Tuple
        "subjects": {"Python", "Math", "Physics", "Chemistry"},  # Set
        "hobbies": ["Cricket", "Chess", "Coding"],  # List
    },
    102: {
        "name": "Bhavna",
        "marks": (35, 45, 50, 40),
        "subjects": {"English", "History", "Civics", "Math"},
        "hobbies": ["Singing", "Reading"],
    },
    103: {
        "name": "Chetan",
        "marks": (90, 88, 95, 92),
        "subjects": {"Python", "Math", "Data Science", "AI"},
        "hobbies": ["Cricket", "Gaming"],
    },
    104: {
        "name": "Divya",
        "marks": (70, 75, 32, 80),
        "subjects": {"Python", "Physics", "Math", "Biology"},
        "hobbies": ["Painting", "Dance"],
    },
}

master_system_summary = {}

highest_avg = -1.0
top_student_name = ""
all_system_subjects = set()
students_passed_all = []
students_failed_any = []

for rno, data in master_students.items():
    total = sum(data["marks"])
    avg = total / len(data["marks"])

    if avg >= 80:
        grade = "A"
    elif avg >= 60:
        grade = "B"
    elif avg >= 40:
        grade = "C"
    else:
        grade = "F"

    if avg > highest_avg:
        highest_avg = avg
        top_student_name = data["name"]

    all_system_subjects.update(data["subjects"])

    failed_subjects = [m for m in data["marks"] if m < 40]
    if len(failed_subjects) == 0:
        students_passed_all.append(data["name"])
    else:
        students_failed_any.append(data["name"])

    studies_python = "Python" in data["subjects"]
    plays_cricket = "Cricket" in data["hobbies"]

    master_system_summary[rno] = {
        "name": data["name"],
        "total": total,
        "average": round(avg, 2),
        "grade": grade,
        "studies_python": studies_python,
        "plays_cricket": plays_cricket,
    }

print("--- Master System Summary ---")
for rno, record in master_system_summary.items():
    print(f"Roll No: {rno} -> {record}")

print("\n--- Analytics Breakdown ---")
print(
    f"Student with Highest Average: {top_student_name} ({highest_avg:.2f} avg)"
)
print("All Unique Subjects Across System:", all_system_subjects)
print("Students Passed All Subjects:", students_passed_all)
print("Students Failed Any Subject:", students_failed_any)
