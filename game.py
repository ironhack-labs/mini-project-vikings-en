from vikingsClasses import Soldier, Viking, Saxon, War
import random

player_names = ["albert","andres","archie","dani", "david","gerard","german","graham","imanol","laura"]

# Function to create a teams
def create_viking_team(num_vikings):
    vikings = []
    for _ in range(num_vikings):
        if not player_names:  # Check if player_names is empty
            print("Error: player_names is empty!")
            break 
        name = random.choice(player_names)
        health = random.randint(80, 100)
        strength = random.randint(50, 100)
        vikings.append(Viking(name, health, strength))
    return vikings


def create_saxon_team(num_saxons):
    saxons = []
    for _ in range(num_saxons):
        health = random.randint(80, 100)
        strength = random.randint(50, 100)
        saxons.append(Saxon(health, strength))
    return saxons


def run_game():
    print("Welcome to the Viking vs Saxon battle game!")
 
    vikings = create_viking_team(6)
    saxons = create_saxon_team(6)

    great_war = War()
    for viking in vikings:
        great_war.addViking(viking)
    for saxon in saxons:
        great_war.addSaxon(saxon)

    round = 0
    # Game loop
    while great_war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        print(f"Round {round} starting...")
        
        if great_war.vikingArmy:
            great_war.vikingAttack()
        else:
            print("Error: Viking army is empty before attack!")

        if great_war.saxonArmy:
            great_war.saxonAttack()
        else:
            print("Error: Saxon army is empty before attack!")

        print(f"Round: {round} // Viking army: {len(great_war.vikingArmy)} warriors, Saxon army: {len(great_war.saxonArmy)} warriors")
        print(great_war.showStatus())
        round += 1

       
    # Display the result
    if great_war.showStatus() == "Vikings have won the war of the century!":
        print("Congratulations! The Vikings have won the battle!")
    elif great_war.showStatus() == "Saxons have fought for their lives and survive another day...":
        print("The Saxons have won the battle! Better luck next time!")

# Starting the game
if __name__ == "__main__":
    run_game()
