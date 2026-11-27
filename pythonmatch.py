# -*- coding: utf-8 -*-
print(" Welcome to Hero Selection")

hero = input("Choose a hero (warrior/mage/archer): ").lower()

match hero:
    case "warrior":
        print("Warrior selected!")
        print("Strength:90")
        print("Magic:20")
        
    case "mage":
        print("Mage slected!")
        print("Strength:30")
        print("Magic:95")
        
    case "archer":
        print("Archer selected!")
        print("Strength:70")
        print("Magic:40")
        
    case _:
        print("Invalid hero choice!")
        
        print("Game started!")