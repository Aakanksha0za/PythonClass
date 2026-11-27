# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:55:07 2026

@author: Admin
"""

class Employee:

    def calculate_salary(self):
        return 50000


class Developer(Employee):

    def calculate_salary(self):
        salary = super().calculate_salary()
        return salary + 20000


class SeniorDeveloper(Developer):

    def calculate_salary(self):
        salary = super().calculate_salary()
        return salary + 30000


employee = SeniorDeveloper()

print(employee.calculate_salary())