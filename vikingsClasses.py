import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength 
    
    def attack(self):
        return self.strength
        

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage 
    
 

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health,strength)
    
    def battleCry(self):
       return "Odin Owns You All!" 

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > self.damage:
            return f"{self.name} has received {self.damage} points of damage"
        else: 
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health,strength)
            
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > self.damage:
            return f"A Saxon has received {self.damage} points of damage"
        else: 
            return f"A Saxon has died in combat"


# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.viking = viking
        self.vikingArmy.append(self.viking)
    
    def addSaxon(self, saxon):
        self.saxon = saxon
        self.saxonArmy.append(self.saxon)

    def vikingAttack(self):
        if len(self.saxonArmy) == 0 or len(self.vikingArmy)==0: 
            return   "Not enough soldiers"
        else:
            self.viking = random.choice(self.vikingArmy)
            self.saxon = random.choice(self.saxonArmy)
            viking_attack =self.viking.strength
            #Saxon takes damage
            saxon_damage = self.saxon.receiveDamage(viking_attack) 
            #saxon is removed from army
            if self.saxon.health <= 0:  
                self.saxonArmy.remove(self.saxon)

            #should return result of calling receiveDamage() of a Saxon with the strength of a Viking
            return saxon_damage

    def saxonAttack(self):
        #Check if armies are empty
        if len(self.saxonArmy) == 0 or len(self.vikingArmy)==0: 
            return "Not enough soldiers"
        else:
            #Randomly selecting soldiers      
            self.viking = random.choice(self.vikingArmy)
            self.saxon = random.choice(self.saxonArmy)
            #Saxon generates damage
            saxon_attack = self.saxon.strength
            #Viking takes damage
            viking_damage = self.viking.receiveDamage(saxon_attack) 
            #viking is removed from army
            if self.viking.health <= 0:  
                self.vikingArmy.remove(self.viking)
            #should return result of calling receiveDamage() of a Viking with the strength of a Saxon
            return viking_damage

    def showStatus(self):
        if len(self.saxonArmy)==0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy)==0:
            return "Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy)>=1 and len(self.vikingArmy)>= 1:
            return "Vikings and Saxons are still in the thick of battle."