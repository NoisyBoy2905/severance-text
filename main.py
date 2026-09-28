from classes import Paladin
from enemy import Enemy
import random 

hero = Paladin("Micha")
boar = Enemy("Mutated Boar", 40, 8, 2, 10)

while hero.is_alive() and boar.is_alive():

    hero.show_health()
    boar.show_health()

    choice = input("[A]ttack or [D]efend? ").strip().upper()

    if choice == "A":
        boar.take_damage(hero.attack)
        print(f"{hero.name} attacks {boar.name} for {hero.attack} damage!")
    elif choice == "D":
        hero.defend()
    else:
        print("Invalid choice. Please enter 'A' or 'D'.")
        continue

    if boar.is_alive():
        hero.take_damage(boar.attack)

if hero.is_alive():
    print(f"You Win! XP gained {boar.xp_reward}")
    hero.xp += boar.xp_reward

else:
    print("You Died!")