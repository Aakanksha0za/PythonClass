# -*- coding: utf-8 -*-
name = "PYTHON"

print("Looping through a string:")

for letter in name:

    if letter == "T":
        print("Skipping:", letter)
        continue

    if letter == "H":
        pass 

        print("Current letter:", letter)

print("\nUsing range function:")

for num in range(1, 6):

    if num == 4:
        print("Stopping at:", num)
        break

        print("Number:", num)

    else:
        print("Loop completed successfully")
    
        print("\nNested for loops:")

for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
        print()

print("\nProgram Finished")