import random
# Soldier
class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receiveDamage(self, damage):
       self.health -= damage
# Viking
class Viking(Soldier):
    def __init__(self, name, health, strength):
       self.name = name
       super().__init__(health, strength)
    def battleCry(self):
        return "Odin Owns You All!"
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f'{self.name} has died in act of combat'
# Saxon
class Saxon(Soldier):
     def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return 'A Saxon has died in combat'
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
        result = saxon.receiveDamage(viking.strength)
        if saxon.health <= 0:
             self.saxonArmy.remove(saxon)
        return result
    def saxonAttack(self):
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)
        result = viking.receiveDamage(saxon.strength)
        if viking.health <= 0:
            self.vikingArmy.remove(viking)
        return result
    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
# BÔNUS - Batalha Automática
def start_battle():
    # Cria a guerra
    war = War()
    # Adiciona alguns guerreiros
    war.addViking(Viking("Ragnar", 100, 50))
    war.addViking(Viking("Lagertha", 120, 40))
    war.addSaxon(Saxon(80, 30))
    war.addSaxon(Saxon(90, 35))
    print(":crossed_swords:  INÍCIO DA BATALHA! :crossed_swords:")
    print("Vikings vs Saxons!")
    print()
    round_number = 1
    # Loop até alguém ganhar
    while war.saxonArmy and war.vikingArmy:
        print(f"--- Rodada {round_number} ---")
        # Viking ataca
        if war.vikingArmy and war.saxonArmy:
            result = war.vikingAttack()
            print(f":crossed_swords:  Ataque Viking: {result}")
        # Saxon ataca
        if war.saxonArmy and war.vikingArmy:
            result = war.saxonAttack()
            print(f":shield:  Ataque Saxon: {result}")
        print(f"Status: Vikings [{len(war.vikingArmy)}] vs Saxons [{len(war.saxonArmy)}]")
        print()
        round_number += 1
    # Resultado final
    print(":dart: " + war.showStatus())
    print(":trophy: BATALHA FINALIZADA!")
# Executa a batalha
if __name__ == "__main__":
    start_battle()

import random
import time
def generate_viking():
    names = ["Ragnar", "Lagertha", "Bjorn", "Ivar", "Floki", "Harald", "Erik"]
    name = random.choice(names)
    health = random.randint(80, 100)
    strength = random.randint(40, 70)
    return Viking(name, health, strength)
def generate_saxon():
    health = random.randint(50, 70)
    strength = random.randint(30, 50)
    return Saxon(health, strength)
def start_battle():
    war = War()
    viking_count = random.randint(2, 3)
    saxon_count = random.randint(2, 4)
    for _ in range(viking_count):
        war.addViking(generate_viking())
    for _ in range(saxon_count):
        war.addSaxon(generate_saxon())
    print(":crossed_swords:  BATTLE BEGIN! :crossed_swords:")
    print("Vikings vs Saxons!")
    print()
    print("VIKING ARMY:")
    for viking in war.vikingArmy:
        print(f"  {viking.name} - Health: {viking.health}, Strength: {viking.strength}")
    print("\nSAXON ARMY:")
    for i, saxon in enumerate(war.saxonArmy, 1):
        print(f"  Saxon {i} - Health: {saxon.health}, Strength: {saxon.strength}")
    print()
    round_number = 1
    # Loop until someone wins
    while war.saxonArmy and war.vikingArmy:
        print(f"--- Round {round_number} ---")
        # Viking attacks
        if war.vikingArmy and war.saxonArmy:
            result = war.vikingAttack()
            print(f":crossed_swords:  Viking Attack: {result}")
            time.sleep(1)
        # Saxon attacks
        if war.saxonArmy and war.vikingArmy:
            result = war.saxonAttack()
            print(f":shield:  Saxon Attack: {result}")
            time.sleep(1)
        print(f"Status: Vikings [{len(war.vikingArmy)}] vs Saxons [{len(war.saxonArmy)}]")
        print()
        # Wait for user to press Enter before next round
        if war.saxonArmy and war.vikingArmy:
            input("Press ENTER for next round...")
            print()
        round_number += 1
    # Final result
    print(":dart: " + war.showStatus())
    print(":trophy: BATTLE FINISHED!")
# Execute the battle
if __name__ == "__main__":
    start_battle()






