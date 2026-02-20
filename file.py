import random
from vikingsClasses import Soldier, Viking, Saxon, War  # ajusta si usas otro nombre

def create_ejercito_vikings(n=5):
    nombres = ["albert","andres","archie","dani","david","gerard","german","graham","imanol","laura"]
    vikings = []
    for i in range(n):
        nombre = random.choice(nombres) + f"#{i+1}"
        health = random.randint(80, 120)
        strength = random.randint(15, 30)
        vikings.append(Viking(nombre, health, strength))
    return vikings

def create_ejercito_saxons(n=5):
    saxons = []
    for i in range(n):
        health = random.randint(60, 100)
        strength = random.randint(10, 25)
        saxons.append(Saxon(health, strength))
    return saxons

def main():
    war = War()
    war.vikingArmy = create_ejercito_vikings(5)
    war.saxonArmy = create_ejercito_saxons(5)

    round_num = 1
    # Loop de juego 
    while war.showStatus() == "Vikings and Saxons are still in the thick of battle.":
        # Each round decides who attack (random)
        if random.choice([True, False]):
            res = war.vikingAttack()
            atacante = "Viking"
        else:
            res = war.saxonAttack()
            atacante = "Saxon"
        print(f"Round {round_num}: {atacante} attack -> {res}")
        print(f"  Vikings: {len(war.vikingArmy)} | Saxons: {len(war.saxonArmy)}")
        print("  Status:", war.showStatus())
        round_num += 1

    print("End Result:", war.showStatus())

if __name__ == "__main__":
    main()
