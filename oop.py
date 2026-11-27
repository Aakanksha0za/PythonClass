# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 09:51:39 2026

@author: Admin
"""

class BankAccount:

    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")

        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")

        if amount > self._balance:
            raise ValueError("Insufficient balance")

        self._balance -= amount


account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)

print(account.balance)