# -*- coding: utf-8 -*-
friends = ["Aakanksha", "Simran", "Archisa", "Shivanjali"]

print("Original List:")
print(friends)

print("\nAccessing Items:")
print("First friend:", friends[0])
print("Last friend", friends[-1])

print("\nChanging Item:")
friends[1] = "Brendan"
print("Updated List:", friends)

print("\nAdding Items:")
friends.append("Arya") 
friends.insert(1, "Aanshi") 
print("After Adding:", friends)

print("\nRemoving Items:")
friends.remove("Shivanjali") 
friends.pop() 
print("After Removing:", friends)

print("\nFinal Student List:")
print(friends)


