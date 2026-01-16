import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health                # mede a vida de cada soldado
        self.strength = strength            # mede a força de cada soldado
    
    def attack(self):
        return self.strength                # quando ataca mede a força de cada um

    def receiveDamage(self, damage):
        self.health -= damage               # quando é atacado reduz a vida
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)       # importamos as propriedades de class pai para a classe filho viking
        self.name = name                         # criamos o atributo de nome

    def battleCry(self):
        return "Odin Owns You All!"              # 

    def receiveDamage(self, damage):
        self.health -= damage                    # 
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

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
        if self.vikingArmy == [] or self.saxonArmy == []:
            pass
        else :
            viking = random.choice(self.vikingArmy)
            saxon = random.choice(self.saxonArmy)
            result = saxon.receiveDamage(viking.strength)
            if saxon.health <= 0:
                self.saxonArmy.remove(saxon)
            return result
    
    def saxonAttack(self):
        if self.vikingArmy == [] or self.saxonArmy == []:
            pass
        else:
            viking = random.choice(self.vikingArmy)
            saxon = random.choice(self.saxonArmy)
            result = viking.receiveDamage(saxon.strength)
            if viking.health <= 0:
                self.vikingArmy.remove(viking)
            return result

    def showStatus(self):
        if len(self.saxonArmy) ==0:
            return "Vikings have won the war of the century!"
        if len(self.vikingArmy) ==0:
            return "Saxons have fought for their lives and survive another day..."
        if len(self.vikingArmy) >=1 and len(self.saxonArmy) >= 1:
            return "Vikings and Saxons are still in the thick of battle."
    pass


