# -*- coding: utf-8 -*-

name = input("Ruhaan ")
pizza = input("Margarita ")
price = float(input("890"))
qty = int(input(5))

total = price*qty

print("\n---Pizza Receipt---")

print(f"Customer: {name}")
print("Pizza: {}".format(pizza))
print("Quantity: %d" % qty)
print(f"Total Bill: {total:.2f}")
