from character import Character
import random

# Normal enemy
class Enemy(Character):

    def __init__(self, name, max_health, attack, defence, xp_reward):
        
        super().__init__(name, max_health, attack, defence)
        self.xp_reward = xp_reward
        self.charging = False

    # Enemy turn
    def take_turn(self, hero):

        if self.charging:
            dmg = hero.take_damage(self.attack * 2.2)
            print(f"{self.name} unleashes a devastating attack on {hero.name} for {dmg} damage!")
            self.charging = False
            return
        roll = random.randint(1, 100)

        if roll <= 50:
            dmg = hero.take_damage(self.attack)
            print(f"{self.name} attacks {hero.name} for {dmg} damage!")
        elif roll <= 70:
            self.defending = True
            print(f"{self.name} braces itself!")
        elif roll <= 90:
            dmg = hero.take_damage(self.attack * 1.5)
            print(f"{self.name} heavy attacks {hero.name} for {dmg} damage!")
        else:
            print(f"{self.name} charges up and prepares for a devastating attack next turn!")
            self.charging = True

# Boss enemy
class Boss(Enemy):

    def __init__(self, name, max_health, attack, defence, xp_reward, specials, enrage_at=0.25, enrage_bonus=2.5):
        super().__init__(name, max_health, attack, defence, xp_reward)
        self.specials = specials
        self.enrage_at = enrage_at
        self.enrage_bonus = enrage_bonus
        self.enraged = False
        self.preparing = None

    # Boss turn: enrage, specials, then normal move
    def take_turn(self, hero):

        if not self.enraged and self.health <= self.max_health * self.enrage_at:
            self.enraged = True
            self.attack *= self.enrage_bonus
            print(f"{self.name} becomes ENRAGED!")

        if self.preparing is not None:
            self.preparing.use(self, hero)
            self.preparing = None
            return 

        if self.charging:
            super().take_turn(hero)
            return
        
        roll = random.randint(1, 100)
        total = 0

        for move in self.specials:
            total += move.chance
            if roll <= total:
                if move.warning is None:
                    move.use(self, hero)
                else:    
                    self.preparing = move
                    print(f"{self.name} {move.warning}")
                return

        super().take_turn(hero)

# Quick test
if __name__ == "__main__":

    boar = Enemy("Mutated Boar", 40, 8, 2, 10)
    boar.take_damage(10)
    boar.show_health()
    print(boar.is_alive())
