from enemies import mutated_frog, mutated_boar, mutated_cheetah

# Dungeon 1
def rainforest_river():
    return "Rainforest River", [
        [mutated_frog(), mutated_frog()],
        [mutated_boar(), mutated_frog()],
        [mutated_cheetah()],
    ]