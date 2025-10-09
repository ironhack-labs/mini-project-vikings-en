import random

# Soldier


class Soldier:
    def __init__(self, health, strength): # constructor function creating a Soldier, 2 arguments: health (1st) and strength (2nd)
        self.health = health      # stores health value in the instance
        self.strength = strength  # stores strength value in the instance
    def attack(self): # attack() method takes no arguments as told in excercise
        return self.strength      # returns Soldier's strength property (attack power)

    def receiveDamage(self, damage): # method receiveDamage() , 1 argument: damage
        self.health -= damage     # subtract damage from the Soldier's health
        #as no return self.health, return is = NONE


# Viking

class Viking(Soldier): # this class is being inherited from (soldier)
    def __init__(self, name, health, strength): # Constructor, new object with 3 arguments: name (special property for Viking only), health (passed down; soldier), strength (passed down; soldier).
        super().__init__(health, strength) # "super()" Calls the parent (Soldier) constructor to set health and strength
        self.name = name   # assign the name property (extra for Vikings, only they will have it)

    # Summary: Viking constructor first uses the parent’s constructor to set up the shared attributes (health and strength), and then it sets its own unique attribute (name).

    def receiveDamage(self, damage):
        self.health -= damage   # subtract damage from health
        if self.health > 0: # if greater than 0, viking is alive
            return f"{self.name} has received {damage} points of damage" # Viking is still alive → return message with name and damage
        else:
            return f"{self.name} has died in act of combat" # Viking is dead → return death message

    def battleCry(self): # battleCry() method
        return "Odin Owns You All!"   # returns string as battle cry
    

# Saxon

class Saxon(Soldier): #Define a new class "Saxons"
    def __init__(self, health, strength): # Constructor, new object, 2 arguments
        super().__init__(health, strength) # call the parent Soldier constructor to set health and strength

    def receiveDamage(self, damage):  # Method, receive damge
        self.health -= damage # subtract damage from Saxon's health
        if self.health > 0: # check if Saxon is still alive (healt above 0)
            return f"A Saxon has received {damage} points of damage"# f-string, replace variable values inside the {}, so it looks inside the variable damage in this case and replaces with value (X)
        else:
            return "A Saxon has died in combat" # if health below 0 it return string


# Davicente

import random  # needed to pick random army members

# War
class War:
    def __init__(self): # constructor takes 0 arguments
        self.vikingArmy = []  # start with an empty list for Vikings
        self.saxonArmy = []   # start with an empty list for Saxons

    def addViking(self, viking): # creates method, and receives 1 argument: a Viking instance
        self.vikingArmy.append(viking)  # add the Viking to the army

    def addSaxon(self, saxon): # creates method receiving 1 argument: a Saxon instance
        self.saxonArmy.append(saxon)  # add the Saxon to the army

    def vikingAttack(self): # method,no arguments taken but it means that it choose a random Saxon (target) and a random Viking (attacker)
        saxon_index = random.randrange(len(self.saxonArmy))  # saxon_index stores the random position of rnadom.ranrange (gives a random number between the indexes in the list and so picks a random saxon form the army)
        viking_index = random.randrange(len(self.vikingArmy))  # same as above but for viking army

        saxon = self.saxonArmy[saxon_index]   # get that Saxon object, "saxon" here is an object from the class "Saxon" ehich can hold data/ attributes, in this case strength and health
        viking = self.vikingArmy[viking_index]  # get that Viking object, smae as above but objet also hold name as attribute

        damage = viking.attack()              # Viking’s attack power = Viking.strength
        result = saxon.receiveDamage(damage)  # call Saxon.receiveDamage(damage) and capture its return string

        if saxon.health <= 0: # if Saxon died (health 0 or below), remove from army
            self.saxonArmy.pop(saxon_index)
            return result  # return the exact string returned by Saxon.receiveDamage()

    def saxonAttack(self): # choose a random Viking (target) and a random Saxon (attacker)
        viking_index = random.randrange(len(self.vikingArmy))  # random valid index into vikingArmy
        saxon_index = random.randrange(len(self.saxonArmy))    # random valid index into saxonArmy

        viking = self.vikingArmy[viking_index]  # get that Viking object
        saxon = self.saxonArmy[saxon_index]     # get that Saxon object

        damage = saxon.attack()                 # Saxon’s attack power = Saxon.strength
        result = viking.receiveDamage(damage)   # call Viking.receiveDamage(damage) and capture its return string

        if viking.health <= 0: # if Viking died (health 0 or below), remove from army
            self.vikingArmy.pop(viking_index)
            return result  # return the exact string returned by Viking.receiveDamage()

    def showStatus(self):
        if len(self.saxonArmy) == 0: # if no Saxons left
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) == 0: # if no Vikings left
            return "Saxons have fought for their lives and survive another day..." # both armies still have at least 1 soldier
        return "Vikings and Saxons are still in the thick of battle."


