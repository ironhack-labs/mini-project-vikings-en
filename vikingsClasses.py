import random

# Soldier # Parent class
class Soldier:
    
    def __init__(self, health, strength):   # The constructor method initializes each new Soldier object
                                            # it takes two arguments => health and strength
        self.health = health #The health attribute shows how much life the solider has
        self.strength = strength #The strength attribute shows how powerful the solider's attack is

    def attack(self): # The attack() method to simulate the soldier attacking an enemy
        return self.strength # It returns the soldier's strength value as the damage received
    
    def receiveDamage(self, damage): # The receiveDamage() method to simulate the soldier taking damage from an attack
        self.health -= damage        # The soldier's health substracted from the damage
    
#Example
soldier1=Soldier(100, 50) #creating soldier 1 with 100 health and 50 strength
print(soldier1.attack()) #return the soldier's strength : output is 50
print(soldier1.receiveDamage(20)) #soldier taking 20 damage
print(soldier1.health) #shows health reduced after damage: out is 80



#Example
soldier1=Soldier(100, 50)
soldier1.attack()
soldier1.receiveDamage(20)
soldier1.health


# Viking #Child Class
class Viking(Soldier): 
    def __init__(self, name, health, strength): #The constructor method initializes each Viking object
                                                #it takes 3 arguments => name, health, strength
        super().__init__(health, strength) #Using super() to call the parent class Soldier constructor
        self.name = name  #Viking class has its own unique attribute:name

    def battleCry(self):     #The battleCry() method returns a specific war cry to the Viking
        return "Odin Owns You All!"

    def receiveDamage(self, damage):  #Overriding the method from Soldier but respond differently when taking damage
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
#Example
viking1=Viking("Rafael", 150, 90) #creating a new viking named Rafael with 150 health and 90 strength
viking2=Viking("Hayley", 120, 70) #creating a new viking named Hayley with 120 health and 70 strength

print(viking1.battleCry()) #"Odin Owns You All!"
print(viking2.attack()) #70 (inherited fromm Soldier)
print(viking1.receiveDamage(40)) #Rafael has received 40 points of damage


# Saxon #Child Class
class Saxon(Soldier):
    def __init__(self, health, strength):    #The constructor method initializes each Saxon object
                                             #it takes 2 arguments => health, strength
        super().__init__(health, strength)  #Using super() to call the parent class Soldier constructor

    def receiveDamage(self, damage): #Overriding the method from Soldier, and it defines how saxon reacts when taking damage
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in act of combat"
        
#Example
saxon1=Saxon(60, 30) #creating a new saxon with 60 health and 30 strength
saxon2=Saxon(100, 60) #creating a new saxon with 100 health and 60 strength
print(saxon1.attack()) # 30 (inherited from Soldier)
print(saxon2.receiveDamage(60)) # Saxon2 has died in act of combact  



class War(): # Define a class War() that manages battles between Vikings and Saxons
    def __init__(self): #The constructor method initializes two empty lists for the Viking and Saxon armies
        self.vikingArmy = [] 
        self.saxonArmy = []

    def addViking(self, viking): #Method to add a viking to the Vikingarmy
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):  #Method to add a saxon to the Saxonarmy
        self.saxonArmy.append(saxon)
    

    def vikingAttack(self):     #Simulate a Viking attack on a Saxon

        #random choice of the soldier from each army
        viking = random.choice(self.vikingArmy) 
        saxon = random.choice(self.saxonArmy)

        saxonResult = saxon.receiveDamage(viking.strength) #The Saxon receives damage equal to the Viking's strength

        if saxon.health <= 0:         #If Saxon's health reaches zero or below, remove from the army
            self.saxonArmy.remove(saxon)   

        return saxonResult         #Return the result of the Saxon's receiveDamage() method

    def saxonAttack(self):   #Simulate a Saxon attack on a Viking
       
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)
        
        vikingResult = viking.receiveDamage(saxon.strength)
        
        if viking.health <=0:
            self.vikingArmy.remove(viking)

        return vikingResult


    def showStatus(self):     #Display the current status of the war

        if len(self.saxonArmy) == 0:          #if no Saxons left, Vikings win
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:          #if no Vikings left, Saxons win
            return "Saxons have fought for their lives and survive another day..."
        else:         #Otherwise, battle is ongoing
            return "Vikings and Saxons are still in the thick of battle."



