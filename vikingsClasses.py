import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self. strength = strength

    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health = self.health - damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        # self.health = health
        # self.strength = strength

    def receiveDamage(self, damage):
        # your code here
        self.health = self.health - damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return (f"Odin Owns You All!")
        # your code here



# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
         super().__init__(health, strength)
        # your code here

    def receiveDamage(self, damage):
        # your code here
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
        # your code here

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
        self.saxonArmy.append(saxon)
        # your code here

    def vikingAttack(self):
        # your code here
        if self.vikingArmy and self.saxonArmy:
            viking = random.choice(self.vikingArmy)
            saxon = random.choice(self.saxonArmy)

            # Saxon receives damage from Viking
            result = saxon.receiveDamage(viking.strength)

            # Remove dead Saxons
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)

            # Return the result of the attack
            return result

    def saxonAttack(self):
         if self.vikingArmy and self.saxonArmy:
            viking = random.choice(self.vikingArmy)
            saxon = random.choice(self.saxonArmy)

            # Viking receives damage from Saxon
            result = viking.receiveDamage(saxon.strength)

            # Remove dead Vikings
            if viking.health <= 0:
                self.vikingArmy.remove(viking)

            return result
        # your code here

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        # your code here
    pass
