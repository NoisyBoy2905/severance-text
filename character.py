import random

class Character:

    # Base stats
    def __init__(self, name, max_health, attack, defence):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack = attack
        self.defence = defence
        self.defending = False
        self.defending_power = 1.5
    
    # Taking damage
    def take_damage(self, raw_damage):
        raw_damage = random.randint(int(raw_damage * 0.8), int(raw_damage * 1.2))
        if self.defending:
            raw_damage = raw_damage / self.defending_power
        damage = round(raw_damage * (100 / (100 + self.defence)))
        self.health = max(0, self.health - damage) 
        return damage

    # Status and display
    def is_alive(self):
        return self.health > 0

    def show_health(self):
        print(f"{self.name} is at {self.health}/{self.max_health} health.")

    def show_stats(self):
        print(f"{self.name} stats are: {self.health}/{self.max_health} health, {self.attack} attack and {self.defence} defence.")

    def show_bar(self):
        bar_length = 20
        filled = round((self.health / self.max_health) * bar_length)
        empty = bar_length - filled
        bar = "#" * filled + "-" * empty
        print(f"{self.display_name():<20} | [{bar}] | {self.health:>3}/{self.max_health}")

    def display_name(self):
        return self.name

    
