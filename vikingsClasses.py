import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
            
    def attack(self):
        return(self.strength)

    def receiveDamage(self, damage):
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return("Odin Owns You All!")

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f"{self.name} has received {damage} points of damage")
        else:
            return(f"{self.name} has died in act of combat")
        


# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return (f"A Saxon has received {damage} points of damage")
        else:
            return(f"A Saxon has died in combat")

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        self.valhalla = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        if self.vikingArmy and self.saxonArmy:
            target = random.choice(self.saxonArmy)
            attacker = random.choice(self.vikingArmy)
            result = target.receiveDamage(attacker.strength)                 # Self face punching not allowed - target and attacker need to be different.

            if target.health <= 0:
                self.saxonArmy.remove(target)                       # no target should be starting combat with 0 health so this does not cause problems
                try:
                    target = random.choice(self.saxonArmy)
                except:                                             # Target army is empty
                    self.showStatus()                               # If unable to find any targets the fight is over.

            print(attacker.battleCry())                             # battlecry() finally gets used
            print(result)
            return(result)                                          # return() was redundant, as we dont need output just modification of exisiting objects                           

    
    def saxonAttack(self):
        if self.vikingArmy and self.saxonArmy:
            target = random.choice(self.vikingArmy)
            attacker = random.choice(self.saxonArmy)
            result = target.receiveDamage(attacker.strength)                 # Self face punching not allowed - target and attacker need to be different.

            if target.health <= 0:
                self.valhalla.append(target)
                self.vikingArmy.remove(target)                      # no target should be starting combat with 0 health so this does not cause problems
                try:
                    target = random.choice(self.vikingArmy)
                except:                                             # Target army is empty
                    self.showStatus()                               # If unable to find any targets the fight is over.
            print(result)
            return(result)                                           # return() was redundant, as we dont need output just modification of exisiting objects  
        

    def showStatus(self):
        if not self.vikingArmy:
            return("Saxons have fought for their lives and survive another day...")
        elif not self.saxonArmy:
            return("Vikings have won the war of the century!")
        else:
            return("Vikings and Saxons are still in the thick of battle.")


    pass

