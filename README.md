![logo_ironhack_blue 7](https://user-images.githubusercontent.com/23629340/40541063-a07a0a8a-601a-11e8-91b5-2f13e4e6b441.png)

# Mini Project | Vikings

# ⚔️ Mini Project | Vikings

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OOP](https://img.shields.io/badge/Concept-OOP-green)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![Ironhack](https://img.shields.io/badge/Ironhack-Bootcamp-orange)

---

## 👥 Group Activity

This project was completed as a **collaborative group activity** as part of the Ironhack Bootcamp.

**👨‍💻 Contributors:**

* [Irish Levi Bawingan](https://github.com/Irish-Lev)
* *(Add your teammates here once available)*

---

## 📌 Introduction

The Vikings and the Saxons are at war ⚔️. Both are Soldiers, but they have different combat behaviors.

This project demonstrates how to build a battle simulation using **Object-Oriented Programming (OOP)** in Python, with a focus on **inheritance and class interaction**.

---

## 🎯 Project Goal

* Apply **OOP principles** in Python
* Understand and implement **inheritance**
* Design interacting classes
* Simulate a battle system
* Work with **test-driven development (TDD)**

---

## 🧱 Project Structure

```
mini-project-vikings/
│
├── vikingsClasses.py   # Core logic (REQUIRED)
├── wargame.py          # Bonus simulation
├── 1-testsSoldier.py
├── 2-testsVikings.py
├── 3-testsSaxons.py
├── 4-testsWar.py
└── README.md
```

---

## 🧠 OOP Concepts Used

### 🔹 Classes & Objects

* `Soldier` → base class
* `Viking`, `Saxon` → derived classes
* `War` → manages interactions

### 🔹 Inheritance

* Avoids code duplication
* Allows extension of base functionality

### 🔹 Polymorphism

* `receiveDamage()` behaves differently depending on the class

---

## ⚙️ Implementation Overview

### 🟦 Soldier (Base Class)

* Attributes: `health`, `strength`
* Methods:

  * `attack()` → returns strength
  * `receiveDamage()` → reduces health

---

### 🟩 Viking

* Inherits from `Soldier`
* Adds:

  * `name`
  * `battleCry()`
* Overrides:

  * `receiveDamage()` (custom messages)

---

### 🟨 Saxon

* Inherits from `Soldier`
* No name attribute
* Custom `receiveDamage()` logic

---

### 🟥 War Class

Controls the simulation:

* Stores:

  * `vikingArmy`
  * `saxonArmy`
* Handles:

  * Attacks
  * Death/removal
  * Battle status

---

## 🧪 Running the Tests

Run the following commands:

```bash
python 1-testsSoldier.py -v
python 2-testsVikings.py -v
python 3-testsSaxons.py -v
python 4-testsWar.py -v
```

✅ All tests should pass

---

## 🎮 Bonus: War Game Simulation

We implemented a simulation (`wargame.py`) that:

* Generates random armies
* Runs battle rounds
* Displays:

  * Attack results
  * Remaining fighters
  * Final winner

Run it with:

```bash
python wargame.py
```

---

## 🚧 Challenges Faced

* Debugging **indentation errors**
* Understanding **inheritance deeply**
* Interpreting **test-driven requirements**
* Managing **method return values correctly**

---

## 📚 Key Learnings

* Writing scalable code using **OOP**
* Reusing logic with **inheritance**
* Debugging using **unit tests**
* Designing systems with interacting objects

---

## 🚀 Future Improvements

* User input for army size
* Enhanced battle visualization
* Player statistics tracking
* GUI or web-based interface

---

## 📦 Deliverables

* ✔ Completed `vikingsClasses.py`
* ✔ All tests passing
* ✔ Bonus simulation implemented

---

## 🙌 Acknowledgements

Thanks to **Ironhack** for this hands-on project that strengthened our understanding of OOP in Python.

---

# 📢 LinkedIn / Portfolio Description

> Built a battle simulation in Python using Object-Oriented Programming principles. Implemented inheritance, polymorphism, and class interactions to model a dynamic war between Vikings and Saxons. Applied test-driven development and created an optional game simulation to visualize the battle.

---


















































































