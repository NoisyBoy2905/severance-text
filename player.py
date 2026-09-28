from character import Character

class Player(Character):

    def __init__(self, name, pillar, subclass, max_health, attack, defence):

        super().__init__(name, max_health, attack, defence)
        self.pillar = pillar
        self.subclass = subclass
        self.level = 1
        self.xp = 0

if __name__ == "__main__":

    hero = Player("Micha", "Religion", "Paladin", 120, 10, 5)
    hero.take_damage(20)
    hero.show_stats()
    print(hero.is_alive())