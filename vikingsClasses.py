import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength
       
    def attack(self):
        return self.strength# your code here

    def receiveDamage(self, damage):
        self.damage=damage
        #self.health -= self.damage
        if self.strength<self.damage:
            self.health = 0
        else:
            self.health -= self.damage
        # your code here
  

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health,strength)
        self.name=name

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.damage=damage
        self.health -= self.damage
        if self.strength<self.damage:
            #self.health = 0
            return f"{self.name} has died in act of combat"
            
        else:
            #self.health -= self.damage
            return f"{self.name} has received {self.damage} points of damage"
       

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health,strength)

    def receiveDamage(self, damage):
        # your code here
        self.damage=damage
        self.health -= self.damage
        if self.strength<self.damage:
            #self.health = 0
            return "A Saxon has died in combat"
            
        else:
            #self.health -= self.damage
            return f"A Saxon has received {self.damage} points of damage"
            


class War():
    def __init__(self):
        # your code here
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, viking):
      
        # your code here
        self.viking=viking
        self.vikingArmy.append(self.viking)

    
    def addSaxon(self, saxon):
        # your code here
        self.saxon=saxon
        self.saxonArmy.append(self.saxon)


    def vikingAttack(self):
        if len(self.vikingArmy) == 0 or len(self.saxonArmy) == 0:
            return "No enough soldiers to attack"
        else:
            self.viking=random.choice(self.vikingArmy)
            self.saxon=random.choice(self.saxonArmy)
            damage = self.viking.strength
            attack= self.saxon.receiveDamage(damage) 

            if self.saxon.health <= 0:
                self.saxonArmy.remove(self.saxon)   

            return attack
    
    def saxonAttack(self):
        # your code here
        if len(self.vikingArmy) == 0 or len(self.saxonArmy) == 0:
            return "No enough soldiers to attack"
        else:
            self.viking=random.choice(self.vikingArmy)
            self.saxon=random.choice(self.saxonArmy)
            damage = self.saxon.strength
            attack= self.viking.receiveDamage(damage) 

            if self.viking.health <= 0:
                self.vikingArmy.remove(self.viking)   

            return attack

    def showStatus(self):
        # your code here
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        






