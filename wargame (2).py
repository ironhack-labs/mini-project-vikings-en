from vikingsClasses import Soldier, Viking, Saxon, War
import random

def create_warriors(war, num_vikings=5, num_saxons=5):
    """Creates a specified number of Viking and Saxon warriors."""
    soldier_names = ["Albert", "Andres", "Archie", "Dani", "David", "Gerard", "German", "Graham", "Imanol", "Laura"]
    
    for _ in range(num_vikings):
        name = random.choice(soldier_names)
        health = random.randint(80, 120)
        strength = random.randint(30, 100)
        war.addViking(Viking(name, health, strength))
    
    for _ in range(num_saxons):
        health = random.randint(80, 120)
        strength = random.randint(30, 100)
        war.addSaxon(Saxon(health, strength))

def battle(war):
    """Simulates the battle between Vikings and Saxons."""
    round_count = 1
    
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(f"Round {round_count}: \n")
        if war.vikingArmy and war.saxonArmy:
            print(war.vikingAttack())
        if war.vikingArmy and war.saxonArmy:
            print(war.saxonAttack())
        
        print(f"Viking army size: {len(war.vikingArmy)} | Saxon army size: {len(war.saxonArmy)}\n")
        print("-" * 40)
        round_count += 1
    
    print("Final Outcome:")
    print(war.showStatus())

if __name__ == "__main__":
    great_war = War()
    create_warriors(great_war)
    battle(great_war)
