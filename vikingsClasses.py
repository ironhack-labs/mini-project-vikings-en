
import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
        # defining the parent class and core attributes. 
    def attack(self):
        return self.strength
        

    def receiveDamage(self, damage):
        self.health -= damage
      
    

# Viking. child class. we draw on the super class with super' then add the attributes unique to the child class Viking. take not of the capitalisation of Viking as it is a class name. 

class Viking(Soldier):
    def __init__(self, name, health, strength):
       self.name = name
       super().__init__(health, strength)

    def battleCry(self):
        return "Odin Owns You All!"
# note for me: damage is a parameter: its value is supplied when receiveDamage()
# is called. During battle, viking.attack() returns the Viking's
# strength, which becomes the damage value received by the Saxon.
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

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
#lowercase viking and saxon receive the add.viking / add.saxon input this is external data.
    def addViking(self, viking):
       self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        resultViking = saxon.receiveDamage(viking.attack())

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return resultViking
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)

        resultSaxon = viking.receiveDamage(saxon.attack())

        if viking.health <= 0:
            self.vikingArmy.remove(viking)

        return resultSaxon
        

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass


