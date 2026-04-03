# With a correction already implemented: dont forget to initialize an instance of Class "War"


from ragnarok_classes import Soldier, Viking, Saxon, War
import random
import time


great_war = War()

#Create 5 Vikings
chosen_valkyrie = []
while len(great_war.vikingArmy) != 5 :
    valkyria = random.choice(list(Viking.VICKING_NAMES.keys()))
    if valkyria not in chosen_valkyrie:
        chosen_valkyrie.append(valkyria)
        great_war.addViking(Viking(valkyria,100,random.randint(0,100)))

  
#print(Viking(random.choice(Viking.VICKING_NAMES),100,59))
#Create 5 Saxons
for i in range(0,5):
    if i:
        great_war.addSaxon(Saxon(random.choice(Saxon.CREATURES_NAMES),100,random.randint(0,100)))


timer= 0.1


round = 0
vicking_lord = random.choice(great_war.vikingArmy).name
rd = random.choice(great_war.vikingArmy)
#print(f"{vicking_lord}: {rd.battleCry()}")
while great_war.showStatus() == "Valkyries and Creatures are still in the thick of battle.":
    round += 1
    time.sleep(timer)
    #print(f"{great_war.vikingAttack().}: {rd.battleCry()}")
    print(great_war.vikingAttack())
    time.sleep(timer)
    print(great_war.saxonAttack())
    
    if round % 5 == 0  :
        print(f"\nround: {round} // Viking army: {len(great_war.vikingArmy)} warriors",f"and Saxon army: {len(great_war.saxonArmy)} warriors\n")
        print(great_war.showStatus())
    else:
        continue
"""
m = great_war.showStatus()         
print(m)       
"""



