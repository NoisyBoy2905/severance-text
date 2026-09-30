class Move:
    # Move stats
    def __init__(self, name, chance, power, hits, warning=None):
        self.name = name
        self.chance = chance
        self.power = power
        self.hits = hits
        self.warning = warning

    # Use move
    def use(self, user, target):
        damages = []
        for i in range(self.hits):
            damages.append(target.take_damage(round(user.attack * self.power)))
        print(f"{user.name} uses {self.name} for {sum(damages)} damage!")