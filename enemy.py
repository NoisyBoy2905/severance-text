from character import Character

class Enemy(Character):

    def __init__(self, name, max_health, attack, defence, xp_reward):
        
        super().__init__(name, max_health, attack, defence)
        self.xp_reward = xp_reward

if __name__ == "__main__":

    boar = Enemy("Mutated Boar", 40, 8, 2, 10)
    boar.take_damage(10)
    boar.show_health()
    print(boar.is_alive())
