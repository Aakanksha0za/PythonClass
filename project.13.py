# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:50:53 2026
3. Abstraction + Polymorphism
Question

Create an abstract Payment class. Implement:

CreditCardPayment
UPIPayment
PayPalPayment

Each class must implement pay() differently.
@author: Admin
"""

from abc import ABC, abstractmethod


# Abstract Base Class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):

    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print("Processing Credit Card Payment...")
        print(
            f"Paid ${amount} using Credit Card ending in {self.card_number[-4:]}.\n"
        )


class UPIPayment(Payment):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print("Processing UPI Payment...")
        print(f"Paid ${amount} using UPI ID: {self.upi_id}.\n")


class PayPalPayment(Payment):

    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print("Processing PayPal Payment...")
        print(f"Paid ${amount} using PayPal account: {self.email}.\n")


# Demonstration
payments = [
    CreditCardPayment("1234567890123456"),
    UPIPayment("alex@upi"),
    PayPalPayment("alex@example.com"),
]

for payment in payments:
    payment.pay(100)