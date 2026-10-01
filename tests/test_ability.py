from ability import Ability

def test_cooldown_works():
    ability = Ability("Test Ability", "T", 1, 2)
    ability.current_cooldown = 2
    assert not ability.is_ready()
    ability.tick()
    ability.tick()
    assert ability.is_ready()