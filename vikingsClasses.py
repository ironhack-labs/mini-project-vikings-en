import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):

        return self.strength

    def receiveDamage(self, damage):
        # subtracting the dmg from health
        self.health -= damage


# Viking


class Viking(Soldier):
    def __init__(self, name, health, strength):
        # creating the Viking -> Solder
        self.name = name
        super().__init__(health, strength)

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage

        # Check if the viking solder is still alive
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


# Saxon


class Saxon(Soldier):
    def __init__(self, health, strength):
        # Creating the Saxon -> Solder
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


# Davicente


class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)

    def vikingAttack(self):
        # Pick a random Saxon and viking
        target_saxon = random.choice(self.saxonArmy)
        attacker_viking = random.choice(self.vikingArmy)

        # Fight
        result = target_saxon.receiveDamage(attacker_viking.strength)

        # check the result of fighting
        if target_saxon.health <= 0:
            self.saxonArmy.remove(target_saxon)

        return result

    def saxonAttack(self):
        target_viking = random.choice(self.vikingArmy)
        attacker_saxon = random.choice(self.saxonArmy)

        result = target_viking.receiveDamage(attacker_saxon.strength)

        if target_viking.health <= 0:
            self.vikingArmy.remove(target_viking)

        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"

        if not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."

        if self.saxonArmy and self.vikingArmy:
            return "Vikings and Saxons are still in the thick of battle."

    pass
