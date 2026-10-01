from classes import Paladin, Sorcerer

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

def test_sorcerer_creation():
    sorcerer = Sorcerer("Test Sorcerer")
    assert sorcerer.name == "Test Sorcerer"
    assert sorcerer.health == 100
    assert sorcerer.attack == 13
    assert sorcerer.defence == 5
    assert sorcerer.mana == 60
    assert sorcerer.max_mana == 60

def test_sorcerer_level_up():
    sorcerer = Sorcerer("Test Sorcerer")
    sorcerer.level_up()
    assert sorcerer.name == "Test Sorcerer"
    assert sorcerer.health == 108
    assert sorcerer.attack == 15
    assert sorcerer.defence == 6

def test_sorcerer_unlocks():
    sorcerer = Sorcerer("Test Sorcerer")
    sorcerer.level_up()
    assert sorcerer.abilities[-1].name == "Chain Lightning"