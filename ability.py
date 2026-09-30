class Ability:

    # Ability stats
    def __init__(self, name, key, power, cooldown, target="one", message=None, cost=0):
        self.name = name
        self.key = key
        self.power = power
        self.cooldown = cooldown
        self.current_cooldown = 0
        self.target = target
        self.message = message
        self.cost = cost

    # Cooldowns and use
    def is_ready(self):
        return self.current_cooldown == 0 

    def can_afford(self, user):
        return user.mana >= self.cost

    def use(self, user, targets):
        user.mana -= self.cost
        if self.message is not None:
            print(f"{user.name} {self.message}")

        for target in targets:
            self.apply(user, target)
        self.current_cooldown = self.cooldown

    def apply(self, user, target):
        dmg = target.take_damage(round(user.attack * self.power))
        print(f"{user.name} uses {self.name} on {target.name} for {dmg} damage!")

    def tick(self):
        if self.current_cooldown > 0:
            self.current_cooldown -= 1 

class HealAbility(Ability):

    def apply(self, user, target):
        healed = target.heal(round(target.max_health * self.power))
        print(f"{target.name} heals for {healed}!")

class BlockAbility(Ability):

    def apply(self, user, target):
        target.blocking = True
        print(f"{target.name} blocks all damage this turn!")

class LifestealAbility(Ability):

    def __init__(self, name, key, power, cooldown, target="one", message=None, cost=0, drain=0.5):
        super().__init__(name, key, power, cooldown, target, message)
        self.drain = drain

    def apply(self, user, target):
        dmg = target.take_damage(round(user.attack * self.power))
        healed = user.heal(round(dmg * self.drain))
        print(f"{user.name} hit {target.name} for {dmg} and drains {healed} HP!")