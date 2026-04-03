# With a correction already implemented: dont forget to initialize an instance of Class "War"


from vikingsClasses import Soldier, Viking, Saxon, War
import random


soldier_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]
great_war = War()

#Create 5 Vikings
for _ in range(0,5):
    great_war.addViking(Viking(soldier_names[random.randint(0,9)],100,random.randint(0,100)))

#Create 5 Saxons
for _ in range(0,5):
    great_war.addSaxon(Saxon(100,random.randint(20,100)))
    
round = 1
while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    
    print(f"\n--- Round {round} ---")
    
    great_war.vikingAttack()
    great_war.saxonAttack()
    
    print(f"Vikings left: {len(great_war.vikingArmy)}")
    print(f"Saxons left: {len(great_war.saxonArmy)}")
    
    round += 1
    
print("\n🏁 FINAL RESULT 🏁")
print(great_war.showStatus())