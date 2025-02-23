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
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return "A Saxon has received DAMAGE points of damage"

# Davicente

class War():
   
    
    def __init__(self):
        # your code here
       self.vikingArmy = []
       self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        if isinstance(viking, list):
            self.vikingArmy.extend(viking)  # Adds all Vikings from the list
        else:
            self.vikingArmy.append(viking) 
    
    def addSaxon(self, saxon):
        # your code here
        if isinstance(saxon,list):
            self.saxonArmy.extend(saxon)
        else:
            self.saxonArmy.append(saxon)    
    
    def vikingAttack(self):
        # your code here
       Saxon =  random.choices(self.saxonArmy)
       viking = random.choices(self.vikingArmy)

       result = Saxon.receiveDamage(viking.strength)

       if Saxon.health <= 0:
            self.saxonArmy.remove(Saxon)
       return result 
    def saxonAttack(self):
        # your code here
       Saxon =  random.choices(self.saxonArmy)
       viking = random.choices(self.vikingArmy)

       result = viking.receiveDamage(Saxon.strength)

       if viking.health <= 0:
            self.vikingArmy.remove(viking)
       return result 
    def showStatus(self):
        # your code here
        if len(self.vikingArmyArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        elif len (self.saxonArmyArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.saxonArmy) == 1 and len(self.vikingArmy) == 1:
            return "Vikings and Saxons are still in the thick of battle."
        
 

#should make a Saxon receiveDamage() equal to the strength of a Viking