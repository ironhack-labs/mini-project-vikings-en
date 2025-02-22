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
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War
class War:
    def __init__(self):
        self.vikings = []
        self.saxons = []

    def addViking(self, viking):
        self.vikings.append(viking)
    
    def addSaxon(self, saxon):
        self.saxons.append(saxon)
    
    def vikingAttack(self):
        if len(self.saxons) > 0:
            saxon = random.choice(self.saxons)
            result = saxon.receiveDamage(random.choice(self.vikings).strength) 
            if saxon.health <= 0:
                self.saxons.remove(saxon)  
            return result
        return None
    
    def saxonAttack(self):
        if len(self.vikings) > 0:
            viking = random.choice(self.vikings)  
            result = viking.receiveDamage(random.choice(self.saxons).strength)   
            if viking.health <= 0:
                self.vikings.remove(viking) 
            return result
        return None

    def showStatus(self):
        if len(self.saxons) == 0:
            return "The Vikings have won the war!"
        elif len(self.vikings) == 0:
            return "The Saxons have won the war!"
        else:
            return f"There are {len(self.vikings)} Vikings and {len(self.saxons)} Saxons in the war. The battle is still ongoing."

