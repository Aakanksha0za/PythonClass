# -*- coding: utf-8 -*-
item = "Shoes"
price = "2000"           #string
discount = 10            #int

price = int(price)

def final_price():
    discount_amount = price*discount/100
    total = price - discount_amount
    print(item, price, discount, "Final Price:", total)
    
final_price()
