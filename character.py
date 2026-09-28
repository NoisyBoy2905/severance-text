import random

class Character:

    def __init__(self, name, max_health, attack, defence):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack = attack
        self.defence = defence
        self.defending = False
    
    def take_damage(self, raw_damage):
        raw_damage = random.randint(int(raw_damage * 0.8), int(raw_damage * 1.2))
        if self.defending:
            raw_damage = raw_damage / 1.5
        damage = round(raw_damage * (100 / (100 + self.defence)))
        self.health = round(max(0, self.health - damage))   
        self.defending = False
        return damage

    def is_alive(self):
        return self.health > 0

    def show_health(self):
        print(f"{self.name} is at {self.health}/{self.max_health} health.")

    def show_stats(self):
        print(f"{self.name} stats are: {self.health}/{self.max_health} health, {self.attack} attack and {self.defence} defence.")