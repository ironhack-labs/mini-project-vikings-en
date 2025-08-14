import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        # your code here
    
    def attack(self):
        return self.strength
        

    def receiveDamage(self, damage):
        self.health -= damage
        # your code here
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
        
   
        

    def battleCry(self):
        return "Odin Owns you all!"
        

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
        # your code here

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"
        # your code here

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    def vikingAttack(self):
        attacking_viking = random.choice(self.vikingArmy)
        attacked_saxon = random.choice(self.saxonArmy)
        if self.saxonArmy == [] or self.vikingArmy == []:
            return "no soldiers left"
        else:
            damage = attacking_viking.strength
            d = attacked_saxon.receiveDamage(damage)
            if attacked_saxon.health <= 0:
                self.saxonArmy.remove(attacked_saxon)
            else:
                print(f"the Saxon lost {damage} health by the Viking")
            return d
        
    def saxonAttack(self):
        attacking_saxon = random.choice(self.saxonArmy)
        attacked_viking = random.choice(self.vikingArmy)
        if self.saxonArmy == [] or self.vikingArmy == []:
            return "no soldiers left"
        else:
            damage = attacking_saxon.strength
            a = attacked_viking.receiveDamage(damage)
            if attacked_viking.health <= 0:
                self.vikingArmy.remove(attacked_viking)
            else:
                print(f"{attacked_viking.name} has received {damage} points of damage")
            return a
    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."    
    
