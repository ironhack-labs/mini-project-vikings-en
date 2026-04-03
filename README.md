# Vikings Battle Simulation System

## Overview

This project implements a battle simulation between two groups (Vikings and Saxons) using Python. The objective is to model interacting entities through Object-Oriented Programming (OOP) and simulate how system state evolves over time.

The project focuses on structuring logic using classes, managing interactions between objects, and validating behavior through unit testing.

---

## Objectives

* Apply Object-Oriented Programming principles
* Implement inheritance and method overriding
* Model interactions between independent entities
* Simulate state changes over iterative steps
* Ensure correctness using unit tests

---

## System Architecture

### Core Classes

**Soldier (Base Class)**

* Attributes:

  * `health`
  * `strength`
* Methods:

  * `attack()` → returns strength value
  * `receiveDamage(damage)` → updates health

---

**Viking (Derived Class)**

* Extends `Soldier` with:

  * `name`
* Overrides:

  * `receiveDamage()` to return contextual messages
* Adds:

  * `battleCry()`

---

**Saxon (Derived Class)**

* Inherits from `Soldier`
* Overrides:

  * `receiveDamage()` with generic battle messages

---

**War (Simulation Controller)**

* Maintains:

  * `vikingArmy` (list)
  * `saxonArmy` (list)
* Responsibilities:

  * Add units to armies
  * Execute attacks between randomly selected units
  * Update system state (health and army size)
  * Remove defeated entities
  * Report battle status

---

## Simulation Logic

* At each iteration, a random Viking and Saxon are selected
* Damage is determined by the attacker's strength
* The defender’s health is reduced accordingly
* Units with zero or negative health are removed from their army
* The process continues until one army is depleted

This structure reflects a simplified agent-based simulation where independent entities interact under defined rules.

---

## Data Logging

The simulation includes a data logging mechanism that records the state of both armies at each round.

Captured data includes:

* Round number
* Number of Vikings remaining
* Number of Saxons remaining
* Winner (when determined)

The results are exported as a CSV file:

```id="sgrx1y"
battle_log.csv
```

This enables further analysis using tools such as Pandas or Excel.

---

## Project Structure

```id="r9xq9a"
vikingsClasses.py   # Core simulation logic and class definitions
wargame.py          # Runs the simulation loop
1-testSoldier.py    # Unit tests for Soldier class
2-testVikings.py    # Unit tests for Viking class
3-testSaxons.py     # Unit tests for Saxon class
4-testWar.py        # Unit tests for War logic
README.md
```

---

## How to Run

### Run Unit Tests

```id="m1k2z8"
python 1-testSoldier.py
python 2-testVikings.py
python 3-testSaxons.py
python 4-testWar.py
```

All tests pass, confirming correct implementation.

---

### Run Simulation

```id="9c3w2f"
python wargame.py
```

This generates:

* Console output showing battle progression
* A CSV file (`battle_log.csv`) containing structured simulation data

---

## Key Technical Concepts

* Object-Oriented Programming (OOP)
* Inheritance and polymorphism
* Method overriding and reuse via `super()`
* State management across interacting objects
* Randomized behavior using Python’s `random` module
* Unit testing for validation

---

## Challenges & Learnings

* Designing a clean inheritance hierarchy (`Soldier → Viking/Saxon`)
* Overriding methods while maintaining base functionality
* Managing interactions between multiple objects within a simulation
* Ensuring logic correctness through test-driven validation

---

## Status

* Fully implemented
* All unit tests passing
* Simulation validated through multiple runs
* Data logging successfully integrated

---

## Context

Developed as part of the Ironhack bootcamp to build strong programming fundamentals and introduce structured problem-solving approaches relevant to data analysis and software development.
