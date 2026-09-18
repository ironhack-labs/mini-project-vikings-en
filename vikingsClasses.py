import random

# Soldier


class Soldier:
    
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        self.damage = 0
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
        # self.health = health
        # self.strength = strength

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
        # if self.health < self.damage:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
        # lf.health <= 0:
            return "A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
       self.vikingArmy = []
       self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking) # self.viking
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result_viking = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return result_viking
    
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        result_saxon = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result_saxon

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) >= 1 and len (self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
    pass


