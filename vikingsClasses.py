import random

# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        # Returns the soldier's strength value
        return self.strength

    def receiveDamage(self, damage):
        # Reduces health by damage amount
        self.health -= damage


# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        # Inherits from Soldier and adds a name attribute
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        # Returns the Viking battle cry
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # Reduces health and returns a message with the Viking's name
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        # Inherits directly from Soldier, no additional attributes
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # Reduces health and returns a generic message
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# War
class War():
    def __init__(self):
        # Initialize two empty armies
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        # Adds a Viking to the Viking army
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        # Adds a Saxon to the Saxon army
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # Select random Saxon and Viking for combat
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        
        # Viking attacks Saxon
        result = saxon.receiveDamage(viking.strength)
        
        # Remove Saxon if health is 0 or below
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        
        return result
    
    def saxonAttack(self):
        # Select random Viking and Saxon for combat
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        
        # Saxon attacks Viking
        result = viking.receiveDamage(saxon.strength)
        
        # Remove Viking if health is 0 or below
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        
        return result

    def showStatus(self):
        # Returns the current war status based on army sizes
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."