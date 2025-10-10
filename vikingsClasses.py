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
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return None
        attacking_viking = random.choice(self.vikingArmy)
        attacked_saxon = random.choice(self.saxonArmy)
        result = attacked_saxon.receiveDamage(attacking_viking.attack())
        if attacked_saxon.health <= 0:
            self.saxonArmy.remove(attacked_saxon)
        return result
    
    def saxonAttack(self):
        if not self.saxonArmy or not self.vikingArmy:
            return None
        attacking_saxon = random.choice(self.saxonArmy)
        attacked_viking = random.choice(self.vikingArmy)
        result = attacked_viking.receiveDamage(attacking_saxon.attack())
        if attacked_viking.health <= 0:
            self.vikingArmy.remove(attacked_viking)
        return result 

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass
