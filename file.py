from vikingsClasses import Viking, Saxon, War
import random

def create_war():
    return War()

def create_vikings(num):
    names = ["Nada", "Reema", "Wareef", "Mayer", "Shatha", "Teif", "Layla", "Albandri"]
    return [Viking(random.choice(names), 100 , random.randint(0, 100)) for _ in range(num)]

def create_saxons(num):
    return [Saxon(100, random.randint(0, 100)) for _ in range(num)]

def add_soldiers_to_war(war, vikings, saxons):
    for viking in vikings:
        war.addViking(viking)
    for saxon in saxons:
        war.addSaxon(saxon)

def battle(war):
    round = 1
    while war.vikingArmy and war.saxonArmy:
        print(f"Round {round}:")
        if random.choice([True, False]):
            print(war.vikingAttack())
        else:
            print(war.saxonAttack())
        print(war.showStatus())
        print("-" * 40)
        round += 1

def main():
    war = create_war()
    vikings = create_vikings(5)
    saxons = create_saxons(5)
    add_soldiers_to_war(war, vikings, saxons)
    round = 0
    battle(war)

if __name__ == "__main__":
    main()
