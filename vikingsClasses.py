import random

# Soldier
class Soldier: # added 2 arguments (health and strength) to the constructor function
    def __init__(self, health, strength):
        self.health = health # added the first instance corresponding to the first input argument
        self.strength = strength # added the second instance corresponding to the second input argument
    
    def attack(self): # added no argument to the method
        return self.strength # the strength property of the Soldier is returned 
    
    def receiveDamage(self, damage): # added 1 argument to the method; no output is returned
        self.health -= damage # remove the damage from the health property
        
# Viking
class Viking(Soldier): # Viking is inherited from Soldier 
    def __init__(self, name, health, strength): # since Viking is an inherited class, the constructor
        # function admits the 2 arguments of parent Soldier. on top of those, a new input argument 
        # "name" is passed. the input arguments are passed in order -> name, health, strength
        super().__init__(health, strength) # the super() function gives access to methods and 
        # properties of the parent class
        self.name = name # added the first instance corresponding to the first input argument
        
    def battleCry(self): # battleCry() is a function which admits no input argument
        return "Odin Owns You All!" # it returns the text value "Odin Owns You All!"
    
    def receiveDamage(self, damage): # reimplemented the receiveDamage() method for Viking. it's a
        # function since it's been declared after 'def' and the single argument 'damage' is passed.
        self.health -= damage # remove the damage from the health property
        # conditional block: 
        # 1. if the Viking is still alive (self.health > 0), this statement is returned ->
        # "NAME has received DAMAGE points of damage"
        # 2. otherwise if the Viking dies, the statement "NAME has died in act of combat" is returned 
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"   

# Saxon
class Saxon(Soldier): # Saxon is inherited from Soldier
    def __init__(self, health, strength): # the constructor function admits 2 arguments 
        # (health & strength) in order 
        super().__init__(health, strength) # gives access to methods and properties of Soldier
    
    # no need to reimplement the attack() method, since it's already been inherited from Soldier
    
    def receiveDamage(self, damage): # the receiveDamage() method needs to be reimplemented since
        # it's a different version than that in Soldier. it's a function and admits 1 argument (the damage)
        self.health -= damage # it removes the received damage from the health property
        # conditional block:
        # 1. if the Saxon is still alive (self.health > 0), this statement is returned -> 
        # "A Saxon has received DAMAGE points of damage"
        # 2. otherwise if the Saxon dies, the statement "A Saxon has died in combat" is returned
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# War
# the War constructor admits 5 methods to its prototype: 
# 1.addViking() 2.addSaxon() 3.vikingAttack() 4.saxonAttack() 5.showStatus()
class War:
    def __init__(self): # the constructor admits no argument
        self.vikingArmy = [] # an empty array is assigned to the vikingArmy property
        self.saxonArmy = [] # an empty array is assigned to the saxonArmy property
    
    def addViking(self, viking): # the addViking() method is a function with 1 argument: a "viking" 
        # object. it returns no output. please note that lowercase viking is used to avoid confusion
        # and possible conflict with the class Viking
        self.vikingArmy.append(viking) # it adds 1 Viking to the vikingArmy
    
    def addSaxon(self, saxon): # similar to addViking()
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self): # vikingAttack() is a function with no input
        if self.saxonArmy and self.vikingArmy: # if both instances are evoked
            attacker = random.choice(self.vikingArmy) # a Viking chosen at random as an attacker
            defender = random.choice(self.saxonArmy) # a Saxon chosen at random doesn't attack back
            
            # Saxon receiveDamage() equal to the strength of a Viking. name it the variable "result"
            # dead Saxons (defender.health <= 0) are removed from the army
            # the result is returned
            result = defender.receiveDamage(attacker.attack()) 
            if defender.health <= 0:
                self.saxonArmy.remove(defender)
            return result
    
    def saxonAttack(self): # similar to vikingAttack()
        if self.saxonArmy and self.vikingArmy: 
            attacker = random.choice(self.saxonArmy)
            defender = random.choice(self.vikingArmy)
            result = defender.receiveDamage(attacker.attack())
            if defender.health <= 0:
                self.vikingArmy.remove(defender)
            return result
    
    def showStatus(self): # showStatus() is a function with no input 
        # returns "Vikings have won the war of the century!" if the Saxon array is empty
        if not self.saxonArmy: 
            return "Vikings have won the war of the century!"
        # returns "Saxons have fought for their lives and survive another day..." if the Viking array is empty
        elif not self.vikingArmy: 
            return "Saxons have fought for their lives and survive another day..."
        # returns "Vikings and Saxons are still in the thick of battle." if there are at least 1 Viking and 1 Saxon
        else:
            return "Vikings and Saxons are still in the thick of battle."
    
    pass
