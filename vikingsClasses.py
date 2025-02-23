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
        self.health = self.health - damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        self.name = name
        super().__init__(health, strength)

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"


    def attack(self):
        return super().attack() 
    

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat" 
        # your code here

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        # your code here

    def attack(self):
        return super().attack()

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
        # your code here

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
        # your code here
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        # your code here
    
    def vikingAttack(self):
        # your code here
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <=0:
            self.saxonArmy.remove(saxon)
        return result
    
    def saxonAttack(self):
        # your code here
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = viking.receiveDamage(saxon.strength)
        if viking.health <=0:
            self.vikingArmy.remove(viking)
        return result

    def showStatus(self):
        # your code here
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


