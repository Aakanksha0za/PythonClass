# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 21:12:11 2026
3. Universal Logging Decorator
Write a function decorator @log_call that wraps any arbitrary function, prints its name along with the exact *args tuple and **kwargs dictionary it was called with, and returns the target function's return value.

Python
# Expected behavior:
@log_call
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice", greeting="Hi")
# Console: "Calling greet with args: ('Alice',), kwargs: {'greeting': 'Hi'}"
# Returns: "Hi, Alice!"
@author: Admin
"""

# Import functools.wraps to preserve the decorated function's metadata (name, docstring, etc.)
from functools import wraps

# Define the decorator function that accepts the target function as its argument
def log_call(func):
    # Apply @wraps so wrapper keeps the original function's name and signature
    @wraps(func)
    # Define the inner wrapper function to catch all positional (*args) and keyword (**kwargs) arguments
    def wrapper(*args, **kwargs):
        # Print the target function's name along with the exact args tuple and kwargs dict
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        # Call the original target function with its arguments and return its output
        return func(*args, **kwargs)
    # Return the wrapper function object to replace the original function definition
    return wrapper


# --- Example Usage ---

# Apply the @log_call decorator to the greet function
@log_call
# Define a standard function taking both positional and keyword arguments
def greet(name, greeting="Hello"):
    # Return the formatted string response
    return f"{greeting}, {name}!"

# Call the decorated function with positional "Alice" and keyword greeting="Hi"
result = greet("Alice", greeting="Hi")
# Print the returned result string to the console
print(result)