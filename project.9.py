# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:17:52 2026
9. Shopping Cart

Create a Cart class. Products should be stored in a dictionary, and the cart should calculate the total price.
@author: Admin
"""

class Cart:

    def __init__(self):
        # Initialize an empty dictionary to store products (name: price)
        self.items = {}

    def add_item(self, product_name, price):
        """Add a product with its price to the cart."""
        self.items[product_name] = price
        print(f"Added {product_name} (${price:.2f}) to the cart.")

    def remove_item(self, product_name):
        """Remove a product from the cart."""
        if product_name in self.items:
            del self.items[product_name]
            print(f"Removed {product_name} from the cart.")
        else:
            print(f"Item '{product_name}' is not in the cart.")

    def calculate_total(self):
        """Calculate and return the total price of all items."""
        total = sum(self.items.values())
        return total

    def display_cart(self):
        """Display all items in the cart."""
        if not self.items:
            print("Your cart is empty.")
            return

        print("\n--- Shopping Cart ---")
        for product, price in self.items.items():
            print(f"- {product}: ${price:.2f}")
        print("---------------------")

# Example Usage

# Create a new Cart object
my_cart = Cart()

# Add items to the cart
my_cart.add_item("Apple", 0.99)
my_cart.add_item("Milk", 2.49)
my_cart.add_item("Bread", 1.80)

# Display current cart contents
my_cart.display_cart()

# Calculate and print total price
total_price = my_cart.calculate_total()
print(f"Total Price: ${total_price:.2f}\n")

# Remove an item
my_cart.remove_item("Milk")

# Calculate new total
print(f"Updated Total: ${my_cart.calculate_total():.2f}")