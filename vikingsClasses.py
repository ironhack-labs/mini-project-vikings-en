import random

###########################################
########## Soldier ########################
###########################################
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage

###########################################
########## Viking #########################
###########################################
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)                                                  # taking the things from PARENT class
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.health -= damage                                                               # subtract damage taken from actual health
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

###########################################
########## Saxon ##########################
###########################################
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)                                                # taking the things from PARENT class

    def receiveDamage(self, damage):
        self.health -= damage                                                               # subtract damage taken from actual health
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

###########################################
########## Davicente ######################
###########################################
class War():
    def __init__(self):
        self.vikingArmy = []                                                                # create an empty list to store the Viking army
        self.saxonArmy = []                                                                 # create an empty list to store the Saxon army

    def addViking(self, viking):
        self.vikingArmy.append(viking)                                                      # append a new Instance of the input class to the list
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)                                                        # append a new Instance of the input class to the list
    
    def vikingAttack(self):
        defender_saxon = random.choice(self.saxonArmy)                                      # checking which saxon is the defender (random)
        attacker_viking = random.choice(self.vikingArmy)                                    # checking which viking is the attacker (random)

        return_value = defender_saxon.receiveDamage(attacker_viking.strength)               # updating defenders health
                                                                                            # -> executing the defenders method .receiveDamage

        if defender_saxon.health <= 0:                                                      # checking if the defender died by the attack
            self.saxonArmy.remove(defender_saxon)                                           # if so, the defender will be deleted from the list
        
        return return_value
    
    def saxonAttack(self):
        defender_viking = random.choice(self.vikingArmy)                                    # checking which viking is the defender (random)
        attacker_saxon = random.choice(self.saxonArmy)                                      # checking which saxon is the attacker (random)

        return_value = defender_viking.receiveDamage(attacker_saxon.strength)               # updating defenders health
                                                                                            # -> executing the defenders method .receiveDamage

        if defender_viking.health <= 0:                                                     # checking if the defender died by the attack
            self.vikingArmy.remove(defender_viking)                                         # if so, the defender will be deleted from the list
        
        return return_value
    
    def showStatus(self):
        if len(self.saxonArmy) <= 0:                                                        # if the list of Saxons is empty -> Vikings have won
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) <= 0:
            return "Saxons have fought for their lives and survive another day..."          # if the list of Vikings is empty -> Saxons have won
        else:
            return "Vikings and Saxons are still in the thick of battle."                   # if both lists are still containing soldiers 
                                                                                            # -> the fight is not over
