import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
       return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


# Saxon
class Saxon(Soldier): #defines new class-Saxon. Inherits properties and methods (health, strength, attack(), recieveDamage()) from soldier unless overrode
    def __init__(self, health, strength): #constructor fn...name is removed as Saxons have 2 arguments: health-property, strength-property (in order)
        super().__init__(health, strength) ##Calls the __init__ method of the parent class (Soldier) to initialize self.health and self.strength.. This avoids duplicating code using the solider setup for health and strength 

     #attack method: no need to write code, inherited from soilder!   
    
    def receiveDamage(self, damage): #reimplimented bc Saxon has different return values (overrides the recieveDamage() method from soilder bc Saxon has specific behaviors-must return a different message-see below)
        self.health -= damage #subtracts the damage value from health
        if self.health > 0: #if alive (after damage)
            return f"A Saxon has received {damage} points of damage" #message displayed if alive
        else: #if dead
            return "A Saxon has died in combat" #message displayed if dead


# War

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy  = []
    
    def addViking(self, viking):
        self.vikingArmy.append(viking)
        
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon) #adds saxon object to the saxonArmy list
    
    def vikingAttack(self):
        defendingSaxon = random.choice(self.saxonArmy) #1
        attackingViking = random.choice(self.vikingArmy) #2
        result = defendingSaxon.receiveDamage(attackingViking.attack()) # 3 and # 4
        if defendingSaxon.health <= 0: # 5.
            self.saxonArmy.remove(defendingSaxon) # 6.
        return result # 3.
        
           
    # def saxonAttack(self):
    #     The `Saxon` version of `vikingAttack()`. A `Viking` receives the damage equal to the `strength` of a `Saxon`.

    # - should be a function
    # - should receive **0 arguments**
    # - should make a `Viking` `receiveDamage()` equal to the `strength` of a `Saxon`
    # - should remove dead vikings from the army
    # - should return **result of calling `receiveDamage()` of a `Viking`** with the `strength` of a `Saxon`

    #1. random saxon (choose a randon saxon)
    #2. random Viking (chose a random viking)
    #3. check the saxon attack strength and saxon attack() method (call (pass) the attack method of the saxon to viking)
    #4. make a Viking receiveDamage() equal to the strength of a Saxon
    #5. if viking health < 0 -> remove from the list vikingArmy (remove the viking if health less than 0)
    #6. return the result of calling receiveDamage() of a Viking with the strength of a Saxon

    def saxonAttack(self):
        defendingViking = random.choice(self.vikingArmy) #1
        attackingSaxon = random.choice(self.saxonArmy) #2
        result = defendingViking.receiveDamage(attackingSaxon.attack()) #3 and #4. 
        if defendingViking.health <= 0: #5.
            self.vikingArmy.remove(defendingViking) #5.
        return result #6.
    
    def isWarOver(self):
        if len(self.saxonArmy) == 0 or len(self.vikingArmy) == 0:
            print(self.showStatus()) 
            return True
        return False

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."        

pass

     

    

# #vikingAttack() method
# A Saxon (chosen at random) has their receiveDamage() method called with the damage equal to the strength of a Viking (also chosen at random). This should only perform a single attack and the Saxon doesn't get to attack back.

# should be a function
# should receive 0 arguments
# should make a Saxon receiveDamage() equal to the strength of a Viking
# should remove dead saxons from the army
# should return result of calling receiveDamage() of a Saxon with the strength of a Viking

# 1. random saxon
# 2. random Viking
# 3. call saxon method receiveDamage -> value == viking strenght
# 4. return saxon health
# 5. check saxon health is < 0
# 6. if health < 0 ->  remove from the list saxonarmy
# 7. print updated saxon army list

#### `showStatus()` method
#1. if saxonArmy == 0 -> "Vikings have won the war of the century!"
#2. elif vikingArmy == 0 -> Saxons have fought for their lives and survive another day..."
#3. elif saxonArmy != 0 and vikingArmy !0 -> "Vikings and Saxons are still in the thick of battle."

#### constructor function
#- should receive **2 arguments** (health & strength)
#- should receive the **`health` property** as its **1st argument**
#- should receive the **`strength` property** as its **2nd argument**

#### `attack()` method
#(This method should be **inherited** from `Soldier`, no need to reimplement it.)
#- should be a function
#- should receive **0 arguments**
#- should return **the `strength` property of the `Saxon`**

#### `receiveDamage()` method
#(This method needs to be **reimplemented** for `Saxon` because the `Saxon` version needs to have different return values.)
#- should be a function
#- should receive **1 argument** (the damage)
#- should remove the received damage from the `health` property
#- **if the Saxon is still alive**, it should return _**"A Saxon has received DAMAGE points of damage"**_
#- **if the Saxon dies**, it should return _**"A Saxon has died in combat"**_