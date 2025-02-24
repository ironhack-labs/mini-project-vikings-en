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
class Viking:
    def __init__(self, name, health, strength):
        self.name = name
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

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

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War class
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        if not self.saxonArmy:
            return "Saxons have been defeated! No Saxons left to attack."
        if not self.vikingArmy:
            return "Vikings have been defeated! No Vikings left to attack."
        attacking_viking = random.choice(self.vikingArmy)
        defending_saxon = random.choice(self.saxonArmy)
        result = defending_saxon.receiveDamage(attacking_viking.attack())
        if defending_saxon.health <= 0:
            self.saxonArmy.remove(defending_saxon)
        return result
    
    def saxonAttack(self):
        if not self.vikingArmy:
            return "Vikings have been defeated! No Vikings left to attack."
        if not self.saxonArmy:
            return "Saxons have been defeated! No Saxons left to attack."
        attacking_saxon = random.choice(self.saxonArmy)
        defending_viking = random.choice(self.vikingArmy)
        result = defending_viking.receiveDamage(attacking_saxon.attack())
        if defending_viking.health <= 0:
            self.vikingArmy.remove(defending_viking)
        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."
