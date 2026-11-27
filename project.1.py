# -*- coding: utf-8 -*-
shop_timings = ("09:00 AM", "09:00 PM")

product_categories = {"Dairy", "Bakery", "Grains", "Snacks"}

grocery_items = ["Milk", "Bread", "Rice", "Eggs", "Chips"]

item_prices = {
    "Milk": 40,
    "Bread": 35,
    "Rice": 60,
    "Eggs": 6,
    "Chips": 20
}

print("WELCOME TO THE MINI GROCERY SHOP")
print(f" Shop Timings: Opens at {shop_timings[0]} | Closes at {shop_timings[1]}")

print("\n  Our Product Categories:")
for category in product_categories:
    print(f"- {category}")

print("\n Available Items in Shop:")
print(", ".join(grocery_items))

print("\n Stock Management: Add a new product")
new_item = input("Enter the name of the new item: ").strip().capitalize()
new_price = int(input(f"Enter the price for {new_item} (in $): "))
new_category = input(f"Enter the category for {new_item}: ").strip().capitalize()

grocery_items.append(new_item)          
item_prices[new_item] = new_price       
product_categories.add(new_category)    

print("\nUpdated Price List:")
for item, price in item_prices.items():
    print(f" {item}: ${price}")


print("\n  Simulating Customer Shopping Cart...")
customer_cart = [new_item, "Milk", "Bread"] 

print(f"Items in Cart: {', '.join(customer_cart)}")

total_bill = 0
for shopping_item in customer_cart:
    total_bill += item_prices[shopping_item] 

print(f" Total Bill Amount: ${total_bill}")

print("THANK YOU FOR VISITING! COME AGAIN!")