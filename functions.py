# -*- coding: utf-8 -*-
class Employee:
    def __init__(self,name,department,salary):
        self.name = name
        self.salary = salary
        self.department = department
def grp_by_department(employee):
    result = { }
    for enp in employee:
        if enp.department not in result:
            result[enp.department] = []
        result[enp.department].append(enp.name)
    return result
employee = [Employee("Ajay","HR","10000000"),Employee("Nidhi","Recruitment","1200000"),Employee("Mehul","Finance","900000"),Employee("Riddhi","Accounting","1300000"),Employee("Rupa","Administration","120000"),Employee("Simran","HR","10000000"),Employee("Samira","Recruitment","1500000"),Employee("Siddhi","Marketing","600000"),Employee("Rishi","Finance","5000000"),Employee("Ramona","Administration","120000")]
print(grp_by_department(employee))

        

