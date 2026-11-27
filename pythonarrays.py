# -*- coding: utf-8 -*-
fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Original Array:")
print(fruits)

print("\nFirst Fruit:", fruits[0])
print("Last Fruit:", fruits[-1])

fruits.append("Grapes")
print("\nAfter Adding Grapes:")
print(fruits)

fruits.insert(2, "Pineapple")
print("\nAfter Inserting Pineapple:")
print(fruits)

fruits.remove("Banana")
print("\nAfter Removing Banana:")
print(fruits)

fruits[1] = "Kiwi"
print("\nAfter Updating Second Element:")
print(fruits)

print("\nTotal Elements:", len(fruits))

print("\nDisplaying All Fruits:")
for fruit in fruits:
    print(fruit)

search = "Mango"
if search in fruits:
    print("\nMango is present in the array.")
else:
    print("\nMango is not present in the array.")

fruits.sort()
print("\nSorted Array:")
print(fruits)

fruits.reverse()
print("\nReversed Array:")
print(fruits)