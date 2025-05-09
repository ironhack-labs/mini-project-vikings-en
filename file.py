from vikingsClasses import War, Viking, Saxon
import random

war = War()

vikings = []
vikings.append(Viking("Desi", 100, 7))
vikings.append(Viking("JD", 100, 7))
vikings.append(Viking("Iva", 100, 7))
vikings.append(Viking("Georg", 100, 7))
vikings.append(Viking("Jonathan", 100, 7))
vikings.append(Viking("Simbiat", 100, 7))
vikings.append(Viking("Katja", 100, 7))
vikings.append(Viking("Ana", 100, 7))
vikings.append(Viking("Montassar", 100, 7))
vikings.append(Viking("Joker", 100, 7))

# saxons = []
# saxons.append(Saxon(100,5)) * 10



for viking in vikings:
    war.addViking(viking)
   
for index in range(9):
    war.addSaxon(Saxon(100, 5))
    
print(war.saxonArmy)
print(war.vikingArmy)
# for index in range(20):
# while war.isWarOver() == False:
#     if random.random() < 0.5:          # random.random() → float in [0.0, 1.0)
#         print(war.vikingAttack())
#     else:
#         print(war.saxonAttack())
    
#Define functions to create the workflow of the game: i.e. functions to create teams (maybe you can create random teams with your classmates' names), run the game, etc.