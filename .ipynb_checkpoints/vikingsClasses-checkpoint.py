import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health 
        self.strength  = strength
    
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
        super().__init__(health , strength)
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
            return  f"{self.name} has received {damage} points of damage"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health , strength)
        

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health <= 0:
            return "A Saxon has died in combat"
        else:
            return  f"A Saxon has received {damage} points of damage"
    

# Davicente

class War():
    def __init__(self):
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
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        #Damage = viking.strength
        Damage = viking.attack()
        saxons_damage_rec = saxon.receiveDamage(Damage)
        if saxon.health <=0:
            self.saxonArmy.remove(saxon)
        return saxons_damage_rec
      
    
    def saxonAttack(self):
        # your code here
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        #Damage = saxon.strength
        Damage = saxon.attack()
        vikings_damage_rec = viking.receiveDamage(Damage)
        if viking.health <=0:
            self.vikingArmy.remove(viking)
        return vikings_damage_rec

    def showStatus(self):
        # your code here
        if len(self.saxonArmy) and len(self.vikingArmy) >= 1:
            return f"Vikings and Saxons are still in the thick of battle."
        elif len(self.saxonArmy) <= 0 :
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy)<= 0:
            return f"Saxons have fought for their lives and survive another day..."
    pass


