from classes import Paladin
from enemy import Enemy
import os

def plural(number, word):
    if number == 1:
        return f"{number} {word}"
    else: 
        return f"{number} {word}s"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def intro():

    name = ""

    clear_screen()

    print(f"{"=" * 10} Welcome To Severance (WIP)! {"=" * 10}")
    print()
    print("The land is splitting.")
    print("Science, Magic and Religion each claim to know why. None of them agree.")
    print("Dungeons tear open without warning, spilling twisted creatures across the world.")
    print("But they all agree on one thing: someone has to go in.")
    print()

    while name == "":
        name = input("Enter your name: ").strip()

    print(f"Welcome, {name}!")  
    print()
    print("Choose your class:")

    menu = [
        "[P] Paladin | 120 Health | 10 Attack | 6 Defence",
        "[?] WIP",
        "[?] WIP",
    ]


    for option in menu:
        print("  " + option)

    print()
    choice = input(">  ").strip().upper()
    print()

    while choice not in ["P"]:
        print("Please Enter a Valid Keybind!")
        choice = input(">  ").strip().upper()
        print()

    if choice == "P":
        hero = Paladin(name)
        print("You have chosen the Paladin class!")
        input("Press Enter to Continue...")
        return hero

def dungeon(hero, name, enemies):

    room = 1 
    for enemy in enemies:
        clear_screen()
        print(f"{"=" * 10} {name} | Room {room} of {len(enemies)}{"=" * 10}")
        print()
        hero.show_bar()
        hero.show_xp_bar()
        print()
        print(f"A {enemy.name} blocks your path!")
        input("Press Enter to fight...")

        won = battle(hero, enemy)
        if not won:
            print()
            print(f"You were defeated in {name}")
            return
        room += 1

    print()
    print("DUNGEON CLEARED!")
    
def battle(hero, enemy):

    turn = 1 

    while hero.is_alive() and enemy.is_alive():

        clear_screen()

        hero.defending = False

        print()
        print(f"{"=" * 10} Turn {turn} {"=" * 10}")
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
                input("Press Enter to Continue...")
                continue

            elif not found.is_ready():
                print(f"{found.name} has {plural(found.current_cooldown, "turn")} till ready!")
                input("Press Enter to Continue...")
                continue
            else:
                found.use(hero, enemy)

        if enemy.is_alive():
            enemy.take_turn(hero)

        for ability in hero.abilities:
            ability.tick()

        input("Press Enter to Continue...")

        turn += 1

    if hero.is_alive():
        print()
        print(f"You Win!")
        print()
        hero.gain_xp(enemy.xp_reward)
        print()
        input("Press Enter to Continue...")
        return True

    else:
        print()
        print("You Died!")
        return False

if __name__ == "__main__":

    rainforest_enemies = [
        Enemy("Mutated Frog", 35, 3, 4, 8),
        Enemy("Mutated Boar", 40, 8, 2, 12),
        Enemy("Mutated Cheetah", 85, 10, 5, 25),
    ]
    
    hero = intro()

    dungeon(hero, "Rainforest River", rainforest_enemies)