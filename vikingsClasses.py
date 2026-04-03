import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage

        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)


    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage

        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
            return f"A Saxon has died in combat"


# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.viking = viking
        self.vikingArmy.append(self.viking)
    
    def addSaxon(self, saxon):
        self.saxon = saxon
        self.saxonArmy.append(self.saxon)
    
    def vikingAttack(self):
        #Are there enough soldiers to proceed?
        if len(self.vikingArmy) == 0 or len(self.saxonArmy) == 0:
            return "Not enough soldiers"
        else:
            # Random selection of soldiers
            viking = random.choice(self.vikingArmy)
            saxon = random.choice(self.saxonArmy)
            
            # Saxon takes damage
            saxon_damage_received = saxon.receiveDamage(viking.strength)

            # Was the saxon killed? If so, remove saxon from army.
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
            
            return saxon_damage_received
           
    def saxonAttack(self):
        #Are there enough soldiers to proceed?
        if len(self.vikingArmy) == 0 or len(self.saxonArmy) == 0:
            return "Not enough soldiers"
        else:
            # Random selection of soldiers
            viking = random.choice(self.vikingArmy)
            saxon = random.choice(self.saxonArmy)

            # Viking takes damage
            viking_damage_received = viking.receiveDamage(saxon.strength) 
        
            # Was the viking killed? If so, remove viking from army.
            if viking.health <= 0:
                self.vikingArmy.remove(viking)   

            return viking_damage_received
        
        

    def showStatus(self):
        if len(self.saxonArmy) == 0 and len(self.vikingArmy) > 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0 and len(self.saxonArmy) > 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."