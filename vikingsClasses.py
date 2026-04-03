import random
import csv

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
        super().__init__(health, strength)
        self.name = name

    def battleCry(self):
        return "Odin Owns You All!"

    def receiveDamage(self, damage):
        super().receiveDamage(damage)  
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"


# Saxon
class Saxon(Soldier):
    def receiveDamage(self, damage):
        super().receiveDamage(damage)  
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"


# War
class War:
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []
        self.battle_log = []  

    def addViking(self, viking):
        self.vikingArmy.append(viking)

    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)

    def log_state(self, round_num):  
        if not self.saxonArmy:
            winner = "Vikings"
        elif not self.vikingArmy:
            winner = "Saxons"
        else:
            winner = None

        self.battle_log.append({
            "round": round_num,
            "viking_army": len(self.vikingArmy),
            "saxon_army": len(self.saxonArmy),
            "winner": winner
        })

    def vikingAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return "No attack possible"
        
        viking = random.choice(self.vikingArmy)
        saxon = random.choice(self.saxonArmy)

        damage = viking.attack() 
        result = saxon.receiveDamage(damage)

        if saxon.health <= 0:
            self.saxonArmy.remove(saxon)  

        return result

    def saxonAttack(self):
        if not self.vikingArmy or not self.saxonArmy:
            return "No attack possible"
        
        saxon = random.choice(self.saxonArmy)
        viking = random.choice(self.vikingArmy)

        damage = saxon.attack()
        result = viking.receiveDamage(damage)

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

    def save_to_csv(self, filename="battle_log.csv"):  
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["round", "viking_army", "saxon_army", "winner"])
            writer.writeheader()
            writer.writerows(self.battle_log)



if __name__ == "__main__":
    war = War()

    # Create armies
    for i in range(4):
        war.addViking(Viking(f"Viking_{i}", 100, 50))
        war.addSaxon(Saxon(100, 40))

    round_num = 0

    while war.vikingArmy and war.saxonArmy:
        print(f"round: {round_num} // Viking army: {len(war.vikingArmy)} warriors and Saxon army: {len(war.saxonArmy)} warriors")
        
        war.log_state(round_num)  # log data
        
        war.vikingAttack()
        war.saxonAttack()

        print(war.showStatus())

        round_num += 1

    # Log final state
    war.log_state(round_num)

    # Save dataset
    war.save_to_csv()

    print("\nSimulation complete. Data saved to battle_log.csv")