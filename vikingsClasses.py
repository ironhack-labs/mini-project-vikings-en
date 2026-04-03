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
        super().__init__(health, strength)
        self.name = name
        
    def battleCry(self):
        # your code here
        return f"Odin Owns You All!"
        
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
        # we first pick random Viking and Saxon 
        attacker = random.choice(self.vikingArmy)
        defender = random.choice(self.saxonArmy)

        # Damage from Viking
        damage = attacker.attack()

        # Receiving damage 
        recevingdamage = defender.receiveDamage(damage)

        # If a Saxon dies 
        if defender.health <= 0:
            self.saxonArmy.remove(defender)
        return recevingdamage

    def saxonAttack(self):
        # your code here
        # pick random Saxon and Viking 
        attacker = random.choice(self.saxonArmy)
        defender = random.choice(self.vikingArmy)

        # Damage from Saxon 
        damage = attacker.attack()

        # Receiving damage 
        receivingdamage = defender.receiveDamage(damage)

        # If a Viking dies
        if defender.health <= 0:
            self.vikingArmy.remove(defender)
        return receivingdamage
    
    #def showStatus(self):
    #    # your code here
    #    if len(self.saxonArmy) == 0:
    #        return f"Vikings have won the war of the century!"
    #    elif len(self.vikingArmy) == 0:
    #        return f"Saxons have fought for their lives and survive another day..."
    #    elif len(self.saxonArmy) == 1 and len(self.vikingArmy) == 1:
    #        return f"Vikings and Saxons are still in the thick of battle."
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return f"Saxons have fought for their lives and survive another day..."
        else:
            return f"Vikings and Saxons are still in the thick of battle."

