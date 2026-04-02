import random

# Soldier

# Constructor Function definition:

class Soldier:
    def __init__(self, health, strength):   # constructor function with 2 arguments: health and strength
        self.health = health           # receives the health property as its 1st argument
        self.strength = strength         # receives the strength property as its 2nd argument

# Methods definition:
    
    def attack(self):   # 0 arguments
        return self.strength    # returns the strength property of the Soldier class

    def receiveDamage(self, damage):   # receives 1 argument (the damage)
        self.health -= damage    # removes the received damage from the health property


# Viking

# Constructor Function definition:

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)    # inheriting these from the Soldier class
        self.name = name      # adding additional name attribute (specific to this class)

# Methods definition:
 
    #### attack method inherited from parent class Soldier ####

    def battleCry(self):   # 0 arguments
        return "Odin Owns You All!"               # message returned in this case

    def receiveDamage(self, damage):    # 1 argument: damage  ;  case of polymorphism - same method, but with a distinct behaviour compared to the soldier
        self.health -= damage                # removes the received damage from the health property
        if self.health > 0:          # assuming the Viking is alive
            return f"{self.name} has received {damage} points of damage"    # returning this message on points of damage
        else:
            return f"{self.name} has died in act of combat"     # otherwise, returning this message


# Saxon

# Constructor Function definition:

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)   # inheriting these from the Soldier class

# Methods definition:

    def receiveDamage(self, damage):      # 1 argument: damage
        self.health -= damage        # removes the received damage from the health property
        if self.health > 0:           # assuming the Saxon is alive
            return f"A Saxon has received {damage} points of damage"   # returning this message on points of damag
        else:
            return "A Saxon has died in combat"   # otherwise, returning this message


# Davicente

# Constructor Function definition:

class War():
    def __init__(self):
        self.vikingArmy = []        # initialising from an empty array 
        self.saxonArmy = []         # initialising from an empty array 
    
# Methods definition:

    def addViking(self, viking):           # 1 argument: viking
        self.vikingArmy.append(viking)      # adding viking; no return
    
    def addSaxon(self, saxon):                 # 1 argument: saxon
        self.saxonArmy.append(saxon)           # adding saxon; no return
        
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)       # choosing viking at random
        saxon = random.choice(self.saxonArmy)          # choosing saxon at random

        encounter = saxon.receiveDamage(viking.attack())       # encounter between the 2

        if saxon.health <= 0:                               # dead saxons removed via this condition
            self.saxonArmy.remove(saxon)
    
        return encounter
    
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)             # choosing saxon at random
        viking = random.choice(self.vikingArmy)           # choosing viking at random

        encounter = viking.receiveDamage(saxon.attack())               # encounter between the 2

        if viking.health <= 0:                         # dead vikings removed via this condition
            self.vikingArmy.remove(viking)
    
        return encounter

    def showStatus(self):
        if len(self.saxonArmy) == 0:                        # saxons all gone
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:                       # vikings all gone
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    

    pass


