from player import Player
from ability import Ability, HealAbility, BlockAbility, LifestealAbility, ManaAbility

class Paladin(Player):

    # Paladin stats and abilities
    def __init__(self, name):
        super().__init__(name, "Religion", "Paladin", 120, 10, 6)
        self.health_growth = 12
        self.attack_growth = 1
        self.defence_growth = 3
        self.defending_power = 3
        self.abilities = [
            Ability("Shield Bash", "S", 1.3, 2),
            Ability("Holy Strike", "H", 2, 4),
        ]

        self.unlocks = {
            2:  Ability("Holy Ground", "G", 1.3, 3, target="all"),
            5:  HealAbility("Lay on Hands", "L", 0.25, 7, target="self"),
            9:  BlockAbility("Divine Aegis", "E", 0, 6, target="self", message="raises a wall of holy light!"),
            13: LifestealAbility("Radiant Slash", "R", 1.6, 4),
            20: Ability("Judgement", "J", 4.0, 8),
        }
    # Paladin defend
    def defend(self):
        self.defending = True 
        print(f"{self.name} raises their shield!")

class Sorcerer(Player):


    def __init__(self, name):
        super().__init__(name, "Magic", "Sorcerer", 100, 13, 5)
        self.health_growth = 8
        self.attack_growth = 2
        self.defence_growth = 1
        self.defending_power = 2
        self.max_mana = 60
        self.mana = self.max_mana
        self.mana_regen = 4
        self.abilities = [
            Ability("Fire Bolt", "F", 1.8, 1, mana_cost=10),
            ManaAbility("Mana Tide", "T", 0.4, 6, target="self"),
        ]

        self.unlocks = {
            2:  Ability("Chain Lightning", "L", 1.2, 3, target="all", mana_cost=12),
            5:  HealAbility("Frost Ward", "I", 0.2, 6, target="self", mana_cost=15),
            9:  BlockAbility("Wind Step", "W", 0, 6, target="self", message="vanishes on a gust of wind!", mana_cost=15),
            13: LifestealAbility("Steam Burst", "B", 1.8, 4, mana_cost=25),
            20: Ability("Meteor", "M", 4.5, 8, mana_cost=40),
        }

    def defend(self):
        self.defending = True
        print(f"{self.name} conjures a magical barrier!")