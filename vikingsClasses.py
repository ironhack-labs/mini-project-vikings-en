import random


class Soldier:
    #constructor funcion
    def __init__(self, health, strength):
        self.health= health 
        self.strength= strength   
    
    #attack method
    def attack(self):
        return self.strength 
    
    #receiveDamage
    def receiveDamage(self, damage):
        self.health -=damage 


class  Viking(Soldier):

    def __init__(self,name, health, strength):
        super().__init__(health, strength)
        self.name= name
    
    def receiveDamage(self, damage):
        self.health -=damage 

        if self.health <=0:
            return f"{self.name} has died in act of combat"
        else:
            return f"{self.name} has received {damage} points of damage"
        
    def battleCry(self):
        return "Odin Owns You All!"


class Saxon (Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    
    def receiveDamage(self, damage):
        self.health -=damage 

        if self.health <=0:
            return f"A Saxon has died in combat"
        else:
            return f"A Saxon has received {damage} points of damage"


class War ():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
    #Method 1
    def addViking(self, Viking):
        self.vikingArmy.append(Viking)

    #Method 2
    def addSaxon(self, Saxon):
        self.saxonArmy.append(Saxon)
    
    #Method 3
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        saxon_receive_damage = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)
        return saxon_receive_damage
    
    #Method 4
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        viking_receive_damage = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return viking_receive_damage
    
    #Method 5
    def showStatus(self):
        if len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..." 
        elif len(self.saxonArmy) == 0:  
            return  "Vikings have won the war of the century!"
        else:
            return  "Vikings and Saxons are still in the thick of battle."
       



