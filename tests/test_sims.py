from sims.simulate import smart_bot
from classes import Paladin
from enemies import mutated_frog, mutated_cheetah

def test_bot_defends_when_boss_prepares():
    hero = Paladin("Test Hero")
    boss = mutated_cheetah()
    boss.preparing = boss.specials[0]
    choice, target = smart_bot(hero, [boss])
    assert choice == "D"

def test_bot_use_AOE():
    hero = Paladin("Test Hero")
    hero.level_up()
    frogs = [mutated_frog(), mutated_frog()]
    choice, target = smart_bot(hero, frogs)
    assert choice.name == "Holy Ground"
    assert target == frogs