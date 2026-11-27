# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 14:57:26 2026
Create a class where only one object can ever exist.
@author: Admin
"""
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            # Create the single instance if it doesn't exist
            cls._instance = super().__new__(cls)
        return cls._instance

# --- Usage ---
s1 = Singleton()
s2 = Singleton()

print(f"s1 is s2: {s1 is s2}")  # Output: True (both reference the exact same object)
print(f"s1 address: {id(s1)}")
print(f"s2 address: {id(s2)}")
