from enemy import Enemy, Boss
from move import Move

#Rainforest Ads
def mutated_frog():
    return Enemy("Mutated Frog", 40, 4, 10, 8)

def mutated_boar():
    return Enemy("Mutated Boar", 35, 12, 2, 12)

def mutated_tadpole():
    return Enemy("Mutated Tadpole", 25, 4, 5, 5)

# Rainforest Boss
def mutated_cheetah():
    return Boss("Mutated Cheetah", 100, 12, 5, 30, [Move("Pounce", 25, 1.25, 2, "crouches low, ready to pounce!")], enrage_bonus=2)

