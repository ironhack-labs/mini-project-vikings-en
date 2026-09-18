import random

# Soldier

class Soldier:
    def __init__(self, health, strength):
        # your code here
        self.health = health
        self.strength = strength

    def attack(self):
        # your code here
        return self.strength

    def receiveDamage(self, damage):
        # your code here
        self.health -=damage
   

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)
        self.name = name
    def attack(self):
        return super().attack()
    def battleCry(self):
        # your code here
        return "Odin Owns You All!"
    def receiveDamage(self,damage):
         # your code here
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        # your code here
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikingArmy = [] #code asked to keep the army empty
        self.saxonArmy = []

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)

    
    def addSaxon(self, saxon):
        # your code here
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        # your code here
        random_chosen_saxon = random.choice(self.saxonArmy)
        random_chosen_viking = random.choice(self.vikingArmy)
        result_vikingAttack = random_chosen_saxon.receiveDamage(random_chosen_viking.attack())
        if random_chosen_saxon.health <=0:
            self.saxonArmy.remove(random_chosen_saxon)

        return result_vikingAttack


    def saxonAttack(self):
        # your code here
        random_chosen_saxon = random.choice(self.saxonArmy)
        random_chosen_viking = random.choice(self.vikingArmy)
        result_saxsonAttack = random_chosen_viking.receiveDamage(random_chosen_saxon.attack())
        if random_chosen_viking.health <= 0:
            self.vikingArmy.remove(random_chosen_viking)
        
        return result_saxsonAttack

    def showStatus(self):
        # your code here
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."   
    pass


