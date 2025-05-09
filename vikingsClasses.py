import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength

    def attack(self):
        return self.strength 

    def receiveDamage(self, damage):
        if self.health > damage:
            self.health -= damage
        
        else:
            self.health = 0



# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health,strength)
        self.name = name

    def battleCry(self):
        return 'Odin Owns You All!'

    def receiveDamage(self, damage):
        if self.health>damage:
            self.health -= damage
            return f'{self.name} has received {damage} points of damage'
        else:
            self.health = 0
            return f'{self.name} has died in act of combat'
        # self.health -= damage
        # if self.health > 0:
        #     return f'{self.name} has received {damage} points of damage'
        # else:
        #     return f'{self.name} has died in act of combat'

# Saxon

class Saxon(Soldier):

    def receiveDamage(self, damage):
        if self.health > damage:
            self.health -= damage
            return f'A Saxon has received {damage} points of damage'
        else: 
            self.health = 0
            return 'A Saxon has died in combat'
        # self.health -= damage
        # if self.health > 0:
        #     return f'A Saxon has received {damage} points of damage'
        # else:
        #     return 'A Saxon has died in combat'

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
        attacker = random.choice(self.vikingArmy)
        target = random.choice(self.saxonArmy)
        
        # there's a 15% chance for a Viking to use a battle cry
        # the battle cry increases their attack by 3
        if random.randrange(100) < 15:
            print(attacker.name,': ', attacker.battleCry())     # shouting the battle cry
            result = target.receiveDamage(attacker.attack()+3)  # increased attack strength
        else:
            result = target.receiveDamage(attacker.attack())    # regular attack
        
        
        if target.health == 0:
            self.saxonArmy.remove(target)
        
        return result
    
    def saxonAttack(self):
        attacker = random.choice(self.saxonArmy)
        target = random.choice(self.vikingArmy)
        
        result = target.receiveDamage(attacker.attack())
        
        if target.health == 0:
            self.vikingArmy.remove(target)
        
        return result
        

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        
            



