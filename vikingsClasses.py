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

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


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


class War:
    def __init__(self):
        self.saxonArmy = []
        self.vikingArmy = []

    def addViking(self, viking):
        if not isinstance(viking, Viking):
            raise TypeError("viking must be an instance of Viking")
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        if not isinstance(saxon, Saxon):
            raise TypeError("saxon must be an instance of Saxon")
        self.saxonArmy.append(saxon)

    def vikingAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return None

        attacking_viking = random.choice(self.vikingArmy)
        target_saxon = random.choice(self.saxonArmy)

        result = target_saxon.receiveDamage(attacking_viking.strength)

        if target_saxon.health <= 0:
            self.saxonArmy.remove(target_saxon)

        return result

    def saxonAttack(self):
        if not self.saxonArmy or not self.vikingArmy:
            return None

        attacking_saxon = random.choice(self.saxonArmy)
        target_viking = random.choice(self.vikingArmy)

        result = target_viking.receiveDamage(attacking_saxon.strength)

        if target_viking.health <= 0:
            self.vikingArmy.remove(target_viking)

        return result

    def showStatus(self) -> str:
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        return "Vikings and Saxons are still in the thick of battle."
