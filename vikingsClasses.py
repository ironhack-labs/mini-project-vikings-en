import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        #Set the initial annotation. 
        self.health = health 
        self.strength = strength
    
    def attack(self):
        #Attack method returns the strength property of the Soldier.
        return self.strength 

    def receiveDamage(self, damage):
        #Removes damage from the Soldiers health.
        self.health -=  damage 

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        #Inherit from the soldier class (parent class) and setting initial annotation for Viking.
        super().__init__(health, strength)
        self.name = name 

    def battleCry(self):
        #Returns specific phrase (to intimidate the enemy)
        return "Odin Owns You All!" 

    def receiveDamage(self, damage):
        #Check if the Viking is still alive after damage
        if self.health > 0: 
            #Returns message if Viking is still alive.
            return f"{self.name} has received {damage} points of damage"  
        else: 
            #Returns message if Viking has died. 
            return f"{self.name} has died in act of combat" 

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        #Inherit from the soldier class (parent class)
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        #Check if the Saxon is still alive after damage
        if self.health > 0: 
            #Returns message if Saxon is still alive.
            return f"A Saxon has received {damage} points of damage" 
        else: 
            #Returns message if Saxon has died. 
            return f"A Saxon has died in combat" 

# Davicente

class War():
    def __init__(self):
        #Initialize the war with empty armies for Vikings and Saxons.
        self.vikingArmy = []
        self.saxonArmy = []
        
    def addViking(self, viking):
        #Adds a single Viking to the VikingArmy list
        self.vikingArmy.append (viking) 
        
    def addSaxon(self, saxon):
        #Adds a single Saxon to the SaxonArmy list
        self.saxonArmy.append (saxon) 
        
    def vikingAttack(self): 
        #Selecting random viking and saxon.
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)

        #The selected Saxon receives damage equal to the Viking's strength
        result = random_saxon.receiveDamage(random_viking.strength) 

        #Removing defeated saxons.
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)

        #Returns the result of the attack 
        return result 

    def saxonAttack(self):
        #Selecting random viking and saxon.
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)

        #The selected Viking receives damage equal to the Saxon's strength
        result = random_viking.receiveDamage(random_saxon.strength) 

        #Removing defeated saxons.
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        
        #Returns the result of the attack 
        return result 

    def showStatus(self):
        #Determines and returns the current status of the battle
        if not self.saxonArmy:
            #All Saxons are defeated
            return "Viking have won the war of the century!"
        elif not self.vikingArmy:
            #All Vikigns are defeated
            return "Saxons have fought for their lives and survive another day..."
        else: 
            #Both armies still have warriors left
            return "Vikings and Saxons are still in the thick of battle."