import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength  # A soldier attacks with their strength

    def receiveDamage(self, damage):
        self.health -= damage  # Reduce health by the damage received

    














# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)  # Inherit from Soldier
        self.name = name  # Add name attribute

    def receiveDamage(self, damage):
        self.health -= damage  # Reduce health
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"










#stopped here continue tomorrow!!!!!!!111!!





# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)  # Inherit from Soldier

    def receiveDamage(self, damage):
        self.health -= damage  # Reduce health
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"









# Davicente

import random

class War:
    def __init__(self):
        self.vikingArmy = []  # Empty list for Viking soldiers
        self.saxonArmy = []  # Empty list for Saxon soldiers

    def addViking(self, viking):
        self.vikingArmy.append(viking)  # Add a Viking to the army

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)  # Add a Saxon to the army

    def vikingAttack(self):
        if len(self.saxonArmy) == 0 or len(self.vikingArmy) == 0:
            return "No battle can happen."

        saxon = random.choice(self.saxonArmy)  # Pick a random Saxon
        viking = random.choice(self.vikingArmy)  # Pick a random Viking

        result = saxon.receiveDamage(viking.strength)  # Viking attacks Saxon

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)  # Remove dead Saxon

        return result

    def saxonAttack(self):
        if len(self.saxonArmy) == 0 or len(self.vikingArmy) == 0:
            return "No battle can happen."

        saxon = random.choice(self.saxonArmy)  # Pick a random Saxon
        viking = random.choice(self.vikingArmy)  # Pick a random Viking

        result = viking.receiveDamage(saxon.strength)  # Saxon attacks Viking

        if viking.health <= 0:
            self.vikingArmy.remove(viking)  # Remove dead Viking

        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."



