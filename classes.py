from player import Player

class Paladin(Player):

    def __init__(self, name):
        super().__init__(name, "Religion", "Paladin", 120, 10, 6)

    def defend(self):
        self.defending = True 
        print(f"{self.name} raises their shield, increasing defence to {self.defence}!")