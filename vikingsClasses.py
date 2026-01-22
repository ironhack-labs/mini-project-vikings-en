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
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        # your code here
        return f"Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
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

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
        
# Davicente

class War():
    def __init__(self) :
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
        random_saxon = random.choice(self.saxonArmy)
        random_viking =  random.choice(self.vikingArmy)

        VikingAttack =  random_saxon.receiveDamage(random_viking.strength)
        
        if random_saxon.health <=0:
             self.saxonArmy.remove(random_saxon)
        
        return VikingAttack

    def saxonAttack(self):
        # your code here
        random_saxon = random.choice(self.saxonArmy)
        random_viking =  random.choice(self.vikingArmy)
    
        SaxonAttack =  random_viking.receiveDamage(random_saxon.strength)
        
        if random_viking.health <=0:
             self.vikingArmy.remove(random_viking)
        
        return SaxonAttack
    
    def showStatus(self):
        # your code here
        if len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy)== 0:
            return f"Vikings have won the war of the century!"
        else:
            return f"Vikings and Saxons are still in the thick of battle."