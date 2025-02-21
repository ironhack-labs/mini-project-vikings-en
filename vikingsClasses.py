import random
import cowsay

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.strength = 150
        self.health = 300
    
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
          super().__init__(health=health, strength=strength)
          self.name = name
        
    def battleCry(self):
        return 'Odin Owns You All!'

    def receiveDamage(self, damage):
        # your code here
        self.health = self.health - damage
        if damage != 0:
            if self.health >0:
                return f"{self.name} has received {damage} points of damage"
            elif self.health <= 0:
                return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
      self.health = 60
      self.strength = 25

    def receiveDamage(self, damage):
        self.health = self.health - damage
        string = ''
        if self.health > 0:
            string = (f"A Saxon has received {damage} points of damage")
        elif self.health <= 0:
            string = 'A Saxon has died in combat'
        return string

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        if self.vikingArmy: 
            self.vikingArmy.append(viking)
        else: 
            self.vikingArmy = [viking]
    
    def addSaxon(self, saxon):
        # your code here
        if self.saxonArmy: 
            self.saxonArmy.append(saxon)
        else: 
            self.saxonArmy = [saxon]
    
    def vikingAttack(self):
        # your code here
        if len(self.saxonArmy) == 0 or len(self.vikingArmy) == 0:
            pass
        else:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            damage = viking.strength
            effect = saxon.receiveDamage(damage) 
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
                print("A Saxon has died in combat")
            return effect
    
    def saxonAttack(self):
        # your code here
        if len(self.vikingArmy) == 0 or len(self.saxonArmy) == 0:
            pass
        else:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            damage = saxon.strength
            effect = viking.receiveDamage(damage)
            if viking.health <=0:
                self.vikingArmy.remove(viking)
                print(f"{viking.name} has received {str(saxon.strength)} points of damage")
            return effect
    
    def showStatus(self):
        # your code here
        string = ''
        if len(self.saxonArmy) > 0 and len(self.vikingArmy) > 0:
            string = 'Vikings and Saxons are still in the thick of battle.'
        elif len(self.vikingArmy) == 0:
            string = 'Saxons have fought for their lives and survive another day...'
        elif len(self.saxonArmy) == 0:
            string = 'Vikings have won the war of the century!'
        return string
    pass


