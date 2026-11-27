# -*- coding: utf-8 -*-
def hungry_monster(monster_name, food, quantity):
    print("Welcome to Monster Restaurant!")
    print("--------------------------------")

    print(monster_name, "enters the restaurant.")
    print(monster_name, "orders", quantity, food)

    if quantity >= 10:
        print(monster_name, "shouts: WOW! That's a giant meal!")
    else:
        print(monster_name, "says: Hmm... I need more food!")

    print(monster_name, "starts eating... Yum Yum Yum!")

    for i in range(1, quantity + 1):
        print("Eating item", i)

    print(monster_name, "has finished eating!")

    if quantity > 15:
        print(monster_name, "becomes SUPER FAT and starts rolling ")
    else:
        print(monster_name, "starts dancing happily ")

    print(monster_name, "says: I will come back tomorrow!")
    print("--------------------------------")


hungry_monster("Bobo Monster", "Pizzas", 12)