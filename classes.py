from player import Player
from ability import Ability, HealAbility, BlockAbility, LifestealAbility

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
            # TEMP: testing, remove these 5 lines later
            Ability("Holy Ground", "G", 1.0, 3, target="all"),
            HealAbility("Lay on Hands", "L", 0.3, 6, target="self"),
            BlockAbility("Divine Aegis", "E", 0, 6, target="self", message="raises a wall of holy light!"),
            LifestealAbility("Radiant Slash", "R", 1.6, 4),
            Ability("Judgement", "J", 4.0, 8),
        ]

        self.unlocks = {
            2:  Ability("Holy Ground", "G", 1.0, 3, target="all"),
            5:  HealAbility("Lay on Hands", "L", 0.3, 6, target="self"),
            9:  BlockAbility("Divine Aegis", "E", 0, 6, target="self", message="raises a wall of holy light!"),
            13: LifestealAbility("Radiant Slash", "R", 1.6, 4),
            20: Ability("Judgement", "J", 4.0, 8),
        }
    # Paladin defend
    def defend(self):
        self.defending = True 
        print(f"{self.name} raises their shield!")