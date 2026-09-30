from character import Character

class Player(Character):

    # Player stats
    def __init__(self, name, pillar, subclass, max_health, attack, defence):

        super().__init__(name, max_health, attack, defence)
        self.pillar = pillar
        self.subclass = subclass
        self.level = 1
        self.xp = 0
        self.health_growth = 12
        self.attack_growth = 1
        self.defence_growth = 3 
        self.max_level = 20
        self.unlocks = {}

    # XP and levelling
    def xp_needed(self):
        return 50 * self.level

    def gain_xp(self, amount):
        self.xp += amount
        print(f"{self.name} gains {amount} XP!")
        while self.xp >= self.xp_needed() and self.level < self.max_level:
            self.xp -= self.xp_needed()
            self.level_up()
        print()
        self.show_xp_bar()

    def level_up(self):
        self.level += 1 
        self.max_health += self.health_growth
        self.attack += self.attack_growth
        self.defence += self.defence_growth
        self.health = self.max_health
        print()
        print("LEVEL UP!")
        print(f"{self.name} is now level {self.level}!")
        self.show_stats()
        if self.level in self.unlocks:
            new_ability = self.unlocks[self.level]
            self.abilities.append(new_ability)
            print(f"You learned a new ability: {new_ability.name}")

    # Display
    def display_name(self):
        return f"{self.name} | Level {self.level}"

    def show_xp_bar(self):
        bar_length = 20
        filled = round((self.xp / self.xp_needed()) * bar_length)
        empty = bar_length - filled
        bar = ("#" * filled) + ("-" * empty)
        print()
        print(f"{"XP":<20} | [{bar}] | {self.xp:>3}/{self.xp_needed()}")

        
# Quick test
if __name__ == "__main__":

    hero = Player("Lincoln", "Religion", "Paladin", 120, 10, 5)
    hero.take_damage(20)
    hero.show_stats()
    print(hero.is_alive())