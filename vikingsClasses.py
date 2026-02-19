import random


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength
    
    def attack(self):
        self.attack=self.strength
        return self.attack


    def receiveDamage(self, damage):
        self.health-=damage
    



class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name=name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f"{self.name} has received {damage} points of damage"
        elif self.health<=0:
            return f"{self.name} has died in act of combat"
        


class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health-=damage
        if self.health>0:
            return f"A Saxon has received {damage} points of damage"
        elif self.health<=0:
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy=[]
        self.saxonArmy=[]

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        random_saxon_defender=random.choice(self.saxonArmy)
        random_viking_attacker=random.choice(self.vikingArmy)

        saxon_damage=random_viking_attacker.strength
        va_result=random_saxon_defender.receiveDamage(saxon_damage)

        if va_result==f"A Saxon has died in combat":
            self.saxonArmy.remove(random_saxon_defender)

        return va_result
    
    def saxonAttack(self):
        random_viking_defender=random.choice(self.vikingArmy)
        random_saxon_attacker=random.choice(self.saxonArmy)

        viking_damage=random_saxon_attacker.strength
        sa_result=random_viking_defender.receiveDamage(viking_damage)

        if sa_result==f"{random_viking_defender.name} has died in act of combat":
            self.vikingArmy.remove(random_viking_defender)

        return sa_result
    
    def showStatus(self):
        if self.saxonArmy==[]:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy==[]:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    pass



