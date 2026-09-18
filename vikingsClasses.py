import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health=health
        self.strength=strength  
        self.damage=0

    def attack(self):
        # your code here
        return self.strength
    
    def receiveDamage(self, damage):
        # your code here
        self.damage=damage
        self.health=self.health-self.damage
        
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name=name

    def receiveDamage(self, damage):
        # your code here
        self.damage=damage
        self.health=self.health-self.damage
        if self.health>0:
            return f'{self.name} has received {self.damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
        
    def battleCry(self):
        return "Odin Owns You All!"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        self.damage=damage
        self.health=self.health-self.damage
        if self.health>0:
            return f'A Saxon has received {self.damage} points of damage'
        else:
            return f'A Saxon has died in combat'

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        # your code here
        viking=random.choice(self.vikingArmy)
        saxon=random.choice(self.saxonArmy)
        saxon_damage=saxon.receiveDamage(viking.strength)
        if saxon.health<=0:
            self.saxonArmy.remove(saxon)
        return saxon_damage
        
    def saxonAttack(self):
        # your code here
        viking=random.choice(self.vikingArmy)
        saxon=random.choice(self.saxonArmy)
        viking_damage=viking.receiveDamage(saxon.strength)
        if viking.health<=0:
            self.vikingArmy.remove(viking)
        return viking_damage
       
    def showStatus(self):
        # your code here
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy)>=1 and len(self.vikingArmy)>=1:
            return "Vikings and Saxons are still in the thick of battle."



