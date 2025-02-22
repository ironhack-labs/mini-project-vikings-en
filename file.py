from vikingsClases import Viking, Saxon, War
import random

def create_viking(name):
    health = random.randint(50, 100)
    strength = random.randint(20, 40)
    return Viking(name, health, strength)

def create_saxon():
    health = random.randint(40, 80)
    strength = random.randint(15, 30)
    return Saxon(health, strength)

def start_war():
    war = War()

    vikings_names = ["Olaf", "Erik", "Thor", "Freya", "Bjorn"]
    for name in vikings_names:
        war.addViking(create_viking(name))

    for _ in range(5):
        war.addSaxon(create_saxon())

    round_number = 1
    while True:
        print(f"Round {round_number} - Viking Attack:")
        print(war.vikingAttack())

        if war.showStatus() != "There are Vikings and Saxons in the war. The battle is still ongoing.":
            print(war.showStatus())
            break

        print(f"Round {round_number} - Saxon Attack:")
        print(war.saxonAttack())

        if war.showStatus() != "There are Vikings and Saxons in the war. The battle is still ongoing.":
            print(war.showStatus())
            break

        round_number += 1
        print("-------------------------------")

if __name__ == "__main__":
    start_war()
