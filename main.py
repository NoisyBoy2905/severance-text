from classes import Paladin
from enemies import mutated_frog, mutated_boar, mutated_cheetah
from move import Move
import os
import random

# Helpers
def plural(number, word):
    if number == 1:
        return f"{number} {word}"
    else: 
        return f"{number} {word}s"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def any_alive(enemies):
    for enemy in enemies:
        if enemy.is_alive():
            return True
    return False

# Target picking
def pick_target(enemies):
    alive_enemies = []

    for enemy in enemies:
        if enemy.is_alive():
            alive_enemies.append(enemy)

    if len(alive_enemies) == 1:
        return alive_enemies[0]

    print("Choose a target:")
    for number, enemy in enumerate(alive_enemies, start=1):
        print(f"[{number}] {enemy.name}")
    
    while True:
        try:
            pick = int(input(">  ").strip())
        except ValueError:
            print("Please enter a valid number!")
            continue

        if 1 <= pick <= len(alive_enemies):
            return alive_enemies[pick - 1]
        print("Invalid Target! Please choose a valid target.")

    
# Title and class select
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

# Dungeon
def dungeon(hero, name, enemies):

    room = 1 

    for room_enemies in enemies:

        # Rest between rooms
        if room > 1:
            percent = random.randint(25, 35)
            heal = round(hero.max_health * (percent / 100))
            hero.health = min(hero.max_health, hero.health + heal)
            print(f"You catch your breath and heal for {heal} health!")
            input("Press Enter to Continue...")

        # Room intro
        clear_screen()
        print(f"{"=" * 10} {name} | Room {room} of {len(enemies)} {"=" * 10}")
        print()
        hero.show_bar()
        hero.show_xp_bar()
        print()
        names = []
        for enemy in room_enemies:
            names.append(enemy.name)

        if len(names) == 1:
            print(f"A {names[0]} blocks your path!")
        else:
            print(f"{' and '.join(names)} block your path!")
        input("Press Enter to fight...")

        # Fight the room
        won = battle(hero, room_enemies)
        if not won:
            print()
            print(f"You were defeated in {name}")
            return
        room += 1

    print()
    print("DUNGEON CLEARED!")
    
# Battle
def battle(hero, enemies):

    turn = 1 

    while hero.is_alive() and any_alive(enemies):

        # Turn display
        clear_screen()

        hero.defending = False

        print()
        print(f"{"=" * 15} Turn {turn} {"=" * 15}")
        print()

        hero.show_bar()
        for enemy in enemies:
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

        # Hero turn
        if choice == "A":
            target = pick_target(enemies)
            dmg = target.take_damage(hero.attack)
            print(f"{hero.name} attacks {target.name} for {dmg} damage!")
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
                found.use(hero, pick_target(enemies))

        # Enemy turn
        for enemy in enemies:
            if enemy.is_alive():
                enemy.defending = False
                enemy.take_turn(hero)

        # End of turn
        for ability in hero.abilities:
            ability.tick()

        input("Press Enter to Continue...")

        turn += 1

    # Battle result
    if hero.is_alive():
        print()
        print(f"You Win!")
        print()
        total_xp = 0
        for enemy in enemies:
            total_xp += enemy.xp_reward
        hero.gain_xp(total_xp)
        print()
        input("Press Enter to Continue...")
        return True

    else:
        print()
        print("You Died!")
        return False

# Start game
if __name__ == "__main__":

    rainforest_enemies = [
        [mutated_frog(), mutated_frog()],
        [mutated_boar(), mutated_frog()],
        [mutated_cheetah()],
    ]
    
    hero = intro()

    dungeon(hero, "Rainforest River", rainforest_enemies)