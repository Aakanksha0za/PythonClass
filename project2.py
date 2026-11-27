# -*- coding: utf-8 -*-
lucky_number = 7
current_number = 0

print("--- Starting Lucky Number Finder ---")

while current_number < 10:
    current_number += 1
    
    if current_number == 4:
        print("Skipping unlucky number 4...")
        continue
        
    print("Checking number: " + str(current_number))
    
    if current_number == lucky_number:
        print("Success! Found the lucky number: " + str(lucky_number))
        break

else:
    print("Loop finished! The lucky number was not found.")

print("--- Game Over ---")


