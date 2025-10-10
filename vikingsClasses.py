import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health= health
        self.strength= strength
        # your code here
    
    def attack(self):
        return self.strength
        # your code here

    def receiveDamage(self, damage):
        self.health-= damage
        # your code here
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name= name
        # your code here

    def battleCry(self):
        return "Odin Owns You All!"
        # your code here

    def receiveDamage(self, damage):
        self.health-= damage
        
        if self.health <= 0:
            return f"{self.name} has died in act of combact"
        else:
            return f"{self.name} has received {damage} points of damage"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        # your code here

    def receiveDamage(self, damage):
        self.health - damage
        if self.health <= 0:
            return f"A Saxon has ided in combat"
        else:
            return f"A Saxon has received {damage} points of damage"
        # your code here

# Davicente

class War():
    def __init__(self):
        self.vikingArmy= []
        self.saxonArmy= []
        # your code here

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        # your code here
    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        saxon_receive_damage = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return saxon_receive_damage
        # your code here
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        viking_receive_damage = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return viking_receive_damage
        # your code here

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        # your code here

