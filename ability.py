class Ability:

    def __init__(self, name, key, power, cooldown):
        self.name = name
        self.key = key
        self.power = power
        self.cooldown = cooldown
        self.current_cooldown = 0

    def is_ready(self):
        return self.current_cooldown == 0 

    def use(self, user, target):
        dmg = target.take_damage(round(user.attack * self.power))
        self.current_cooldown = self.cooldown
        print(f"{user.name} uses {self.name} on {target.name} for {dmg} damage!")

    def tick(self):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1 