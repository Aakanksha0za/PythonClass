# -*- coding: utf-8 -*-
items = ["Lipstick", "Perfume",  "Mascara"]

print(items[0])   
print(items[2])   
print(items[-1])

items[2] = "Foundation"
print(items)

items.append("Eyeliner")
print(items)

items.remove("Foundation")
print(items) 

for n in items:
    print(n)
    
  
print(len(items)) 

print("Lipstick" in items)

items.sort()
print(items)        
items.sort(reverse=True)
print(items)

copy = items.copy()
copy.append(2)
print(items, copy)

l1 = ["Perfume"]
l2 = ["Mascara"]
print(l1 + l2)

reversed_items = items[::-1]
print("Reversed:", reversed_items)

shopping_list = ["Apples","Kiwi","Grapes"]
print("\n--- SHOPPING LIST  ---")

shopping_list.append("Orange")
print(shopping_list)

shopping_list.remove("Apples")
shopping_list.pop()
print(shopping_list) 

print(shopping_list)





      

