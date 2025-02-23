from vikingsClasses import Soldier, Viking, Saxon, War
import random

def create_team_vikings(num_vikings):
    viking_team = []
    viking_names = ["Ragnar", "Lagertha", "Bjorn", "Floki", "Ivar", "Ubbe", "Siggy", "Aslaug"]

    for _ in range(num_vikings):
        viking = Viking(random.choice(viking_names), random.randint(50, 100), random.randint(5, 15))
        viking_team.append(viking)

    return viking_team

def create_team_saxons(num_saxons):
    saxon_team = []

    for _ in range(num_saxons):
        saxon = Saxon(random.randint(30, 70), random.randint(3, 8))
        saxon_team.append(saxon)

    return saxon_team

def run_game():
    war = War()

    viking_team = create_team_vikings(5)  # Create a team of 5 Vikings
    saxon_team = create_team_saxons(5)    # Create a team of 5 Saxons

    for viking in viking_team:
        war.addViking(viking)

    for saxon in saxon_team:
        war.addSaxon(saxon)

    while war.vikingArmy and war.saxonArmy:
        viking_attack_result = war.vikingAttack()
        print(f"Viking attacks: {viking_attack_result}")

        saxon_attack_result = war.saxonAttack()
        print(f"Saxon counterattacks: {saxon_attack_result}")

    print(war.showStatus())

if __name__ == "__main__":
    run_game()