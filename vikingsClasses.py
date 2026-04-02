import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength= strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        if damage>0:
            self.health-=damage
        

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name=name
        super().__init__(health, strength)
        
    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        
        if self.health>0:
           return f"{self.name} has received {damage} points of damage"
        else:
           return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        
        if self.health>0:
           return f"A Saxon has received {damage} points of damage"
        else:
           return f"A Saxon has died in combat"

# New Class


# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    pass
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    pass
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    pass
    
    def vikingAttack(self):
        random_saxon=random.choice(self.saxonArmy)
        random_viking=random.choice(self.vikingArmy)

        life_saxon=random_saxon.receiveDamage(random_viking.attack())

        if random_saxon.health<=0:
            self.saxonArmy.remove(random_saxon)
            
        return life_saxon  
           
    pass 
    
    def saxonAttack(self):
        if not self.saxonArmy or not self.vikingArmy:
            return
        random_saxon=random.choice(self.saxonArmy)
        random_viking=random.choice(self.vikingArmy)

        life_viking=random_viking.receiveDamage(random_saxon.attack())

        if random_viking.health<=0:
            self.vikingArmy.remove(random_viking)

        return life_viking
    pass
    
    def showStatus(self):
        vikings_Alive=len(self.vikingArmy)
        saxon_Alive=len(self.saxonArmy)

        if vikings_Alive<=0:
            return "Saxons have fought for their lives and survive another day..."
        elif saxon_Alive<=0:
            return "Vikings have won the war of the century!"
        else:
            return "Vikings and Saxons are still in the thick of battle."    
    pass


