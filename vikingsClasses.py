import random # We will use random in the code later, that is the reason why we should import this library

#Parent class (Soldier): General definition of the Soldiers (2 arguments)
# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength  #This argument is important in deciding the results on the battlefield
    def attack(self): #This is the main funtion that we will use in battlefield
        return self.strength 

    def receiveDamage(self, damage):
        # self.health = self.health - damage
        self.health -= damage #This line shows us how the soldier loses health throughout the war
        return
    
#Child classes (#1 Viking and #2 Saxon):

# Viking

class Viking(Soldier): #In this line we are calling the Parent class (Soldier), in order to use its methods
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health,strength) #Here we are acceding to the methods of the PARENT class

#Attack should be inherited from Soldier

    def battleCry(self):    #Viking style!
        return "Odin Owns You All!" 

    def receiveDamage(self, damage): #Reimplement from Parent class (Soldier)
        self.health -= damage #It is important noticed that "health" is an argument from Parent class (Soldier)
        if self.health > 0: #If health is bigger than 0 means that the Viking is still alive!!!
            return f"{self.name} has received {damage} points of damage" #Vikigns is more personalizated it means that it includes the Vikings name!
        
        else:                 #If health is less than 0 the code assumes the Viking is dead </3!!
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier): #In this line we are calling the Parent class (Soldier), in order to use its methods
    def __init__(self, health, strength):   #There is 1 argument less than Vikings class ("no name")
        super().__init__(health,strength) #Here we are acceding to the methods of the PARENT class

#Attack is inherited from the Parent class (Soldier)

    def receiveDamage(self, damage): #Reimplement from Parent class (Soldier)
         # self.health = self.health - damage
        self.health -= damage #It is important noticed that "health" is an argument from Parent class (Soldier)
        if self.health > 0: #If health is bigger than 0 means that the Saxon is still alive!!!   
            return f"A Saxon has received {damage} points of damage" 
        
        else:                 #If health is less than 0 the code assumes the Saxon is dead </3!!
            return f"A Saxon has died in combat"

# Let´s begin the war!!!

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking): 
        self.vikingArmy.append(viking) #Adds 1 Viking to the vikingArmy. If you want a 10 Viking army, you need to call this 10 times.
                                       # if you wanna add viking use: self.vikingArmy.append(viking1)
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = viking.attack()  #damage equal to the strength of a Viking // strength of a Viking = attack
        result_saxon_receiveDamage = saxon.receiveDamage (damage)
        if saxon.health <= 0:
           self.saxonArmy.remove(saxon) #remove dead saxon from the army
        return result_saxon_receiveDamage   #result of calling receiveDamage() of a Saxon with the strength of a Viking
  

    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        damage = saxon.attack()  #damage equal to the strength of a saxon // strength of a saxon = attack
        # A Viking receives the damage equal to the strength of a Saxon
        result_viking_receiveDamage = viking.receiveDamage (damage) #strength of a saxon = attack
        if viking.health <= 0:
           self.vikingArmy.remove(viking)  #remove dead vikings from the army
        return result_viking_receiveDamage #result of calling receiveDamage() of a Viking with the strength of a Saxon


    def showStatus(self):
        if len(self.saxonArmy)  == 0: 
           return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0: 
           return"Saxons have fought for their lives and survive another day..."
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >= 1: #if there are at least 1 Viking and 1 Saxon
            return "Vikings and Saxons are still in the thick of battle."
        


