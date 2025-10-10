from vikingsClasses import Soldier, Viking, Saxon, War

#Create armies
war=War()

#Add vikings
war.addViking(Viking("Harald", 150, 25))
war.addViking(Viking("Olaf", 120, 20))
war.addViking(Viking("Erik", 170, 30))
war.addViking(Viking("Thor", 200, 50))
war.addViking(Viking("Odin", 133, 22))

#Add saxons
war.addSaxon(Saxon(110, 25))
war.addSaxon(Saxon(140, 34))
war.addSaxon(Saxon(152, 40))
war.addSaxon(Saxon(132, 32))
war.addSaxon(Saxon(135, 36))

#Run one turn
print("Viking attacks!")
print(war.vikingAttack())
print("Saxon attacks!")
print(war.saxonAttack())
print(war.showStatus())