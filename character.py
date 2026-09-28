class Character:

    def __init__(self, name, max_health, attack, defence):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack = attack
        self.defence = defence
    
    def take_damage(self, raw_damage):
        damage = raw_damage * (100 / (100 + self.defence))
        self.health = round(max(0, self.health - damage))   

    def is_alive(self):
        return self.health > 0

    def show_health(self):
        print(f"{self.name} is at {self.health} hitpoints!")

    def show_stats(self):
        print(f"{self.name} stats are: {self.health}/{self.max_health} health, {self.attack} attack and {self.defence} defence.")