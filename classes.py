from player import Player
from ability import Ability

class Paladin(Player):

    def __init__(self, name):
        super().__init__(name, "Religion", "Paladin", 120, 10, 6)
        self.abilities = [
            Ability("Shield Bash", "S", 1.3, 2),
            Ability("Holy Strike", "H", 2, 4),
        ]

    def defend(self):
        self.defending = True 
        print(f"{self.name} raises their shield!")