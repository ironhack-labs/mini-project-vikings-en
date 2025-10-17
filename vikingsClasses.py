import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health = self.health - damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"
            
# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"
            

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
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        saxon_damage = random_saxon.receiveDamage(random_viking.strength)
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return saxon_damage
    
    def saxonAttack(self):
        random_saxon = random.choice(self.saxonArmy)
        random_viking = random.choice(self.vikingArmy)
        viking_damage = random_viking.receiveDamage(random_saxon.strength)
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return viking_damage

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."
    pass


