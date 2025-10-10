import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # call the parent class method to apply the health, strength logic
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        # call the parent class method to apply the damage logic
        super().receiveDamage(damage)

        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage



class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)


    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# Davicente

import random

# ---------- Base classes ----------
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage


class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        # reuse parent logic
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# ---------- War class ----------
class War:
    def __init__(self):
        # armies start empty
        self.vikingArmy = []
        self.saxonArmy = []

    # Adders (no return values)
    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    # One Viking attacks one Saxon (randomly chosen)
    def vikingAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return None  

        attacker = random.choice(self.vikingArmy)
        defender = random.choice(self.saxonArmy)

        result = defender.receiveDamage(attacker.attack())

        # remove dead saxons
        if defender.health <= 0:
            self.saxonArmy.remove(defender)

        # return the Saxon's receiveDamage() message
        return result

    # One Saxon attacks one Viking (randomly chosen)
    def saxonAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return None

        attacker = random.choice(self.saxonArmy)
        defender = random.choice(self.vikingArmy)

        result = defender.receiveDamage(attacker.attack())

        # remove dead vikings
        if defender.health <= 0:
            self.vikingArmy.remove(defender)

        # return the Viking's receiveDamage() message
        return result

    # Status line according to remaining armies
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."



