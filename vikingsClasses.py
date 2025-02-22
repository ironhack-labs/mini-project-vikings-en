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
        if self.health < 0:
            self.health = 0  
        return None  
    

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return f"FOR GLORY, {self.name.upper()}!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return f"{self.name} has fallen in battle!"
        else:
            return f"{self.name} has {self.health} health left!"


# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            return "A Saxon has fallen!"
        else:
            return f"A Saxon has {self.health} health left!"


# War
class War:
    def __init__(self):
        self.vikings = []
        self.saxons = []

    def addViking(self, viking):
        self.vikings.append(viking)

    def addSaxon(self, saxon):
        self.saxons.append(saxon)

    def vikingAttack(self):
        if not self.saxons:
            return "No Saxons left to attack!"

        viking = random.choice(self.vikings)
        saxon = random.choice(self.saxons)

        damage = viking.attack()
        result = saxon.receiveDamage(damage)

        if saxon.health == 0:  # Remove dead Saxon
            self.saxons.remove(saxon)

        return result or "A Saxon has fallen!"

    def saxonAttack(self):
        if not self.vikings:
            return "No Vikings left to attack!"

        saxon = random.choice(self.saxons)
        viking = random.choice(self.vikings)

        damage = saxon.attack()
        result = viking.receiveDamage(damage)

        if viking.health == 0:  # Remove dead Viking
            self.vikings.remove(viking)

        return result or f"{viking.name} has fallen in battle!"

    def showStatus(self):
        if not self.saxons:
            return "Vikings win the war!"
        elif not self.vikings:
            return "Saxons win the war!"
        else:
            return f"There are {len(self.vikings)} Vikings and {len(self.saxons)} Saxons left in the battle."


