import random
from vikingsClasses import Soldier, Viking, Saxon, War

# Function to create a Viking team
def create_viking_team(names, health_range=(50, 100), strength_range=(10, 20)):
    vikings = []
    for name in names:
        health = random.randint(*health_range)
        strength = random.randint(*strength_range)
        vikings.append(Viking(name, health, strength))
    return vikings

# Function to create a Saxon team
def create_saxon_team(num_saxons, health_range=(50, 100), strength_range=(5, 15)):
    saxons = []
    for _ in range(num_saxons):
        health = random.randint(*health_range)
        strength = random.randint(*strength_range)
        saxons.append(Saxon(health, strength))
    return saxons

# Function to simulate the war
def run_battle(war):
    print("The battle begins!\n")

    while war.vikings and war.saxons:
        # Vikings attack
        print(war.vikingAttack())
        print(war.showStatus())

        if not war.saxons:  # Check if Saxons are all dead
            break

        # Saxons attack
        print(war.saxonAttack())
        print(war.showStatus())

    # Display the outcome
    print("\nGame Over!")
    print(war.showStatus())

# Main game function
def main():
    viking_names = ["Erik", "Olaf", "Bjorn", "Leif", "Thorvald"]

    # Create Viking and Saxon teams
    vikings = create_viking_team(viking_names)
    saxons = create_saxon_team(5)

    # Create a new war
    war = War()

    # Add the teams to the war
    for viking in vikings:
        war.addViking(viking)

    for saxon in saxons:
        war.addSaxon(saxon)

    # Run the battle
    run_battle(war)

if __name__ == "__main__":
    main()