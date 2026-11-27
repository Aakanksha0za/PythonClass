# -*- coding: utf-8 -*-
# User inputs (always string by default)
age_str = "30"
salary_str = "45000.75"
name = "Ashwini"

# Type casting
age = int(age_str)
salary = float(salary_str)

print("Name:", name)
print("Age:", age, type(age))
print("Salary:", salary, type(salary))

# Casting back to string
age_text = str(age)
print("Age as string:", age_text, type(age_text))

