# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:09:05 2026

@author: Admin
"""

class Vehicle:
  def __init__(self,make,model,year):
    self.make = make
    self.model = model
    self.year = year
    
class ElectricCar(Vehicle):
  def __init__(self,battery_capacity,*args,**kwargs):
    super(). __init__(*args,**kwargs)
    self.battery_capacity = battery_capacity
  def info(self):
    return f"{self.year} {self.make} {self.model} {self.battery_capacity}"
    
class PetrolCar(Vehicle):
  def __init__(self,combustion_engine,*args,**kwargs):
    super(). __init__(*args,**kwargs)
    self.combustion_engine = combustion_engine
  def info(self):
    return f"{self.combustion_engine}"
    
car1 = ElectricCar(85,"Tesla","Model S",2018)
print (car1.info())
car2 = ElectricCar(battery_capacity = 75, make = "Toyota",model = "Fortuner",year = 2012)
print(car2.info())
car3 = PetrolCar( 98,"Toyota","Liva",2012)
print(car3.info())