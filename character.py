class Character:

    def __init__(self, name, max_health, attack, defence):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack = attack
        self.defence = defence
        self.defending = False
    
    def take_damage(self, raw_damage):
        if self.defending:
            raw_damage = raw_damage / 1.5
        damage = raw_damage * (100 / (100 + self.defence))
        self.health = round(max(0, self.health - damage))   
        self.defending = False

    def is_alive(self):
        return self.health > 0

    def show_health(self):
        print(f"{self.name} is at {self.health}/{self.max_health} health.")

    def show_stats(self):
        print(f"{self.name} stats are: {self.health}/{self.max_health} health, {self.attack} attack and {self.defence} defence.")