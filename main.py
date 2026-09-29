from classes import Paladin
from enemy import Enemy
import os

def plural(number, word):
    if number == 1:
        return f"{number} {word}"
    else: 
        return f"{number} {word}s"

def battle(hero, enemy):

    os.system('cls' if os.name == 'nt' else 'clear')

    turn = 1 

    while hero.is_alive() and enemy.is_alive():

        print()
        print(f"========== Turn {turn} ==========")
        print()

        hero.show_bar()
        enemy.show_bar()

        print()

        menu = [
            "[A] Attack",
            "[D] Defend",
        ]

        for ability in hero.abilities:
            if ability.is_ready():
                menu.append(f"[{ability.key}] {ability.name}")
            else:
                menu.append(f"[{ability.key}] {ability.name} | {plural(ability.current_cooldown, "turn")}")

        for option in menu:
            print("  " + option)

        print()
        choice = input(">  ").strip().upper()
        print()

        if choice == "A":
            dmg = enemy.take_damage(hero.attack)
            print(f"{hero.name} attacks {enemy.name} for {dmg} damage!")
        elif choice == "D":
            hero.defend()
        else:
            found = None
            for ability in hero.abilities:
                if ability.key == choice:
                    found = ability

            if found is None:
                print("Please Enter a Valid Keybind!")
                continue

            elif not found.is_ready():
                print(f"{found.name} has {plural(found.current_cooldown, "turn")} till ready!")
                continue
            else:
                found.use(hero, enemy)

        if enemy.is_alive():
            dmg = hero.take_damage(enemy.attack)
            print(f"{enemy.name} attacks {hero.name} for {dmg} damage!")

        for ability in hero.abilities:
            ability.tick()

        turn += 1

    if hero.is_alive():
        print(f"You Win! XP gained {enemy.xp_reward}")
        hero.xp += enemy.xp_reward
        return True

    else:
        print("You Died!")
        return False

if __name__ == "__main__":
    
    hero = Paladin("Micha")
    enemy = Enemy("Mutated Boar", 40, 8, 2, 10)

    battle(hero, enemy)