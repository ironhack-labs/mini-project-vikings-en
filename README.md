# Python War Game: Vikings, Saxons, and Ragnarok

## Overview

This project is a simple battle simulator built using object-oriented programming in Python. It is divided into two versions:

- **Base project**: a Viking vs Saxon battle simulation
- **Ragnarok extension**: a themed version inspired by Norse mythology, featuring Valkyries and mythological creatures

The second version builds directly on the logic of the first, extending it with richer narrative elements and more dynamic output.

---

## Project Structure

```
.
├── vikingsClasses.py      # Core classes for the original Viking vs Saxon game
├── wargame.py             # Script that runs the original battle simulation
├── ragnarok_classes.py    # Extended mythology-based version of the class system
└── ragnarok_game.py       # Script that runs the Ragnarok version of the game
```

---

## Base Project

### vikingsClasses.py

This file defines the core class structure of the simulation.

#### Classes

- **Soldier**
  - Base class
  - Attributes: `health`, `strength`
  - Methods:
    - `attack()` → returns strength
    - `receiveDamage(damage)` → reduces health

- **Viking (inherits from Soldier)**
  - Adds `name`
  - Overrides:
    - `battleCry()` → returns a fixed battle phrase
    - `receiveDamage()` → returns custom messages including the Viking’s name

- **Saxon (inherits from Soldier)**
  - Similar to `Soldier`
  - Returns generic damage messages

- **War**
  - Manages both armies:
    - `vikingArmy`
    - `saxonArmy`
  - Methods:
    - `addViking()` / `addSaxon()`
    - `vikingAttack()` → Viking damages a Saxon
    - `saxonAttack()` → Saxon damages a Viking
    - `showStatus()` → returns current battle state

---

### wargame.py

This script runs the base simulation.

#### Behavior

- Initializes a `War` instance
- Creates:
  - 5 Vikings (random names, random strength)
  - 5 Saxons
- Runs a loop where:
  - Vikings attack
  - Saxons attack
  - Army sizes and status are printed each round
- Stops when one army is eliminated

---

## Ragnarok Extension

### ragnarok_classes.py

This file extends the base project with a Norse mythology theme.

#### Key Differences

- **Vikings become Valkyries**
  - Names are tied to unique actions via a dictionary
  - Each Valkyrie has a specific attack flavor

- **Saxons become mythological creatures**
  - Named enemies such as Fenrir, Jormungandr, and Nidhogg

- **Enhanced battle output**
  - Includes Valkyrie action plus combat result

- **Thematic endgame messages**
  - Reflect Ragnarok mythology

---

### ragnarok_game.py

This script runs the enhanced version of the simulation.

#### Behavior

- Initializes a `War` instance
- Creates:
  - 5 unique Valkyries
  - 5 mythological creatures
- Runs a timed simulation loop
- Every 5 rounds:
  - Prints round number
  - Displays army sizes
  - Shows current battle status

---

## Key Programming Concepts

- Object-Oriented Programming (OOP)
- Inheritance and method overriding
- Randomized simulation
- State management with lists
- Loop-based execution

---

## How to Run

Run the base version:

```
python wargame.py
```

Run the Ragnarok version:

```
python ragnarok_game.py
```

---

## Differences Between Versions

| Feature        | Base Project      | Ragnarok Extension     |
|----------------|-------------------|--------------------    |
| Theme          | Vikings vs Saxons | Norse mythology        |
| Characters     | Generic           | Named Valkyries        |
| Enemies        | Saxons            | Mythological creatures |
| Output         | Basic             | Narrative              |
| Loop           | Simple            | Timed + updates        |
