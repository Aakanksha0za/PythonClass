# -*- coding: utf-8 -*-
text = "Python Programming"
word = "madam"

print("Original String:", text)
print("-" * 40)

# 1. Length of string
print("1. Length of string:", len(text))

# 2. Uppercase and Lowercase
print("2. Uppercase:", text.upper())
print("   Lowercase:", text.lower())

# 3. Reverse a string
print("3. Reversed string:", text[::-1])

# 4. Palindrome check
print("4. Palindrome check for 'madam':")
if word == word[::-1]:
    print("   Palindrome")
else:
    print("   Not Palindrome")

# 5. Count vowels
vowels = "aeiouAEIOU"
vowel_count = 0
for ch in text:
    if ch in vowels:
        vowel_count += 1
print("5. Vowel count:", vowel_count)

# 6. Count each character
char_count = {}
for ch in text:
    char_count[ch] = char_count.get(ch, 0) + 1
print("6. Character count:", char_count)

# 7. Substring check
print("7. Substring 'Program' exists?")
if "Program" in text:
    print("   Found")
else:
    print("   Not Found")

# 8. Remove spaces
print("8. Remove spaces:", text.replace(" ", ""))

# 9. First and last character
print("9. First character:", text[0])
print("   Last character:", text[-1])

# 10. Word count
words = text.split()
print("10. Word count:", len(words))

# 11. Replace word
print("11. Replace 'Python' with 'Java':", text.replace("Python", "Java"))

# 12. Anagram check
str1 = "listen"
str2 = "silent"
print("12. Anagram check (listen & silent):")
if sorted(str1) == sorted(str2):
    print("   Anagram")
else:
    print("   Not Anagram")

# 13. Remove duplicate characters
dup_text = "programming"
result = ""
for ch in dup_text:
    if ch not in result:
        result += ch
print("13. Remove duplicates:", result)

# 14. Capitalize each word
sentence = "python programming language"
print("14. Title case:", sentence.title())

print("-" * 40)
print("All string programs executed successfully!")