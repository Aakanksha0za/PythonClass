# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:20:21 2026
1. Greeting
 Create a function greet(name) that prints:
Hello Aditya
when called with "Aditya".
2. Addition
 Create a function add(a, b) that returns the sum of two numbers.
3. Even/Odd
 Create a function check_even(number) that returns "Even" if the number is even, otherwise "Odd".
4. Maximum
 Create a function find_max(a, b, c) that returns the largest of three numbers.
5. Factorial
 Create a function factorial(n) that calculates the factorial using a for loop.

Level 2 — Functions + Lists
6. List Sum
 Create a function list_sum(numbers) that returns the sum of all elements without using Python’s sum().
Example:
list_sum([10, 20, 30, 40])
Expected:
100
7. Count Even Numbers
 Create a function that accepts a list and returns how many even numbers it contains.
8. Find Largest
 Create a function that accepts a list and returns the largest number without using max().
9. Reverse List
 Create a function that accepts a list and returns the reversed list without using .reverse().

Level 3 — Functions + Dictionary
10. Student Marks
Given:
students = {
    "Aditya": 85,
    "Rahul": 72,
    "Priya": 91,
    "Amit": 65
}
Create a function that finds the student with the highest marks.

11. Word Frequency
Create a function that accepts a sentence and returns a dictionary containing the frequency of each word.
Example:
word_count("python is easy and python is powerful")
Expected:
{
    "python": 2,
    "is": 2,
    "easy": 1,
    "and": 1,
    "powerful": 1
}

Level 4 — Classes
12. Student Class
Create a Student class with:
name
age
marks
Create a method display() that prints all information.

13. Calculator Class
Create a Calculator class with methods:
add()
subtract()
multiply()
divide()
Example:
calc = Calculator()

calc.add(10, 5)
calc.multiply(10, 5)

14. Bank Account
Create a BankAccount class with:
account_holder
balance
Methods:
deposit(amount)
withdraw(amount)
check_balance()
Don’t allow withdrawal if the amount is greater than the balance.

Level 5 — Functions + Classes 🔥
15. Employee Management
Create an Employee class containing:
name
salary
department
Methods:
display()
increase_salary(percent)
Example:
emp = Employee("Aditya", 50000, "IT")

emp.display()
emp.increase_salary(10)
emp.display()

Level 6 — Challenge 🔥🔥
16. Shopping Cart
Create a Product class:
name
price
quantity
Create a ShoppingCart class that can:
add_product()
remove_product()
calculate_total()
display_cart()
Example:
cart = ShoppingCart()

cart.add_product("Laptop", 50000, 1)
cart.add_product("Mouse", 1000, 2)

cart.display_cart()
print(cart.calculate_total())
Expected total:
52000
🔥 Final Challenge
17. Library Management System
Build a small library system using classes.
You should have:
Book
Library
Book should contain:
title
author
available
Library should have methods:
add_book()
display_books()
borrow_book()
return_book()
search_book()
Requirements:
A borrowed book cannot be borrowed again.
A returned book becomes available.
Search should work by title.
Store multiple books in a list.
Use functions/methods, loops, if/else, lists and classes.
This last one is a good mini-project because it combines the Python topics you’ve been practicing.

