# With a correction already implemented: dont forget to initialize an instance of Class "War"
from vikingsClasses import Soldier, Viking, Saxon, War
import random

soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]
great_war = War()

# Create 5 Vikings
for i in range(20):
    name = random.choice(soldier_names)
    great_war.addViking(Viking(name, 100, random.randint(50, 100)))

# Create 5 Saxons
for i in range(20):
    great_war.addSaxon(Saxon(100, random.randint(50, 100)))

print("\nTHE GREAT WAR BEGINS!\n")
print(f"\nStarting armies: {len(great_war.vikingArmy)} Vikings vs {len(great_war.saxonArmy)} Saxons\n")

round = 0
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    # Viking attack
    great_war.vikingAttack()
    
    # Check if battle ended after Viking attack
    current_status = great_war.showStatus()
    if current_status != "Vikings and Saxons are still in the thick of battle.":
        print(f"round: {round} // Viking army: {len(great_war.vikingArmy)} warriors and Saxon army: {len(great_war.saxonArmy)} warriors")
        break
    
    # Saxon attack (only if battle continues)
    great_war.saxonAttack()
    
    # Print round summary
    print(f"round: {round} // Viking army: {len(great_war.vikingArmy)} warriors and Saxon army: {len(great_war.saxonArmy)} warriors")
    round += 1

# Final results
print("\nBATTLE ENDED!\n ")
print(great_war.showStatus())
print(f"\nTotal rounds: {round + 1}")