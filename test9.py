# -*- coding: utf-8 -*-
print(" Ammusement Park ")

age = int(input(" Your age: "))
height = int(input("Your height: "))

if age > 10:
    
    if height > 150:
        print("Enjoy the ride! You meet both age and height requirements.")
    else:
        print("Sorry, you cannot ride. You are old enough but too short.")
else:
    print("Sorry, you cannot ride. You do not meet the age requirement.")

