from classes import Paladin, Sorcerer
from ability import ManaAbility, BlockAbility, HealAbility
from dungeons import rainforest_river
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

def sim_dungeon(bot, hero_class):
    hero = hero_class("Bot")
    name, rooms = rainforest_river()

    for number, room in enumerate(rooms, start=1):
        if number > 1:
            percent = random.randint(25, 35)
            hero.heal(round(hero.max_health * (percent / 100)))

        if not sim_battle(hero, room, bot):
            return False    

    return True            

if __name__ == "__main__":

    classes = {
        "P": Paladin,
        "S": Sorcerer,
    }

    smart_wins = 0
    mash_wins = 0

    choice = input("Which Class? [P] Paladin, [S] Sorcerer: ").strip().upper()
    while choice not in classes:
        choice = input("Please enter P or S: ").strip().upper()
    hero_choice = classes[choice]

    for i in range(1000):

        with contextlib.redirect_stdout(io.StringIO()):
            smart_won = sim_dungeon(smart_bot, hero_choice)
            mash_won = sim_dungeon(mash_bot, hero_choice)
            if smart_won:
                smart_wins += 1
            if mash_won:
                mash_wins += 1

    print(f"Smart bot won {smart_wins} out of 1000 runs. ({smart_wins / 1000 * 100:.2f}% win rate)")
    print(f"Mash bot won {mash_wins} out of 1000 runs. ({mash_wins / 1000 * 100:.2f}% win rate)")
