import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength =strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        self.health = health
        self.strength =strength

        super().__init__(strength)


    def battleCry(self):
        return f"Odin Owns You All!{self.name},{self.health},{self.strength} "

    def receiveDamage(self, damage):
        self.damage=damage
        self.health -= damage
        
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
        super().__init__(strength)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy =[]


    def addViking(self, viking):
        self.viking =viking
        self.vikingArmy.append(viking)  
    
    def addSaxon(self, saxon):
        self.saxon =saxon
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        x = self.viking and self.damage == self.saxon and self.strength
        if "has died" in x:
                self.vikingArmy.remove(viking)
    
    def saxonAttack(self):
        x = self.saxon and self.damage == self.viking and self.strength
        if "has died" in x:
                self.saxonArmy.remove(saxon)

    def showStatus(self):
        if self.saxonArmy.empty():
            return f"Vikings have won the war of the century!"
        elif self.vikingArmy.empty():
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.viking)>=1 and len(self.saxon)>=1:
            return f"Vikings and Saxons are still in the thick of battle."
    pass

