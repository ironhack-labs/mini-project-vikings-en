import random

# Soldier: basic fighter with health and strength
class Soldier:
    def __init__(self, health, strength):
        # Save starting health and strength
        self.health = health
        self.strength = strength

    def attack(self):
        # Damage this soldier can do
        return self.strength

    def receiveDamage(self, damage):
        # Lose health when hit
        self.health -= damage


# Viking: a Soldier with a name and a battle cry
class Viking(Soldier):
    def __init__(self, name, health, strength):
        # Set Soldier stats first
        super().__init__(health, strength)
        # Save Viking's name
        self.name = name

    def battleCry(self):
        # Viking shout
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # Viking takes damage and reports what happened
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


# Saxon: like a Soldier, but with a  message
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # Saxon takes damage and reports what happened
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# War: holds two armies and runs the fights
class War:
    def __init__(self):
        # Start with empty armies
        self.vikingArmy = []
        self.saxonArmy = []

    # Add one Viking to the army
    def addViking(self, viking):
        self.vikingArmy.append(viking)

    # Add one Saxon to the army
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    # One random Viking hits one random Saxon
    def vikingAttack(self):
        # If any army is empty, no attack happens
        if not self.vikingArmy or not self.saxonArmy:
            return None

        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        # Saxon takes damage equal to Viking's strength
        result = saxon.receiveDamage(viking.attack())

        # If Saxon died, remove from army
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)

        # Return the message from receiveDamage
        return result

    # One random Saxon hits one random Viking
    def saxonAttack(self):
        # If any army is empty, no attack happens
        if not self.vikingArmy or not self.saxonArmy:
            return None

        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)

        # Viking takes damage equal to Saxon's strength
        result = viking.receiveDamage(saxon.attack())

        # If Viking died, remove from army
        if viking.health <= 0:
            self.vikingArmy.remove(viking)

        # Return the message from receiveDamage
        return result

    # Tell who is winning or if the war continues
    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."
