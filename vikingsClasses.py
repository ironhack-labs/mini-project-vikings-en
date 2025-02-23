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

# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
        return "Odin Owns You All!"

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if self.saxonArmy:
            saxon = random.choice(self.saxonArmy)
            viking = random.choice(self.vikingArmy)
            result = saxon.receiveDamage(viking.attack())
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
            return result

    def saxonAttack(self):
        if self.vikingArmy:
            viking = random.choice(self.vikingArmy)
            saxon = random.choice(self.saxonArmy)
            result = viking.receiveDamage(saxon.attack())
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
            return result

    def showStatus(self):
        print(f"Viking army: {len(self.vikingArmy)} warriors and Saxon army: {len(self.saxonArmy)} warriors")
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."

# Main game loop
great_war = War()

# Adding Vikings and Saxons to the armies
great_war.addViking(Viking("Ragnar", 100, 20))
great_war.addViking(Viking("Lagertha", 100, 25))
great_war.addSaxon(Saxon(100, 15))
great_war.addSaxon(Saxon(100, 15))

round_number = 0

# Game loop
while great_war.vikingArmy and great_war.saxonArmy:
    round_number += 1
    print(f"round: {round_number} // {great_war.showStatus()}")
    great_war.vikingAttack()
    if not great_war.saxonArmy:
        break
    great_war.saxonAttack()

# Final status
print(great_war.showStatus())
