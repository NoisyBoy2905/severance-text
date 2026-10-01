import json, os, io, contextlib
from classes import Paladin, Sorcerer

SAVE_FILE = "save.json"
CLASSES = {
    "Paladin": Paladin,
    "Sorcerer": Sorcerer,
}

def save_game(hero):
    data = {
        "name": hero.name,
        "class": hero.subclass,
        "level": hero.level,
        "xp": hero.xp,
    }

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

def has_save():
    return os.path.exists(SAVE_FILE)

def load_game():
    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    hero_class = CLASSES[data["class"]]
    hero = hero_class(data["name"])
    with contextlib.redirect_stdout(io.StringIO()):
        for i in range(data["level"] - 1):
            hero.level_up()
    hero.xp = data["xp"]
    return hero

def peek_save():
    with open(SAVE_FILE, "r") as f:
        data = json.load(f)
    return data