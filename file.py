import random
from vikingsClasses import Viking, Saxon, War

# Function to create a Viking team 
def create_viking_army(num_vikings):
    viking_names = ["Sven", "Ragnar", "Erik", "Sune", "Ivar", "Rune", "Ole"]
    vikings = [Viking(random.choice(viking_names), random.randint(50, 100), random.randint(30, 50)) for _ in range(num_vikings)]
    return vikings

# Function to create a Saxon army
def create_saxon_army(num_saxons):
    saxons = [Saxon(random.randint(40, 90), random.randint(20, 40)) for _ in range(num_saxons)]
    return saxons

# to start the war
def start_game():
    print(" Welcome to Vikings vs. Saxons game! \n")

    war = War()

    vikings = create_viking_army(5)
    saxons = create_saxon_army(5)

    for viking in vikings:
        war.addViking(viking)
    
    for saxon in saxons:
        war.addSaxon(saxon)

    round_num = 1
    while war.vikingArmy and war.saxonArmy:
        print(f"\nRound {round_num} ")
        
        if random.choice([True, False]):
            print("Vikings attack!")
            print(war.vikingAttack())
        else:
            print("Saxons attack!")
            print(war.saxonAttack())

        round_num += 1

    # Show winner
    print("\ngame is Over! ")
    print(war.showStatus())

if __name__ == "__main__":
    start_game()
