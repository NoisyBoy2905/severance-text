from enemy import Enemy, Boss
from move import Move

# Rainforest Adds
def mutated_frog():
    return Enemy("Mutated Frog", 40, 4, 10, 8)

def mutated_boar():
    return Enemy("Mutated Boar", 35, 12, 2, 12)

def mutated_tadpole():
    return Enemy("Mutated Tadpole", 25, 4, 5, 5)

# Rainforest Boss
def mutated_cheetah():
    return Boss("Mutated Cheetah", 100, 12, 5, 30, [Move("Pounce", 25, 1.25, 2, "crouches low, ready to pounce!")], enrage_bonus=2)

# Spaceship Adds
def security_drone():
    return Enemy("Security Drone", 22, 5, 5, 6)

def maintenance_bot():
    return Enemy("Maintenance Bot", 70, 8, 15, 16)

def sentry_turret():
    return Enemy("Sentry Turret", 30, 9, 5, 14)

# Spaceship Boss
def rogue_overseer():
    return Boss("Rogue Overseer", 120, 10, 10, 45, [
        Move("Laser Sweep", 20, 2.25, 1, "locks its targeting laser onto you!"),
        Move("Twin Blasters", 15, 0.8, 2),
    ], enrage_bonus=1.5)

# Rift Adds 
def rift_wisp():
    return Enemy("Rift Wisp", 60, 18, 10, 40)

def rift_knight():
    return Enemy("Rift Knight", 180, 32, 40, 120)

def rift_stalker():
    return Enemy("Rift Stalker", 110, 35, 10, 90)

# Rift Bosses
def rift_warden():
    return Boss("Rift Warden", 450, 34, 30, 300, [
        Move("Crushing Slam", 20, 2.5, 1, "raises its hammer high above you!"),
    ], enrage_bonus=1.4)

def hollow_colossus():
    return Boss("Hollow Colossus", 900, 42, 40, 600, [
        Move("Cataclysm", 15, 3.0, 1, "draws the rift into its fists..."),
        Move("Rending Claws", 15, 0.9, 2),
        Move("Tremor", 10, 1.4, 1, "stamps the ground and the floor starts to crack!"),
    ], enrage_at=0.3, enrage_bonus=1.5)
