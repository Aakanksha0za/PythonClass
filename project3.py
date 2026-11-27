# -*- coding: utf-8 -*-
# Use a for loop to print numbers from 1 to 10
i = 10
while i >= 1:
    print(i)
    i -= 1
#Use a while loop to print numbers from 10 to 1    
i = 10
while i >= 1:
    print(i)
    i -= 1
# Print all the even numbers from 1 to 20 using a loop and if condition    
for i in range(2, 21, 2):
    print(i)
    
 # Take a number from the user and print its multiplication table from 1 to 10       
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(str(num) + " x " + str(i) + " = " + str(num * i))
    


