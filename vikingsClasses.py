import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
   
        self.health = health
        self.strength = strength
         
    def attack(self):
        return  self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        
# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):

        self.name = name
        super().__init__(health,strength)

    def battleCry(self):

        return "Odin Owns You All!"

    def receiveDamage(self, damage):

        self.damage = damage
        self.health = self.health - damage
        
        if self.health >0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
                

# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        
        super().__init__(health,strength)
        self.health = health 
        strength = 25
        self.strength = strength
    def receiveDamage(self, damage):
        
        self.damage = damage
        self.health = self.health - self.damage
        
        if self.health >0:
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
        self.vikingArmy.append(viking)
        
    def addSaxon(self, saxon):

        self.saxon = saxon 
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        
        random_saxon =  random.randint(0,len(self.saxonArmy)-1)
        rand_saxon = self.saxonArmy[random_saxon]
        
        rand_viking = random.randint(0,len(self.vikingArmy)-1)
        rand_viking = self.vikingArmy[rand_viking]
        saxon_dmg_taken = rand_viking.attack()
        
        final_saxon_health = rand_saxon.receiveDamage(saxon_dmg_taken)
        
        if rand_saxon.health <=0:
            self.saxonArmy.remove(self.saxon)
            
        return final_saxon_health

    def saxonAttack(self):
        random_saxon =  random.randint(0,len(self.saxonArmy)-1)
        rand_saxon = self.saxonArmy[random_saxon]
        rand_saxon.attack()
        
        viking_dmg_taken = rand_saxon.attack()
    
        rand_viking = random.randint(0,len(self.vikingArmy)-1)
        rand_viking = self.vikingArmy[rand_viking]
        
        final_viking_health =rand_viking.receiveDamage(viking_dmg_taken)

        if rand_viking.health <=0:
            self.vikingArmy.remove(self.viking)
            
        return final_viking_health

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.saxonArmy) == 1 and len(self.vikingArmy) == 1 :
            return "Vikings and Saxons are still in the thick of battle."
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."



