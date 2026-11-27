# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 21:24:37 2026
10. Employee Analysis — Mixed Challenge

Create an Employee class containing:

* name
* salary
* skills as a set

Store employees in a list.

Write a function that returns a dictionary containing:

* highest-paid employee
* average salary
* all unique skills
@author: Admin
"""

class Employee:

    def __init__(self, name, salary, skills):
        self.name = name
        self.salary = salary
        self.skills = set(skills)  # Store skills as a set


def analyze_employees(employees):
    # Handle empty list case
    if not employees:
        return {"highest_paid": None, "average_salary": 0.0, "all_skills": set()}

    # 1. Find highest-paid employee
    highest_paid = employees[0]
    total_salary = 0
    all_skills = set()

    # 2. Loop through the list to gather all required information
    for emp in employees:
        # Check for highest salary
        if emp.salary > highest_paid.salary:
            highest_paid = emp

        # Add to total salary for average calculation
        total_salary += emp.salary

        # Add employee's skills into the main skills set
        all_skills.update(emp.skills)

    # Calculate average
    average_salary = total_salary / len(employees)

    # Return dictionary
    return {
        "highest_paid": highest_paid,
        "average_salary": average_salary,
        "all_skills": all_skills,
    }


# --- Example Usage ---

# Create list of employees
employee_list = [
    Employee("Alice", 95000, {"Python", "SQL", "Docker"}),
    Employee("Bob", 110000, {"Java", "AWS", "Docker"}),
    Employee("Charlie", 85000, {"Python", "HTML", "CSS"}),
]

# Run function
result = analyze_employees(employee_list)

# Print results
print("Highest Paid Employee:", result["highest_paid"].name)
print("Average Salary:", result["average_salary"])
print("All Unique Skills:", result["all_skills"])