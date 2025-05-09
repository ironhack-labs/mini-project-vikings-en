import vikingsClasses as vik
import random
from random import randrange


# Variables
namelist = ["Bjorn", "Erik", "Leif", "Ragnar", "Ivar", "Harald", "Sigurd", "Thorstein", "Olaf", "Eirik",
    "Hakon", "Gunnar", "Ulf", "Arne", "Skallagrim", "Snorri", "Sten", "Trygve", "Halfdan", "Ketill","Astrid", "Freydis", "Gudrun", "Ingrid", "Sigrid", "Brynhild", "Thyra", "Helga", "Ragnhild", "Kari",
    "Liv", "Ylva", "Torhild", "Solveig", "Aslaug", "Gunnhild", "Eydis", "Alfhild", "Hilde", "Skadi"]

valuedict = {
    'Saxon': {
        'num': None,
        'strength': (5,11),
        'health': (80,150)
    },
    'Viking': {
        'num': None,
        'strength': (8,20),
        'health': (140,220)       
    }
}

groups = ['Saxon','Viking']

# Functions

def raise_army(num,group,war):
    """ Raises an army of type {group} with {num} members in {war}
    
    num: number of members of army to be raised
    group: the group the army belongs to
        - 'Saxon' for Saxon
        - 'Viking' for Viking
    war: a War object
    """
    
    if group == 'Saxon':
        for _ in range(num):
            tmp = vik.Saxon(randrange(valuedict[group]['health'][0],valuedict[group]['health'][1]),
                        randrange(valuedict[group]['strength'][0],valuedict[group]['strength'][1]))
            war.addSaxon(tmp) 
           
    elif group == 'Viking':
        for _ in range(num):
            tmp_vik = vik.Viking(random.choice(namelist),
                          randrange(valuedict[group]['health'][0],valuedict[group]['health'][1]),
                        randrange(valuedict[group]['strength'][0],valuedict[group]['strength'][1]))
            war.addViking(tmp_vik)

    print(f'Raised an army of {num} {group}s')
    

#
# MAIN PROGRAMME
#

# Greeting and input
print('Welcome to Saxons and Vikings 0.1')
print('---------------------------------\n')


# Creating war instance
w1 = vik.War()


# Setting up armies
for g in groups:
    while not isinstance(valuedict[g]['num'], int):
        choice = input(f'Please enter the desired size of the {g} army: ')
        if choice.isdigit():
            valuedict[g]['num'] = int(choice)

    print(f'Raising {g} army')
    raise_army(valuedict[g]['num'],g,w1)


# double checking functionality for debugging
# print(len(w1.vikingArmy))
# print(len(w1.saxonArmy))

# for x in w1.vikingArmy:
#     print(x.name, x.strength, x.health)

######################
# Action cycle
#####################

while w1.showStatus() == 'Vikings and Saxons are still in the thick of battle.':
    if randrange(10) < 6:
        print(w1.saxonAttack())
    else:
        print(w1.vikingAttack())
    
# Final result
print('\nThe battle has ended!\n')

print(w1.showStatus())

