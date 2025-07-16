import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength 
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    def battleCry(self):
        # your code here
        return "Odin Owns You All!"
    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        # Return a string to match the subclasses' return type
        if self.health >= 1:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)
    def receiveDamage(self, damage): 
        # your code here
        self.health -= damage
        if self.health >= 1:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return None
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damage = viking.strength
        result = saxon.receiveDamage(damage)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result

    def saxonAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return None
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damage = saxon.strength
        result = viking.receiveDamage(damage)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


