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
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        # your code here
        super().__init__(health, strength)  
        self.name = name 

    def battleCry(self):
        # your code here
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage  # تقليل الصحة بمقدار الضرر المستلم
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
        # your code here

    def receiveDamage(self, damage):
        # your code here
        self.health -= damage  # تقليل الصحة بناءً على الضرر
        if self.health > 0:
            return f"Saxon has received {damage} points of damage"
        else:
            return f"Saxon has died in act of combat"

# Davicente

class War():
    def __init__(self):
        # your code here
        self.vikings = []  # قائمة لتخزين الفايكنغ
        self.saxons = []   # قائمة لتخزين الساكسونيين

    def addViking(self, viking):
        # your code here
        self.vikings.append(viking)  # إضافة الفايكنغ إلى الحرب
    
    def addSaxon(self, saxon):
        # your code here
        self.saxons.append(saxon)
    
    def vikingAttack(self):
        # your code here
        if len(self.saxons) > 0:
            saxon = self.saxons[0]  # الهجوم على أول ساكسوني
            damage = self.vikings[0].strength  # تحديد الضرر بناءً على قوة الفايكنغ
            return saxon.receiveDamage(damage)

        else:
            return "No Saxons left to attack!"
    
    def saxonAttack(self):
        # your code here
        if len(self.vikings) > 0:
            viking = self.vikings[0]  # الهجوم على أول فايكنغ
            damage = self.saxons[0].strength  # تحديد الضرر بناءً على قوة الساكسوني
            return viking.receiveDamage(damage)
        else:
            return "No Vikings left to attack!"

    def showStatus(self):
        # your code here
        if len(self.vikings) > 0 and len(self.saxons) > 0:
            return f"There are {len(self.vikings)} Vikings and {len(self.saxons)} Saxons left."
        else:
            return "The war is over!"



