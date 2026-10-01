from enemies import mutated_frog, mutated_boar, mutated_cheetah, mutated_tadpole
from enemies import security_drone, maintenance_bot, sentry_turret, rogue_overseer

# Dungeon 1 (Lv 1)
def rainforest_river():
    return "Rainforest River", [
        [mutated_tadpole(), mutated_tadpole()],
        [mutated_frog(), mutated_frog()],
        [mutated_boar(), mutated_frog()],
        [mutated_cheetah()],
    ]

# Dungeon 2 (Lv 2-4)
def derelict_spaceship():
    return "Derelict Spaceship", [
        [security_drone(), security_drone(), security_drone()],
        [maintenance_bot(), security_drone(), security_drone()],
        [sentry_turret(), sentry_turret()],
        [rogue_overseer()],
    ]
