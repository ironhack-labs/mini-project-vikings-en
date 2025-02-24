from vikingsClasses import Viking,Saxon,War
import random

war = War()


for v in range(10):
    viking = Viking(name=f'A Viking {v}',health=100,strength=100)
    war.addViking(viking)
for s in range(10):
    saxon = Saxon(health=100,strength=100)
    war.addSaxon(saxon)


while len(war.saxonArmy) > 0 and len(war.vikingArmy) > 0:
    if random.choice([True,False]):
        print(war.vikingAttack())
    else:
        print(war.saxonAttack())

print(war.showStatus())

