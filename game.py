from vikingsClasses import Soldier, Viking, Saxon, War
import random

# Create a war instance
battle = War()

# Sample Viking names
viking_names = ["Renad", "Yara", "Rahaf", "Tala"]

# Create Vikings and add them to the war
for _ in range(3):  
    name = random.choice(viking_names)
    health = random.randint(50, 100)
    strength = random.randint(10, 20)
    battle.addViking(Viking(name, health, strength))

# Create Saxons and add them to the war
for _ in range(3):
    health = random.randint(50, 100)
    strength = random.randint(10, 20)
    battle.addSaxon(Saxon(health, strength))


# The loop continues as long as there are soldiers in both armies
while len(battle.vikingArmy) > 0 and len(battle.saxonArmy) > 0:
    
    # Randomly choose whether the Vikings or the Saxons will attack
    if random.choice([True, False]):
        # If the result is True, the Vikings will attack
        print(battle.vikingAttack())
    else:
        # If the result is False, the Saxons will attack
        print(battle.saxonAttack())

    # Print the current status of the battle after each attack
    print(battle.showStatus())  

print("The war has ended!")
