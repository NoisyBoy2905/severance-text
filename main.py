from classes import Paladin
from enemy import Enemy

hero = Paladin("Micha")
boar = Enemy("Mutated Boar", 40, 8, 2, 10)

def battle():

    while hero.is_alive() and boar.is_alive():

        hero.show_bar()
        boar.show_bar()

        menu = [
            "[A]ttack",
            "[D]efend",
        ]

        for ability in hero.abilities:
            if ability.is_ready():
                menu.append(f"[{ability.key}] {ability.name}")
            else:
                menu.append(f"[{ability.key}] {ability.name} ({ability.current_cooldown} turns)")

        choice = input(", ".join(menu) + "? ").strip().upper()

        if choice == "A":
            dmg = boar.take_damage(hero.attack)
            print(f"{hero.name} attacks {boar.name} for {dmg} damage!")
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
                print(f"{found.name} has {found.current_cooldown} turns till ready!")
                continue
            else:
                found.use(hero, boar)

        if boar.is_alive():
            dmg = hero.take_damage(boar.attack)
            print(f"{boar.name} attacks {hero.name} for {dmg} damage!")

        for ability in hero.abilities:
            ability.tick()

    if hero.is_alive():
        print(f"You Win! XP gained {boar.xp_reward}")
        hero.xp += boar.xp_reward

    else:
        print("You Died!")

if __name__ == "__main__":

    battle()