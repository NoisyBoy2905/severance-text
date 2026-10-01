from character import Character

def test_health_never_below_zero():
    hero = Character("Test Hero", 100, 10, 5)
    hero.take_damage(500)
    assert hero.health == 0

def test_block_take_0_damage():
    hero = Character("Test Hero", 100, 10, 5)
    hero.blocking = True
    hero.take_damage(50)
    assert hero.health == 100 

def test_damage_within_range():
    hero = Character("Test Hero", 100, 0, 0)
    damage = hero.take_damage(10)
    assert 8 <= damage <= 12

def test_heal_never_exceeds_max_health():
    hero = Character("Test Hero", 50, 10, 5)
    hero.health = 40
    healed = hero.heal(20)
    assert hero.health == 50
    assert healed == 10