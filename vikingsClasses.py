import random

# Soldier


class Soldier:
    def __init__(self, health, strength): # should receive 2 arguments (health & strength)
        self.health = health # should receive the health property as its 1st argument
        self.strength = strength # should receive the strength property as its 2nd argument
    
    def attack(self): # should be a function & should receive 0 arguments
        return self.strength # should return the strength property of the Soldier

    def receiveDamage(self, damage): # should be a function & should receive 1 argument
        self.health -= damage # should remove the received damage from the health property
        # Shouldn't return anything
    

# Viking

class Viking(Soldier): # Viking should inherit from Soldier
    def __init__(self, name, health, strength): # should receive 3 arguments (name, health & strength)
        self.name = name # should receive the name property as its 1st argument
        self.health = health # should receive the health property as its 2nd argument
        self.strength = strength # should receive the strength property as its 3rd argument

    def battleCry(self): # should be a function & should receive 0 arguments
        return "Odin Owns You All!" # should return "Odin Owns You All!"

    def receiveDamage(self, damage): # should be a function & should receive 1 argument (the damage)
        self.health -= damage # should remove the received damage from the health property
        if self.health > 0: # if the Viking is still alive, it should return "NAME has received DAMAGE points of damage"
            return f"{self.name} has received {damage} points of damage"
        else: # if the Viking dies, it should return "NAME has died in act of combat"
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier): # Saxon should inherit from Soldier

    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def receiveDamage(self, damage):
        self.health -= damage # should remove the received damage from the health property
        if self.health > 0: # if the Saxon is still alive, it should return "A Saxon has received DAMAGE points of damage"
            return f"A Saxon has received {damage} points of damage"
        else: # if the Saxon dies, it should return "A Saxon has died in combat"
            return "A Saxon has died in combat"

## War - Define the game
# Davicente

class War():
    def __init__(self): # When we first create a War, the armies should be empty. We will add soldiers to the armies later & should receive 0 arguments
        self.vikingArmy = [] # should assign an empty array to the vikingArmy property
        self.saxonArmy = [] # should assign an empty array to the saxonArmy property

    def addViking(self, viking):
        self.vikingArmy.append(viking) # should add the received Viking to the army
        # shouldn't return anything
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon) # should add the received Saxon to the army
        # shouldn't return anything
    
    def vikingAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        # should make a Saxon receiveDamage() equal to the strength of a Viking
        result1 = saxon.receiveDamage(viking.strength)

        if saxon.health <= 0: # should remove dead saxons from the army
            self.saxonArmy.remove(saxon)

        return result1 # should return result of calling receiveDamage() of a Saxon with the strength of a Viking
            
    def saxonAttack(self):
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        result2 = viking.receiveDamage(saxon.strength) # should make a Viking receiveDamage() equal to the strength of a Saxon

        if viking.health <= 0: # should remove dead vikings from the army
            self.vikingArmy.remove(viking) # should return result of calling receiveDamage() of a Viking with the strength of a Saxon

        return result2
            

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return f"Vikings have won the war of the century!"
        
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        
        elif len(self.vikingArmy) >= 1 and len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
    
    pass


