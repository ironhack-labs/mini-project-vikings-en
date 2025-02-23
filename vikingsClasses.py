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

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking: Viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon: Saxon):
        self.saxonArmy.append(saxon)
        
    
    def vikingAttack(self):
        if len(self.vikingArmy) == 0:
            pass
        
        else:   
          saxon = random.choice(self.saxonArmy)# choose randomly from a list
          viking = random.choice(self.vikingArmy)
            #make a Saxon receiveDamage() equal to the strength of a Viking
          attackResult = saxon.receiveDamage(viking.strength)
            #remove dead saxons from the army
          if saxon.health <= 0:
              self.saxonArmy.remove(saxon)
          return attackResult
    
    def saxonAttack(self):
        if len(self.saxonArmy) == 0:
            pass
        else:
          saxon = random.choice(self.saxonArmy)# choose randomly from a list
          viking = random.choice(self.vikingArmy)
           #make a vaiking receiveDamage() equal to the strength of a saxon  
          attackResult = viking.receiveDamage(saxon.strength)
           #remove dead vaiking from the army
          if viking.health <= 0:
              self.vikingArmy.remove(viking)
          return attackResult

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return 'Vikings have won the war of the century!'
        
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        else:
            return "Vikings and Saxons are still in the thick of battle."
    


