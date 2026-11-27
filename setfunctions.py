# -*- coding: utf-8 -*-
games = {"Chess", "Football", "Cricket"}


print("Type of games set:")
print(type(games))

print("\nNumber of items in set:")
print(len(games))

print("\nGames in the set:")
for item in games:
    print(item)

games.add("Tennis")
print("\nAfter add():")
print(games)

games.update(["Hockey", "Badminton"])
print("\nAfter update():")
print(games)

games.remove("Football")
print("\nAfter remove():")
print(games)

games.discard("Chess")
print("\nAfter discard():")
print(games)

removed_item = games.pop()
print("\nAfter pop():")
print("Removed Item:", removed_item)
print(games)

games.clear()
print("\nAfter clear():")
print(games)

extra_set = {"Pizza", "Burger"}
del extra_set

print("\nextra_set deleted successfully")