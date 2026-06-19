from viking_war_2 import Berserker, Archer

ragnar = Berserker("Ragnar", 100, 20)
print(ragnar.name)
print(ragnar.health)
print(ragnar.attack())
print(ragnar.battleCry())


bjorn = Archer("Bjorn", 80, 25)
print(bjorn.name)
print(bjorn.health)
print(bjorn.attack())
print(bjorn.battleCry())