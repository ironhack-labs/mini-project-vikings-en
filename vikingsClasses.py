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
        # print(f"Soldier received {self.damage} damage. his health is now {self.health}")

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"


""" Test Viking
test_viking = Viking("Harald", 100, 8)
test_viking.battleCry()
test_viking.attack()
test_viking.receiveDamage(75)
test_viking.receiveDamage(50)
"""

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health <= 0:
            return f"A Saxon has died in combat"
    
""" Test Saxon     
test_saxon = Saxon(100, 8)
test_saxon.receiveDamage(75)
test_saxon.receiveDamage(50)
"""

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
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        message = saxon.receiveDamage(viking.attack())
        if "died" in message:
            self.saxonArmy.remove(saxon)
        return message

    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        message = viking.receiveDamage(saxon.attack())
        print(message)
        if "died" in message:
            self.vikingArmy.remove(viking)
        return message

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            print("Vikings have won the war of the century!")
            return "Vikings have won the war of the century!"    
        elif len(self.vikingArmy) == 0:
            print("Saxons have fought for their lives and survive another day...")
            return "Saxons have fought for their lives and survive another day..." 
        else: 
            print("Vikings and Saxons are still in the thick of battle.")
            return "Vikings and Saxons are still in the thick of battle."
            

    pass

"""Test War 
war = War()
v1 = Viking("Harald", 100, 28)
v2 = Viking("Ragnar", 100, 27)
war.addViking(v1)
war.addViking(v2)

s1 = Saxon(100, 18)
s2 = Saxon(100, 14)
war.addSaxon(s1)
war.addSaxon(s2)

while len(war.vikingArmy) > 0 and len(war.saxonArmy) > 0:
    war.vikingAttack()
    if len(war.saxonArmy) == 0:
        war.showStatus()
    war.saxonAttack()
    if len(war.vikingArmy) == 0:
        war.showStatus()
    war.showStatus()
"""
