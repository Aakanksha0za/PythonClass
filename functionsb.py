# -*- coding: utf-8 -*-
class BankAccount:
  def __init__(self,initial_balance = 0 ):
    self.balance = initial_balance
  
  def deposit(self,amount):
    self.balance+= amount
    return self.balance
  def withdraw(self,amount):
    if amount>self.balance:
      print(f"Insufficent money!(Requested: {amount} Available:{self.balance}")
    else:
      self.balance-= amount
    return self.balance
    
def process_transactions(account, transactions):
    for action, amount in transactions:
        if action == "deposit":
            account.deposit(amount)
        elif action == "withdraw":
            account.withdraw(amount)
            
    return account.balance

acc = BankAccount(200)
money =[
  ("deposit",50),
  ("withdraw",130),
  ("deposit",10),
  ("withdraw",20),
]

final_balance = process_transactions(acc, money)
print(f"Final Balance: {final_balance}")                                 


