# -*- coding: utf-8 -*-
text = " Hello Python World! "

print("Original Text:", text)

print("Lowercase:", text.lower())

print("Uppercase:", text.upper())

print("Title Case:", text.title())

print("Capitalize:", text.capitalize())

print("Strip:", text.strip())

print("LStrip:", text.lstrip())

print("RStrip:", text.rstrip())

print("Replace:", text.replace("Python", "Coding"))

print("Find 'Python':", text.find("Python"))

print("Count of 'o':", text.count("o"))

print("Starts with 'Hello':", text.strip().startswith("Hello"))

print("Ends with 'World!':", text.strip().endswith("World!"))

print("Split:", text.strip().split(" "))

words = ["I", "love", "Python"]
print("Join:", "-".join(words))

print("Is Alpha:", "Hello".isalpha())

print("Is Digit:", "12345".isdigit())

print("Is Alnum:", "Hello123".isalnum())

print("Swapcase:", text.swapcase())

print("Center:", text.strip().center(30, "*"))

print("Length:", len(text))