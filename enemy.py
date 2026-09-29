from character import Character
import random

class Enemy(Character):

    def __init__(self, name, max_health, attack, defence, xp_reward):
        
        super().__init__(name, max_health, attack, defence)
        self.xp_reward = xp_reward
        self.charging = False

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



if __name__ == "__main__":

    boar = Enemy("Mutated Boar", 40, 8, 2, 10)
    boar.take_damage(10)
    boar.show_health()
    print(boar.is_alive())
