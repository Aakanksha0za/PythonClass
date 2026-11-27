# Python program using slicing and concatenation

name = input("Aakanksha ")
word1 = input("Cat ")
word2 = input("Dog ")

# Slicing examples
first_two = name[:2]
last_two = name[-2:]
reverse_name = name[::-1]

# Concatenation examples
magic_name = first_two + "⭐" + last_two
secret_word = word1[:3] + word2[-3:]

# Output
print("\n--- Results ---")
print("First two letters of name:", first_two)
print("Last two letters of name:", last_two)
print("Reversed name:", reverse_name)
print("Magic name:", magic_name)
print("Secret word:", secret_word)