@author: Admin
"""
def greet(name):
    print(f"Hello {name}")

def add(a, b):
    return a + b

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def list_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def count_evens(numbers):
    count = 0
    for num in numbers:
        if num % 2 == 0:
            count += 1
    return count

def find_largest_in_list(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

def reverse_list(numbers):
    reversed_lst = []
    for i in range(len(numbers) - 1, -1, -1):
        reversed_lst.append(numbers[i])
    return reversed_lst

def highest_scorer(students_dict):
    top_student = None
    max_marks = -1
    for student, marks in students_dict.items():
        if marks > max_marks:
            max_marks = marks
            top_student = student
    return top_student

def word_count(sentence):
    words = sentence.split()
    frequency = {}
    for word in words:
        word = word.lower()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print(f"Student: {self.name} | Age: {self.age} | Marks: {self.marks}")

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New Balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds! Withdrawal denied.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining Balance: ${self.balance}")

    def check_balance(self):
        print(f"Account Holder: {self.account_holder} | Balance: ${self.balance}")


class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display(self):
        print(f"Employee: {self.name} | Dept: {self.department} | Salary: ${self.salary:.2f}")

    def increase_salary(self, percent):
        self.salary += self.salary * (percent / 100)
        print(f"Salary increased by {percent}% for {self.name}.")


class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_product(self, name, price, quantity):
        product = Product(name, price, quantity)
        self.items.append(product)

    def remove_product(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                self.items.remove(item)
                print(f"Removed {name} from cart.")
                return
        print(f"Product '{name}' not found in cart.")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item.price * item.quantity
        return total

    def display_cart(self):
        print("--- Shopping Cart ---")
        for item in self.items:
            print(f"{item.name} - Price: ${item.price} x Qty: {item.quantity}")


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added book: '{title}'")

    def display_books(self):
        print("\n--- Library Books ---")
        if not self.books:
            print("No books available in the library.")
            return
        for book in self.books:
            print(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if book.available:
                    book.available = False
                    print(f"Successfully borrowed: '{book.title}'")
                    return
                else:
                    print(f"Sorry, '{book.title}' is currently unavailable.")
                    return
        print(f"Book '{title}' not found in library.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    print(f"Successfully returned: '{book.title}'")
                    return
                else:
                    print(f"'{book.title}' was not borrowed.")
                    return
        print(f"Book '{title}' not found in library.")

    def search_book(self, title):
        print(f"\nSearch results for '{title}':")
        found = False
        for book in self.books:
            if title.lower() in book.title.lower():
                print(book)
                found = True
        if not found:
            print("No matching books found.")


if __name__ == "__main__":
    print("=== Level 1 ===")
    greet("Aditya")
    print("Add:", add(5, 10))
    print("Check Even:", check_even(7))
    print("Find Max:", find_max(10, 25, 15))
    print("Factorial:", factorial(5))

    print("\n=== Level 2 ===")
    print("List Sum:", list_sum([10, 20, 30, 40]))
    print("Count Evens:", count_evens([1, 2, 3, 4, 6, 7, 8]))
    print("Largest in List:", find_largest_in_list([12, 45, 2, 89, 34]))
    print("Reverse List:", reverse_list([1, 2, 3, 4, 5]))

    print("\n=== Level 3 ===")
    students = {"Aditya": 85, "Rahul": 72, "Priya": 91, "Amit": 65}
    print("Top Student:", highest_scorer(students))
    print("Word Count:", word_count("python is easy and python is powerful"))

    print("\n=== Level 4 ===")
    s1 = Student("Aditya", 20, 85)
    s1.display()

    calc = Calculator()
    print("Calc Add:", calc.add(10, 5))
    print("Calc Multiply:", calc.multiply(10, 5))

    acc = BankAccount("Aditya", 500)
    acc.deposit(200)
    acc.withdraw(800)  
    acc.withdraw(300)  
    acc.check_balance()

    print("\n=== Level 5 ===")
    emp = Employee("Aditya", 50000, "IT")
    emp.display()
    emp.increase_salary(10)
    emp.display()

    print("\n=== Level 6 ===")
    cart = ShoppingCart()
    cart.add_product("Laptop", 50000, 1)
    cart.add_product("Mouse", 1000, 2)
    cart.display_cart()
    print("Total:", cart.calculate_total())

    print("\n=== Final Challenge ===")
    lib = Library()
    lib.add_book("Python Basics", "Guido van Rossum")
    lib.add_book("Clean Code", "Robert C. Martin")
    lib.display_books()
    lib.borrow_book("Python Basics")
    lib.borrow_book("Python Basics")  
    lib.display_books()
    lib.return_book("Python Basics")
    lib.search_book("Clean")

