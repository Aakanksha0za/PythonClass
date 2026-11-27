# -*- coding: utf-8 -*-
print(" While Loop Demo")

num = 1

while num <= 10:

    if num == 3:
        print("Skipping", num)
        num += 1
        continue 

    if num == 8:
        print("Breaking at", num)
        break 
    print("Number:", num)
    num += 1

else:
    print("Loop completed successfully!")

print("Program Ended")
