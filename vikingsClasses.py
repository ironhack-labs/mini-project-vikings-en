import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health=health
        self.strength=strength

    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health-=damage

    
# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name=name



    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.damage=damage
        self.health-=self.damage
        if self.health>0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
        

    def receiveDamage(self, damage):
        self.damage=damage
        self.health-=self.damage
        if self.health>0:
            return f"A Saxon has received {self.damage} points of damage"
        else:
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
        if not self.saxonArmy or not self.vikingArmy:
            return None
        random_saxon = random.choice(self.saxonArmy)
        random_viking=random.choice(self.vikingArmy)
        result=random_saxon.receiveDamage(random_viking.strength)
        if random_saxon.health<=0:
            self.saxonArmy.remove(random_saxon)
        return result
    
    def saxonAttack(self):
        if not self.saxonArmy or not self.vikingArmy:
            return None
        random_saxon = random.choice(self.saxonArmy)
        random_viking=random.choice(self.vikingArmy)
        result=random_viking.receiveDamage(random_saxon.strength)
        if random_viking.health<=0:
            self.vikingArmy.remove(random_viking)
        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
            
    
    pass

