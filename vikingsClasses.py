import random
from unittest import result

# Soldier

#constructor function
#should receive 2 arguments (health & strength)

class Soldier:
    def __init__(self, health, strength):
        #should receive the health property as its 1st argument
        #should receive the strength property as its 2nd argument
        self.health = health
        self.strength = strength


    #attack() method
    #should be a function
    #should receive 0 arguments
    def attack(self):
        ##should return the strength property of the Soldier
        return self.strength


#receiveDamage() method
#should be a function
#should receive 1 argument (the damage)
    def receiveDamage(self, damage):
        # should remove the received damage from the health property (i.e. health - damage)
        self.health -= damage
        #shouldn't return anything  


# Viking

# A Viking class inherits from Soldier
class Viking(Soldier):
    #A Viking is a Soldier with an additional property, their name. 
    # The other properties are similar to the Soldier class (health & strength)
    # So constructor function should now receive 3 arguments (name, health & strength)
    def __init__(self, name, health, strength):
        # Now I use the Soldier constructor to store health and strength store the name inside this Viking
        super().__init__(health, strength)
        # Now remeber "self.health = health" and this "self.strength = strength" have already been set in the Soldier class, so I only need  for "name".
        self.name = name

    # WHEN the Viking uses battleCry:
    # return "Odin Owns You All"
    def battleCry(self):
        return "Odin Owns You All!"

    
    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
                return f"{self.name} has received {damage} points of damage"
        else:
                return f"{self.name} has died in act of combat"


# Saxon

#Saxon should inherit from Soldier
class Saxon(Soldier):
    def __init__(self, health, strength):
        #use the Soldier constructor to store or receive health and strength
        super().__init__(health, strength)

#When a Saxon receives damage, subtract it from health.
#If the Saxon is still alive, return a damage message.
#If the Saxon dies, return a death message.
    def receiveDamage(self, damage):
        self.health -= damage

        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# Davicente

#constructor function
# When we first create a War, the armies should be empty. We will add soldiers to the armies later.
#should receive 0 arguments
#should assign an empty array to the vikingArmy property
#should assign an empty array to the saxonArmy property

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    # addViking() method
    def addViking(self, viking):
        # Receive one Viking object
        # Add that Viking to the Viking army
        # No value needs to be returned.
        self.vikingArmy.append(viking)
     
    # addSaxon() method
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
        
    #vikingAttack() method
    def vikingAttack(self):
        # choose one random Viking from the Viking army
        viking = random.choice(self.vikingArmy)
        # choose one random Saxon from the Saxon army
        saxon = random.choice(self.saxonArmy)
        # let the Saxon receive damage equal to the Viking's strength
        # save the returned message
        result = saxon.receiveDamage(viking.strength)
        # if the Saxon's health is 0 or below,
        # remove that Saxon from the Saxon army
        if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
                # return the damage/death message
        return result

    # saxonAttack() method
    def saxonAttack(self):
        # choose one random Saxon from the Saxon army
        saxon = random.choice(self.saxonArmy)
        # choose one random Viking from the Viking army
        viking = random.choice(self.vikingArmy)
        # let the Viking receive damage equal to the Saxon's strength
        # save the returned message
        result = viking.receiveDamage(saxon.strength)
        # if the Viking's health is 0 or below,
        # remove that Viking from the Viking army
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
            # return the damage/death message
        return result

    def showStatus(self):
        # if there are no Saxons left,
        # the Vikings have won
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        # if there are no Vikings left,
        # the Saxons have survived and won
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        # otherwise, both armies still have fighters,
        # so the battle is still going on
        else:
            return "Vikings and Saxons are still in the thick of battle."



