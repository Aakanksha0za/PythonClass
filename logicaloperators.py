# -*- coding: utf-8 -*-
print(" Gaming Club Entry Checker ")

age = int(input("Enter your age: "))
score = int(input("Enter your game score: "))
membership = input("Are you a member? (yes/no): ").lower()

if age >= 10 and age <= 18:
    print(" Age requirement passed!")

    if score >= 80 or membership == "yes":
        print(" You qualify for the gaming tournament!")

        if not (score < 50):
            print(" You can compete for prizes!")
        else:
            print(" You can play, but not for prizes.")
    else:
        print(" Need score 80+ or membership.")
else:
    print(" Age requirement not met.")