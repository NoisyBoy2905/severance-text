from classes import Sorcerer
from ability import Ability
from enemies import mutated_frog

def test_cooldown_works():
    ability = Ability("Test Ability", "T", 1, 2)
    ability.current_cooldown = 2
    assert not ability.is_ready()
    ability.tick()
    ability.tick()
    assert ability.is_ready()

def test_mana_cost_taken():
    hero = Sorcerer("Test Hero")
    fire_bolt = hero.abilities[0] 
    frog = mutated_frog()
    fire_bolt.use(hero, [frog])
    assert hero.mana == 50

def test_can_not_afford_without_mana():
    hero = Sorcerer("Test Hero")
    hero.mana = 5
    fire_bolt = hero.abilities[0] 
    assert fire_bolt.can_afford(hero) == False

def test_mana_tide_restore_never_over_max():
    hero = Sorcerer("Test Hero")
    hero.mana = 10
    mana_tide = hero.abilities[1] 
    mana_tide.use(hero, [hero])
    assert hero.mana == 34
    hero.mana = 50
    mana_tide.use(hero, [hero])
    assert hero.mana == 60