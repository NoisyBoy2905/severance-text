class Player:

    def __init__(self, name, pillar, subclass, max_health, attack, defence):
        self.name = name
        self.pillar = pillar
        self.subclass = subclass
        self.max_health = max_health
        self.health = max_health
        self.attack = attack
        self.defence = defence
        self.level = 1
        self.xp = 0

    def take_damage(self, raw_damage):
        damage = raw_damage * (100 / (100 + self.defence))
        self.health = round(max(0, self.health - damage))

    def is_alive(self):
        return self.health > 0

    def show_stats(self):
        print(f"{self.name} stats are: {self.health}/{self.max_health} health, {self.attack} attack and {self.defence} defence.")

    def show_health(self):
        print(f"{self.name} is at {self.health} hitpoints!")


if __name__ == "__main__":

    hero = Player("Micha", "Religion", "Paladin", 120, 10, 5)
    hero.take_damage(20)
    hero.show_stats()
    print(hero.is_alive())