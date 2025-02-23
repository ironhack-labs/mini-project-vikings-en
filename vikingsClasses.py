import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        # Initialize health and strength for all soldiers
        self.health = health
        self.strength = strength
    
    def attack(self):
        # Soldier's attack returns its strength
        return self.strength

    def receiveDamage(self, damage):
        # Reduce the soldier's health by the damage amount
        self.health -= damage

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)  
        self.name = name

    def battleCry(self):
        # Return Viking battle cry
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # Reduce health and return appropriate message
        self.health -= damage
        if self.health > 0:
            # Fixed: include the actual damage value
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)  

    def receiveDamage(self, damage):
        # Reduce health and return appropriate message
        self.health -= damage
        if self.health > 0:
            # Fixed: include the actual damage value
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War
class War:
    def __init__(self):
        # Initialize the armies as empty lists
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # Add a Viking to the Viking army
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        # Add a Saxon to the Saxon army
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        # Choose a random Viking and a random Saxon to engage in battle
        # Fixed: random index should be within the valid range
        viking_index = random.randint(0, len(self.vikingArmy) - 1)
        saxon_index = random.randint(0, len(self.saxonArmy) - 1)

        # Viking attacks Saxon
        viking_strength = self.vikingArmy[viking_index].attack()
        result = self.saxonArmy[saxon_index].receiveDamage(viking_strength)
        # Remove Saxon if dead
        if result == "A Saxon has died in combat":
            self.saxonArmy.pop(saxon_index)
        return result
    def saxonAttack(self):
        # Choose a random Viking and a random Saxon to engage in battle
        # Fixed: random index should be within the valid range
        viking_index = random.randint(0, len(self.vikingArmy) - 1)
        saxon_index = random.randint(0, len(self.saxonArmy) - 1)

        # Saxon attacks Viking
        saxon_strength = self.saxonArmy[saxon_index].attack()
        result = self.vikingArmy[viking_index].receiveDamage(saxon_strength)
        # Remove Viking if dead
        if result == f"{self.vikingArmy[viking_index].name} has died in act of combat":
            self.vikingArmy.pop(viking_index)
        return result

    def showStatus(self):
        # Return the current status of the war
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
