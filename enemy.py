class Enemy:

    def __init__(self, name, max_health, attack, defence, xp_reward):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack = attack
        self.defence = defence
        self.xp_reward = xp_reward

    def take_damage(self, raw_damage):
        damage = raw_damage * (100 / (100 + self.defence))
        self.health = round(max(0, self.health - damage))

    def is_alive(self):
        return self.health > 0

    def show_health(self):
        print(f"{self.name} is at {self.health} hitpoints!")

if __name__ == "__main__":

    boar = Enemy("Mutated Boar", 40, 8, 2, 10)
    boar.take_damage(10)
    boar.show_health()
    print(boar.is_alive())
