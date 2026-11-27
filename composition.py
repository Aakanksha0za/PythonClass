# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:24:18 2026

@author: Admin
"""

class Engine:
    def __init__(self, horsepower: int, engine_type: str):
        self.horsepower = horsepower
        self.engine_type = engine_type
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.engine_type} engine ({self.horsepower} HP) purrs to life.")
        else:
            print("Engine is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print("Engine stopped.")
        else:
            print("Engine is already off.")


class Car:
    def __init__(self, make: str, model: str, engine: Engine):
        self.make = make
        self.model = model
        
        self.engine = engine

    def start_car(self):
        print(f"Starting the {self.make} {self.model}...")
        
        self.engine.start()

    def stop_car(self):
        print(f"Stopping the {self.make} {self.model}...")
        self.engine.stop()

if __name__ == "__main__":
   
    v6_engine = Engine(horsepower=300, engine_type="V6")

    my_car = Car(make="Toyota", model="Camry", engine=v6_engine)

    my_car.start_car()
    my_car.stop_car()