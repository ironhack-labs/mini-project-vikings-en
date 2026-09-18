import random

# Soldier


class Soldier:
     """Represents a soldier with health and strength."""

    def __init__(self, health, strength):
        """Initialize a soldier with health and strength."""
        self.health = health
        self.strength = strength
        self.damage = 0
    
    def attack(self):
        """Return the soldier's strength as their attack damage."""
        return self.strength

    def receiveDamage(self, damage):
        """Apply received damage and reduce the soldier's health."""
        self.damage = damage
        self.health = self.health - self.damage
    

# Viking

class Viking(Soldier):
    """Represents a Viking who inherits from the Soldier class."""
    def __init__(self, name, health, strength):
        """Initialize a Viking with a name, health, and strength."""
        self.name = name
        super().__init__(health, strength)
        
    def battleCry(self):
        """Return the Viking's battle cry."""
        return f"Odin Owns You All!"

    def receiveDamage(self, damage):
        """Reduce the Viking's health and report whether they survived."""
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        """Initialize a Saxon with health and strength."""
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        """Reduce the Saxon's health and report whether they survived."""
        self.damage = damage
        self.health = self.health - self.damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        elif self.health <= 0:
            return f"A Saxon has died in combat"


# Davicente

class War():
    def __init__(self):
        """Initialize empty Viking and Saxon armies."""
        self.vikingArmy = []
        self.saxonArmy = []
    
    def addViking(self, viking):
        """Add a Viking to the Viking army."""
        self.vikingArmy.append(viking)

    
    def addSaxon(self, saxon):
        """Add a Saxon to the Saxon army."""
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        """Select a random Viking and Saxon and have the Viking attack."""
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        damage_viking= saxon.receiveDamage(viking.strength)
        if saxon.health <=0:
            self.saxonArmy.remove(saxon)
        return damage_viking
    
    def saxonAttack(self):
        """Select a random Saxon and Viking and have the Saxon attack."""
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage_saxon = viking.receiveDamage(saxon.strength)
        if viking.health <=0:
            self.vikingArmy.remove(viking)
        return damage_saxon

    def showStatus(self):
        """Return a message describing the current status of the war."""
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."

   # pass


