# Severance (Text Prototype)

A turn-based dungeon crawler in the terminal, written in Python. It's the text-based prototype of **Severance**, an FFXIV-style MMO I'm designing. Each version builds toward the full game:

Blackjack → **Text prototype (this repo)** → 2.5D version → 3D single-player → 3D multiplayer

![Intro and class select](screenshots/intro.png)

## The world

Dungeons have been appearing across the world for two thousand years, growing bigger and more dangerous. Three pillars (Science, Magic and Religion) can't agree on why, but have to fight together to survive them.

## How to run

Needs **Python 3.12+**. There are no extra packages to install.

```
python main.py
```

## Features so far

- **Turn-based combat:** attack, defend, or use abilities with cooldowns
- **Paladin class:** a tank with 7 abilities unlocked from level 1 to 20, including an AOE attack, a heal, a block and lifesteal
- **Levelling:** XP, level-ups, stat growth and new abilities, up to level 20
- **2 dungeons:**
  - **Rainforest River:** 4 rooms of mutated animals, ending with a boss
  - **Derelict Spaceship:** 4 rooms of rogue robots, ending with a boss
- **Bosses:**
  - **Telegraphed attacks:** the boss warns you a turn before a big hit, so you can defend
  - **Enrage:** the boss gets stronger at low health
- **Group fights:** fight several enemies at once, with damage variance and defence scaling
- **Mana system:** ready for the Sorcerer (in progress)

## Screenshots

**First fight:** pick an ability, choose a target

![First fight](screenshots/dungeon1firstfight.png)

**Level up:** stats grow and a new ability unlocks

![Level up with new ability](screenshots/LevelUPwithNewAbility.png)

**Death:** ignore the boss's warning and Pounce hits hard

![Death screen](screenshots/deathscreen.png)

## Design docs

[`docs/Severance Monsters.xlsx`](docs/Severance%20Monsters.xlsx) has all the planning and balance work:

| Tab | What's in it |
|---|---|
| Monsters | Every enemy's stats, plus how much damage their defence blocks |
| Classes | Class stats, abilities and stats at every level |
| Dungeon Plans | The plan for each dungeon next to what's built so far |
| Build Order | What's next and in what order |
| Base Moves / Boss Specials / Damage Table | How enemy attacks work and how hard they hit |
| Balance Log | Every balance change, why it was made, and how it was found (playtests or simulations) |

## Project structure

| File | What it does |
|---|---|
| `main.py` | Game start, battle loop, dungeon runs |
| `character.py` | Base class for anything that fights (health, damage, healing) |
| `player.py` | Player: XP, levelling, unlocking abilities |
| `classes.py` | Playable classes (Paladin) |
| `ability.py` | Abilities: damage, heal, block, lifesteal |
| `enemy.py` | Enemy and Boss AI |
| `move.py` | Boss special moves |
| `enemies.py` | Every enemy's stats |
| `dungeons.py` | Dungeon layouts |

## Coming next

The Sorcerer class, tutorial tips, branching paths in the Spaceship, a multi-floor Cave dungeon, then loot, shops and saving. The full list is on the Build Order tab.
