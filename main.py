from player import Player
from enemy import Enemy
import random 

hero = Player("Micha", "Religion", "Paladin", 120, 10, 5)
boar = Enemy("Mutated Boar", 40, 8, 2, 10)

while hero.is_alive() and boar.is_alive():

    hero.show_health()
    boar.show_health()

    choice = input("[A]ttack or [D]efend?").strip().upper()

    if choice == "A":
        boar.take_damage(hero.attack)
    if choice == "D":
        pass

    if boar.is_alive():
        hero.take_damage(boar.attack)

if hero.is_alive():
    print(f"You Win! XP gained {boar.xp_reward}")
    hero.xp += boar.xp_reward

else:
    print("You Died!")