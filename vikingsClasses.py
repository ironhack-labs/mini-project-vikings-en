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
        self.health-=(damage)
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health-=(damage)
        if self.health <= 0:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
         self.health-=(damage)
         if self.health <= 0:
            return "A Saxon has died in combat"
         else:
            return f"A Saxon has received {damage} points of damage"



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
        if len(self.saxonArmy) == 0:  # Ensure Saxons are available
            return "No Saxons left to fight."
        attack_viking = random.choice(self.vikingArmy)
        attack_sexon = random.choice(self.saxonArmy)
        receive_Damage = attack_sexon.receiveDamage(attack_viking.strength)
        if attack_sexon.health <= 0:
            self.saxonArmy.remove(attack_sexon)
        return receive_Damage


    
    def saxonAttack(self):
        # your code here
        if len(self.vikingArmy) == 0:  # Ensure Vikings are available
            return "No Vikings left to fight."
        attack_viking = random.choice(self.vikingArmy)
        attack_sexon = random.choice(self.saxonArmy)
        receive_Damage = attack_viking.receiveDamage(attack_sexon.strength)
        if attack_viking.health <= 0:
            self.vikingArmy.remove(attack_viking)
        return receive_Damage

    def showStatus(self):
        # your code here
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."


