"""
1 - Assign a random viking name so user doesn't have to input it. adds also a name to Saxons.
2 - Set health to 100 and attack as random(1,100) for Vikings and Saxons.
3 - Ask for army Sizes (user input)
4 - Create a function that creates as many Saxon/Viking as the user asked for and add them to the armies inside war.
5 - Set the workflow with a round system and a while loop that runs until one of the armies is empty
6 - Show status every 10 rounds
7 - Show final status at the end of the war
"""

import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        # print(f"Soldier received {self.damage} damage. his health is now {self.health}")

# Viking

class Viking(Soldier):
    def __init__(self, health, strength):
        vikings_names = ["Harald", "Bjorn", "Erik", "Leif", "Ragnar", "Ivar", "Sigurd", "Olaf", "Gunnar", "Thor"]   # Create a list of vikings names to randomly assign to each viking created
        self.name = random.choice(vikings_names)    # Assign a radom name from vikings_name
        super().__init__(health, strength)

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        elif self.health <= 0:
            return f"{self.name} has died in act of combat"
    
    def __repr__ (self):     # Print name, HP and ATK of the wviking for better visualization
        return f"{self.name}, HP: {self.health}, ATK: {self.strength} "

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        saxon_names = ["Alfred", "Cedric", "Cuthbert", "Edmund", "Edward", "Godwin", "Harold", "Leofric", "Oswald", "Wulfric"]
        super().__init__(health, strength)
        self.name = random.choice(saxon_names)

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= self.damage
        if self.health > 0:
            return f"A Saxon has received {self.damage} points of damage"
        elif self.health <= 0:
            return f"A Saxon has died in combat"
    
    def __repr__ (self):     # Print name, HP and ATK of the Saxon for better visualization
        return f"{self.name}, HP: {self.health}, ATK: {self.strength} "

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        message = saxon.receiveDamage(viking.attack())
        if "died" in message:
            self.saxonArmy.remove(saxon)
        return message

    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        message = viking.receiveDamage(saxon.attack())
        print(message)
        if "died" in message:
            self.vikingArmy.remove(viking)
        return message

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            print("Vikings have won the war of the century!")
            return "Vikings have won the war of the century!"    
        elif len(self.vikingArmy) == 0:
            print("Saxons have fought for their lives and survive another day...")
            return "Saxons have fought for their lives and survive another day..." 
        else: 
            print("Vikings and Saxons are still in the thick of battle.")
            return "Vikings and Saxons are still in the thick of battle."
            

    pass

# War Setup

def create_saxon():
    health = 100
    strength = random.randint(1,100)
    return Saxon(health, strength)

def create_viking():
    health = 100
    strength = random.randint(1,100)
    return Viking(health, strength)

# User give the armies size
saxon_army_size = int(input("How big is the Saxon army ? "))
vikings_army_size = int(input("How big is the Viking army ? "))

# Create the war instance
war = War()

# Add the soldiers to the armies
for i in range(saxon_army_size):
    saxon = create_saxon()
    war.addSaxon(saxon)

for i in range(vikings_army_size):
    viking = create_viking()
    war.addViking(viking)

"""Round workflow:
While one army has soldiers:
1 - Randomly choose a Viking or Saxon to attack
2 - Randomly choose a target from the opposite army
4 - Check if the target is dead and remove from army if so
5 - Show status every 10 rounds
6 - Show final status at the end of the war
"""
round = 1
while len(war.saxonArmy) > 0 and len(war.vikingArmy) > 0:
    attacker = random.choice(["viking","saxon"])
    if attacker == "saxon":
        war.saxonAttack()
    else:
        war.vikingAttack()
    round += 1
    if round % 10 == 0: # Show status every 10 rounds
        print(f"Round {round}:")
        war.showStatus()
print(f"After {round} days of battle.")
war.showStatus()




"""
Priest class

class Priest(Soldier):
    def __init__(self, health, magic):
        super().__init__(health)
        self.magic = magic

"""