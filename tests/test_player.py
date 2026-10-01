from classes import Paladin 

def test_paladin_creation():
    paladin = Paladin("Test Paladin")
    assert paladin.name == "Test Paladin"
    assert paladin.health == 120
    assert paladin.attack == 10
    assert paladin.defence == 6

def test_level_up_correct_stats():
    paladin = Paladin("Test Paladin")
    paladin.level_up()
    assert paladin.level == 2
    assert paladin.health == 132
    assert paladin.attack == 11
    assert paladin.defence == 9

def test_ability_unlocks():
    paladin = Paladin("Test Paladin")
    paladin.level_up()
    assert paladin.abilities[-1].name == "Holy Ground"