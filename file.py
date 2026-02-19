import random
from vikingsClasses import War, Viking, Saxon

def create_viking_horde(number_of_vikings):
    names = ["Olaf", "Sigurd", "Ivar", "Ubbe","Ragnar","Bjorn","Loki"]
    horde = []
    for v in range(number_of_vikings):
        name = random.choise(names)

        # Viking with a random health and random str
        new_viking = Viking(name, random.randint(100,150), random.randint(50,100))
        horde.append(new_viking)


