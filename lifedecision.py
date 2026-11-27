# -*- coding: utf-8 -*-
print(" DAILY LIFE DECISION SYSTEM ")
print("----------------------------")

attendance = 78
fees_paid = True

age = 17
special_permission = False

light_on = False

degree = True
experience = False
internship = True

is_raining = True
have_umbrella = False

is_holiday = False


print("\n Exam Check")
if attendance > 75 and fees_paid:
    print(" You can write the exam ")
else:
    print(" You cannot write the exam")

print("\n Voting Check")
if age >= 18 or special_permission:
    print(" You can vote")
else:
    print(" You cannot vote")

print("\n Light Status Before:", light_on)
light_on = not light_on
print(" Light Status After:", light_on)

print("\n Job Check")
if degree and (experience or internship):
    print(" You are eligible for job")
else:
    print(" Not eligible for job")

print("\n Holiday Check")
if not is_holiday:
    print(" Go to school")
else:
    print(" Enjoy holiday")

print("\n Weather Check")
if is_raining and not have_umbrella:
    print(" Take umbrella or you will get wet!")
else:
    print(" You are safe!")
    
print("\n All Decisions Completed!")
