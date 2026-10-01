from classes import Paladin, Sorcerer
from ability import ManaAbility, BlockAbility, HealAbility
from dungeons import rainforest_river, derelict_spaceship
from main import any_alive
import io
import contextlib
import random

def mash_bot(hero, enemies):
    for enemy in enemies:
        if enemy.is_alive():
            return "A", enemy

def smart_bot(hero, enemies):
    for enemy in enemies:
        if enemy.is_alive() and (enemy.charging or getattr(enemy, "preparing", None) is not None):
            # Block ability ready? Use it, otherwise defend
            for ability in hero.abilities:
                if isinstance(ability, BlockAbility) and ability.is_ready() and ability.can_afford(hero):
                    return ability, [hero]
            return "D", None

    alive = []
    for enemy in enemies:
        if enemy.is_alive():
            alive.append(enemy)

    for ability in hero.abilities:
        if ability.is_ready() and ability.can_afford(hero):
            if isinstance(ability, ManaAbility) and hero.mana >= (hero.max_mana / 2):
                continue
            if isinstance(ability, HealAbility) and hero.health >= (hero.max_health / 2):
                continue
            if isinstance(ability, BlockAbility):
                continue
            if ability.target == "all":
                return ability, alive
            if ability.target == "self":
                return ability, [hero]
            return ability, [alive[0]]

    return "A", alive[0]


def sim_battle(hero, enemies, bot):
    turn = 1

    while hero.is_alive() and any_alive(enemies):
        hero.defending = False
        hero.blocking = False

        choice, target = bot(hero, enemies)

        if choice == "A":
            target.take_damage(hero.attack)
        elif choice == "D":
            hero.defend()
        else:
            choice.use(hero, target)

        for enemy in enemies:
            if enemy.is_alive():
                enemy.defending = False
                enemy.take_turn(hero)

        for ability in hero.abilities:
            ability.tick()
        hero.mana = min(hero.max_mana, hero.mana + hero.mana_regen)

        turn += 1
        if turn > 500:
            return False  
        
    if hero.is_alive():
        total_xp = 0
        for enemy in enemies:
            total_xp += enemy.xp_reward
        hero.gain_xp(total_xp)
        return True

    return False

def sim_dungeon(bot, hero_class, dungeon, level):
    hero = hero_class("Bot")
    for i in range(level - 1):
        hero.level_up()
    name, rooms = dungeon()

    for number, room in enumerate(rooms, start=1):
        if number > 1:
            percent = random.randint(25, 35)
            hero.heal(round(hero.max_health * (percent / 100)))

        if not sim_battle(hero, room, bot):
            return False

    return True

def run_batch(bot, hero_class, dungeon, level, runs):
    wins = 0
    for i in range(runs):
        with contextlib.redirect_stdout(io.StringIO()):
            won = sim_dungeon(bot, hero_class, dungeon, level)
        if won:
            wins += 1
    return wins / runs * 100

def pick(question, options):
    choice = input(question).strip().upper()
    while choice not in options and choice != "A":
        choice = input("Please pick one of the letters shown: ").strip().upper()
    if choice == "A":
        return list(options.values())
    return [options[choice]]

if __name__ == "__main__":

    classes = {
        "P": Paladin,
        "S": Sorcerer,
    }
    dungeons = {
        "R": ("Rainforest River", rainforest_river, 1),
        "D": ("Derelict Spaceship", derelict_spaceship, 2),
    }
    runs = 5000

    class_list = pick("Which class? [P] Paladin, [S] Sorcerer, [A] All: ", classes)
    dungeon_list = pick("Which dungeon? [R] Rainforest River, [D] Derelict Spaceship, [A] All: ", dungeons)
    rounds = int(input("How many rounds? "))

    for dungeon_name, dungeon, level in dungeon_list:
        for hero_class in class_list:
            print()
            print(f"===== {dungeon_name} (Lv {level}) | {hero_class.__name__} =====")

            smart_results = []
            mash_results = []

            for round_number in range(1, rounds + 1):
                smart = run_batch(smart_bot, hero_class, dungeon, level, runs)
                mash = run_batch(mash_bot, hero_class, dungeon, level, runs)
                smart_results.append(smart)
                mash_results.append(mash)
                print(f"Round {round_number}: smart {smart:.1f}% | mash {mash:.1f}%")

            print(f"Smart average {sum(smart_results) / len(smart_results):.1f}% (lowest {min(smart_results):.1f}%, highest {max(smart_results):.1f}%)")
            print(f"Mash average {sum(mash_results) / len(mash_results):.1f}% (lowest {min(mash_results):.1f}%, highest {max(mash_results):.1f}%)")

    print()
    print(f"({rounds} rounds x {runs} runs each)")
