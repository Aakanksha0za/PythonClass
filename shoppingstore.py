# -*- coding: utf-8 -*-
store = {
    "Rice": {
        "price": 50,
        "stock": 20
    },

    "Milk": {
        "price": 30,
        "stock": 15
    },

    "Sugar": {
        "price": 45,
        "stock": 10
    }
}

print("===== SUPERMARKET MENU =====")

print("\nPrice of Rice:", store["Rice"]["price"])
print("Stock of Milk:", store["Milk"]["stock"])

print("\nSugar details:", store.get("Sugar"))

item = "Rice"

if item in store:
    print("\n", item, "is available in store")
else:
    print(item, "not found")

store["Oil"] = {
    "price": 120,
    "stock": 8
}

print("\nOil added successfully!")

store["Rice"]["stock"] = 25

print("\nRice stock updated!")

print("\n===== STORE ITEMS =====")

for product, details in store.items():

    print("\nProduct:", product)

    for key, value in details.items():
        print(key, ":", value)

removed_item = store.pop("Milk")

print("\nMilk removed from store")
print("Removed details:", removed_item)

last_item = store.popitem()

print("\nLast inserted item removed:")
print(last_item)

print("\n===== FINAL STORE DATA =====")

for product, details in store.items():

    print("\nProduct:", product)

    for key, value in details.items():
        print(key, ":", value)


