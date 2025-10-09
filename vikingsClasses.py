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
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin owns you all!"

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has receive {damage} points of damage"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health <= 0:
            return f"A Saxon has died in combat"
        else:
            return f"A Saxon has receive {damage} points of damage"

# Davicente

class War():
    def __init__(self):
        vikingArmy = []
        saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
    
    def saxonAttack(self):
        # your code here

    def showStatus(self):
        # your code here
    pass


