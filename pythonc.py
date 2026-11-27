# -*- coding: utf-8 -*-


def unique_subjects(students):
  return list({subject
                for student in students
                for subject in student['subjects']
                })

student_data = [ 
   {"name":"Alice", "subjects":["Maths","Physics","Chemistry"]},
   {"name":"Lia", "subjects":["English","Physics","Maths"]},
   {"name":"Ruth","subjects":["Chemistry","History","Physics"]},
   {"name":"ELizabeth","subjects":["Geography","Maths","Chemistry"]}
 ] 
print(unique_subjects(student_data))

#OR

class Student:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects


def all_subjects(students):
    subjects = set()

    for student in students:
        subjects.update(student.subjects)

    return subjects


students = [
    Student("Aditya", ["Python", "SQL", "Java"]),
    Student("Rahul", ["Python", "AWS"]),
    Student("Neha", ["SQL", "Docker"])
]

print(all_subjects(students))