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
        self.damage = damage
        self.health -= damage
    

# Viking

class Viking(Soldier):
    VICKING_NAMES =  {
    "Hrist the Shaker": "shakes the ground",
    "Mist the Silent Veil": "summons thick fog",
    "Skeggjöld the Axe": "throws a blazing axe",
    "Skögul the Raging One": "enters battle rage",
    "Hildr the Warrior": "raises the fallen",
    "Thrud the Might": "strikes with force",
    "Hlökk the Shrieking One": "unleashes a scream",
    "Herfjötur the Host-Fetter": "binds with chains",
    "Geirönul the Spear-Bearer": "calls spears from above",
    "Reginleif the Gods'Kin": "channels divine power"
}

    
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    
    def attack(self):
        return super().attack()                 

    def battleCry(self):
        # your code here

        return self.VICKING_NAMES[self.name]
        
    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
        
    

# Saxon


class Saxon(Soldier):
    CREATURES_NAMES = [
    "Fenrir the World-Breaker",
    "Jormungandr the World Serpent",
    "Sleipnir the Eight-Legged Steed",
    "Nidhogg the Corpse-Eater",
    "Huginn and Muninn the Minds of Odin",
    "Garmr the Helhound Guardian",
    "Ratatoskr the Tree-Runner",
    "Skoll and Hati the Sun and Moon Hunters",
    "Hraesvelgr the Wind-Maker",
    "Fafnir the Cursed Dragon"
    ]
    

    def __init__(self, name, health, strength):
        self.name = name
        # your code here
        super().__init__(health, strength)

    def attack(self):
        return super().attack()  

    def receiveDamage(self, damage):
        self.damage = damage
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {self.damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


class War():
    def __init__(self):
        # your code here
        self.vikingArmy = []
        self.saxonArmy = []
        

    def addViking(self, viking):
        # your code here
        self.vikingArmy.append(viking)
    
    
    def addSaxon(self, saxon):
        # your code here
        self.saxon = saxon

        self.saxonArmy.append(self.saxon)
        

    
    def vikingAttack(self):
        # your code here
        if len(self.saxonArmy) !=0 and len(self.vikingArmy) != 0:
            saxon_warrior = self.saxonArmy[random.randrange(len(self.saxonArmy))]
            viking_warrior = random.choice(self.vikingArmy)
            outcome = saxon_warrior.receiveDamage(viking_warrior.attack())
            if saxon_warrior.health <= 0:
                self.saxonArmy.remove(saxon_warrior)

            return f"{viking_warrior.name} {Viking.battleCry(viking_warrior)}\n{outcome}"
        else:
            return ""

    
    def saxonAttack(self):
        # your code here
        if len(self.saxonArmy) !=0 and len(self.vikingArmy) != 0:
            saxon_warrior = self.saxonArmy[random.randrange(len(self.saxonArmy))]
            viking_warrior = random.choice(self.vikingArmy)
            outcome = viking_warrior.receiveDamage(saxon_warrior.attack())
            if viking_warrior.health <= 0:
                self.vikingArmy.remove(viking_warrior)
            return outcome
        else:
            return ""
        
    
  

    def showStatus(self):
        # your code here
        if len(self.saxonArmy) == 0:
            return "\nThe Valkyries stopped the Ragnarok and Asgard is safe!\n"
        elif len(self.vikingArmy) == 0:
            return "\nThe light has fallen, and the world is lost.\n"
        elif len(self.saxonArmy) >= 1 and len(self.vikingArmy) >=1:
            return "Valkyries and Creatures are still in the thick of battle."
        else:
            pass
        

