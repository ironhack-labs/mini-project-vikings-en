from vikingsClasses import Soldier, Viking, Saxon, War
import random

war = War()

for _ in range(5):
    viking = Viking(name=f"Viking_{random.randint(1, 100)}", health=100, strength=random.randint(20, 50))
    war.addViking(viking)

for _ in range(5):
    saxon = Saxon(health=100, strength=random.randint(10, 40))
    war.addSaxon(saxon)


round = 1
while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    print(f"\n **ROUND {round}** ")

    print("Viking attacks!")
    print(war.vikingAttack())

    print("Saxon attacks!")
    print(war.saxonAttack())

   
    print(f"\n Current Status: {war.showStatus()}")
    round += 1


print("\n FINAL RESULT:")
print(war.showStatus())
