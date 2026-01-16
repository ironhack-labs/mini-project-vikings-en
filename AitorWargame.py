from vikingsClasses import Soldier, Viking, Saxon, War
import random

aitor_war = War()

# Create Armies
# Vikings

"""
viking_names = ["Loki", "Thor", "Odin", "Sif", "Heimdall"]
for name in random.sample(viking_names, k=len(viking_names)):
    aitor_war.addViking(Viking(name,random.randint(70,170),random.randint(10,100)))

# Saxon
for i in range(0,11):
    if i:
        aitor_war.addSaxon(Saxon(random.randint(50,150),random.randint(0,80)))
"""
viking_names = ["Harmandeep", "Suzana", "Aitor"]
for name in random.sample(viking_names, k=len(viking_names)):
    aitor_war.addViking(Viking(name,random.randint(90,170),random.randint(20,100)))

# Saxon
for i in range(0,6):
    if i:
        aitor_war.addSaxon(Saxon(random.randint(50,150),random.randint(0,80)))

# Let's go to War

round = 0
print("¡¡War starts!!")
while aitor_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
    if random.choice([True, False]):
        print(aitor_war.vikingAttack())
    else:
        print(aitor_war.saxonAttack())

    names = [viking.name for viking in aitor_war.vikingArmy]
    print(f"round: {round} // {names} in Viking army",f"and {len(aitor_war.saxonArmy)} warriors in Saxon army")
    print(aitor_war.showStatus())
    round += 1

