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
        self.name = name
        super().__init__(health, strength)

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"
        

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

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
        chosen_viking_idx = random.sample(range(len(self.vikingArmy)), 1)[0] if len(self.vikingArmy) > 0 else 0
        chosen_saxon_idx = random.sample(range(len(self.saxonArmy)), 1)[0] if len(self.saxonArmy) > 0 else 0
        received_damage = self.saxonArmy[chosen_saxon_idx].receiveDamage(self.vikingArmy[chosen_viking_idx].strength)
        if received_damage == f"A Saxon has died in combat":
            del self.saxonArmy[chosen_saxon_idx]
        return received_damage
    
    def saxonAttack(self):
        # your code here
        chosen_viking_idx = random.sample(range(len(self.vikingArmy)), 1)[0] if len(self.vikingArmy) > 0 else 0
        chosen_viking = self.vikingArmy[chosen_viking_idx]
        chosen_saxon_idx = random.sample(range(len(self.saxonArmy)), 1)[0] if len(self.saxonArmy) > 0 else 0
        received_damage = chosen_viking.receiveDamage(self.saxonArmy[chosen_saxon_idx].strength)
        if received_damage == f"{chosen_viking.name} has died in act of combat":
            del self.vikingArmy[chosen_viking_idx]
        return received_damage

    def showStatus(self):
        # your code here
        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."
    pass


