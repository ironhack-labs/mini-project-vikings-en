import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength
    def attack(self):
        # your code here
        return self.strength
    def receiveDamage(self, damage):
        # your code here
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        self.name = name
        super().__init__(health, strength) #Inherits from the Soldier class
    def battleCry(self):
        # your code here
        return "Odin Owns You All!"
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)
    def attack(self):
        return super().attack() #Inherits the Soldier attack.
    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        # your code here
        if not self.vikingArmy or not self.saxonArmy:
            return
        #Brings in the random warriors
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        result = saxon.receiveDamage(viking.attack())

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)

        return result

        
    def saxonAttack(self):
        # your code here
        if not self.vikingArmy or not self.saxonArmy:
                    return
        #Brings in the random warriors
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        
        result = viking.receiveDamage(saxon.attack())

        if viking.health <= 0:
            self.vikingArmy.remove(viking)

        return result

        
    def showStatus(self):
        # your code here
         if not self.saxonArmy:
            return f"Vikings have won the war of the century!"
         elif not self.vikingArmy:
            return f"Saxons have fought for their lives and survive another day..."
         else:
            return f"Vikings and Saxons are still in the thick of battle."
    pass


